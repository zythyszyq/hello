#导入各种包
import pandas as pd
from pyreadstat import pyreadstat
import matplotlib.pyplot as plt

#绘图设置
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体

# 读取SPSS格式数据

def 绘制单个类别变量柱状图(数据表, 变量: str):
    """ 绘制单个类别变量柱状 """
    x = 数据表[变量].value_counts().index
    y = 数据表[变量].value_counts(normalize=True).values * 100
    # 创建图
    fig, ax = plt.subplots()
    # 绘制柱状图
    rects1 = ax.bar(x, y)
    # 设置x轴变量名称
    ax.set_xlabel(变量)
    # 设置y轴最大值
    ax.set_ylim(ymax=100)
    # 在柱上方显示对应的值
    ax.bar_label(rects1, fmt="%.1f", padding=3)
    # 显示图形
    plt.show()



def 读取SPSS数据(文件所在位置及名称):
    """ 读取SPSS文件，保留标签内容和有序变量顺序 """
    result, metadata = pyreadstat.read_sav(
        文件所在位置及名称, apply_value_formats=True, formats_as_ordered_category=True)
    return result, metadata


def 有序变量描述统计函数(表名,变量名):
    result=表名[变量名].value_counts(sort=False)
    描述统计表=pd.DataFrame(result)
    描述统计表['比例']=描述统计表['count']/描述统计表['count'].sum()
    描述统计表['累计比例']=描述统计表['比例'].cumsum()
    return 描述统计表

# 调用自定义函数，执行区间估计推论统计 
import pandas as pd
from scipy import stats
# 打开数据文件
file_path = R"data/movie_data_cleaned.csv"
df_movies = pd.read_csv(file_path)
# 计算均值和标准误差
mean = df_movies['average'].mean()
std_error = stats.sem(df_movies['average'])
# 设定置信水平
confidence_level = 0.95
# 设定自由度
自由度 = len(df_movies['average']) - 1
# 计算置信区间
confidence_interval = stats.t.interval(confidence_level, 自由度, loc=mean, scale=std_error)
# 输出结果
print(F"均值：{mean: .2f}")
print(F"均值在置信水平{confidence_level}下的置信区间为：", confidence_interval)

def 数值变量描述统计1(数据表, 变量名):
    result = 数据表[变量名].describe()
    中位数 = result['median']
    平均值 = result['mean']
    标准差 = result['std']
    return 中位数, 平均值, 标准差


def 数值变量描述统计(数据表, 变量名):
    """ 对数值变量进行描述统计 """
    result = 数据表[变量名].describe()
    return result

  
def goodmanKruska_tau_y(df, x: str, y: str) -> float:  
    """计算两个定序变量相关系数tau_y"""  
    # 取得条件次数表  
    cft = pd.crosstab(df[y], df[x], margins=True)  
    # 取得全部个案数目  
    n = cft.at['All', 'All']  
    # 初始化变量  
    E_1 = E_2 = tau_y = 0  
  
    # 计算E_1  
    for i in range(cft.shape[0] - 1):  
        F_y = cft['All'][i]  
        E_1 += ((n - F_y) * F_y) / n  
  
    # 计算E_2  
    for j in range(cft.shape[1] - 1):  
        for k in range(cft.shape[0] - 1):  
            F_x = cft.iloc[cft.shape[0] - 2, j]  # 根据之前的建议，这里仍使用 cft.shape[0] - 2  
            f = cft.iloc[k, j]  
            E_2 += ((F_x - f) * f) / F_x  
  
    # 计算tau_y  
    tau_y = (E_1 - E_2) / E_1  
  
    return tau_y

def 相关系数强弱判断(相关系数值):
    """ 相关系数强弱的判断 """
    if 相关系数值 >= 0.8:
        return '极强相关'
    elif 相关系数值 >= 0.6:
        return '强相关'
    elif 相关系数值 >= 0.4:
        return '中等程度相关'
    elif 相关系数值 >= 0.2:
        return '弱相关'
    else:
        return '极弱相关或无相关'


def 制作交叉表(数据表, 自变量, 因变量):
    return pd.crosstab(数据表[自变量], 数据表[因变量], normalize='columns', margins=True)
