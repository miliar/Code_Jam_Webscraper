#include<iostream>
using namespace std;
int main()
{
	freopen("A-small-attempt2.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取
	freopen("output.txt","w",stdout); //输出重定向，输出数据将保存在out.txt文件中

	int nCount =  0;			//对比的数量
	cin>>nCount;		
	int nPreSaves[4];			//保存相应的值
	int nPreBufs[4];			//保存相应的值
	int nSelectRowCount = 0;    //选择的行列
	int nSameNum = 0;			//相似的数量
	int nSame = 0;				//相似的数
	for (int i = 0 ; i < nCount ; i++)
	{
		nSameNum = 0;
		cin>>nSelectRowCount;
		nSelectRowCount--;
		for (int j = 0; j < 4; j++)
		{
			if (j == nSelectRowCount)
			{
				cin>>nPreSaves[0]>>nPreSaves[1]>>nPreSaves[2]>>nPreSaves[3];
			}
			else
			{
				cin>>nPreBufs[0]>>nPreBufs[1]>>nPreBufs[2]>>nPreBufs[3];
			}
		}

		cin>>nSelectRowCount;
		nSelectRowCount--;
		for (int j = 0; j < 4 ; j++)
		{
			cin>>nPreBufs[0]>>nPreBufs[1]>>nPreBufs[2]>>nPreBufs[3];

			if (j == nSelectRowCount)
			{
				for (int k = 0 ; k < 4 ; k++)
				{
					for (int p = 0 ; p < 4 ; p++)
					{
						if (nPreBufs[p] == nPreSaves[k])
						{
							nSameNum++;
							nSame = nPreSaves[k];
							break;
						}
					}
				}
			}	
		}
		cout<<"Case #"<<i+1<<": ";
		switch(nSameNum)
		{
		case 0:
			cout<<"Volunteer cheated!"<<endl;
			break;
		case 1:
			cout<<nSame<<endl;
			break;
		default:
			cout<<"Bad magician!"<<endl;
		}
	}
//	fclose(stdin);//关闭文件
	fclose(stdout);//关闭文件
	return 0;
}



