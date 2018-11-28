#include <iostream>
#include <fstream>
using namespace std;

main()
{
	int i,j,k;
	int p,q,m,n,a,b,a1;
	int N,M;
	int temp1,temp2,temp3;
	int T;
	int S[100][100];
	int B1[100][100];
	ifstream infile("input");
	ofstream outfile("output",ios_base::app);
	infile>>T;
	for(i=0;i<T;i++)
	{
		outfile<<"Case #"<<i+1<<": ";
		infile>>N;		//N行
		infile>>M;		//M列

		for(j=0;j<N;j++)		//输入二维矩阵
		{
			for(k=0;k<M;k++)
			{
				infile>>S[j][k];
			}
		}
		for(j=0;j<N;j++)		//输入二维矩阵
		{
			for(k=0;k<M;k++)
			{
				B1[j][k]=S[j][k];
			}
		}

		if((N==1)||(M==1))		//只有1行或1列时
		{
			outfile<<"YES"<<endl;
			continue;
		}

		if(N==2)		//只有2行时
		{
			m=0;
			n=0;
			a=0;
			b=0;
			a1=0;
			for(k=0;k<M;k++)		//如果第0行全部相等，第1行不全部相等，第1行必须比第0行高
			{
				if(S[0][0]==S[0][k])
				{
					m=m+1;
				}
				if(S[1][0]==S[1][k])
				{
					n=n+1;
				}
			}
			if((m==M)&&(n==M))		//2行都相等
			{
				outfile<<"YES"<<endl;
				goto p1;
			}
			if((m==M)&&(n!=M))		//第0行相等，第1行不相等
			{
				for(k=0;k<M;k++)
				{
					if(S[1][k]>=S[0][k])
					{
						a=a+1;
					}
				}
				if(a==M)
				{
					outfile<<"YES"<<endl;
					goto p1;
				}
			}
			if((m!=M)&&(n==M))		//第1行相等，第0行不相等
			{
				for(k=0;k<M;k++)
				{
					if(S[0][k]>=S[1][k])
					{
						a1=a1+1;
					}
				}
				if(a1==M)
				{
					outfile<<"YES"<<endl;
					goto p1;
				}
			}
/*			for(k=0;k<M;k++)		//两行都不相等
			{
				if(S[0][k]==S[1][k])
				{
					b=b+1;
				}
			}
			if(b==M)
			{
				outfile<<"YES"<<endl;
				goto p1;
			}
			else
			{
				outfile<<"NO"<<endl;
				goto p1;
			}
*/
		}

		if(M==2)		//只有2列时
		{
			m=0;
			n=0;
			a=0;
			b=0;
			a1=0;
			for(k=0;k<N;k++)		//如果第0列全部相等，第1列不全部相等，第1列必须比第0行高
			{
				if(S[0][0]==S[k][0])
				{
					m=m+1;
				}
				if(S[0][1]==S[k][1])
				{
					n=n+1;
				}
			}
			if((m==N)&&(n==N))		//2列都相等
			{
				outfile<<"YES"<<endl;
				goto p1;
			}
			if((m==N)&&(n!=N))		//第0列相等，第1列不相等
			{
				for(k=0;k<N;k++)
				{
					if(S[k][1]>=S[k][0])
					{
						a=a+1;
					}
				}
				if(a==N)
				{
					outfile<<"YES"<<endl;
					goto p1;
				}
			}
			if((m!=N)&&(n==N))		//第1列相等，第0列不相等
			{
				for(k=0;k<N;k++)
				{
					if(S[k][0]>=S[k][1])
					{
						a1=a1+1;
					}
				}
				if(a1==N)
				{
					outfile<<"YES"<<endl;
					goto p1;
				}
			}
/*			for(k=0;k<N;k++)		//2列都不相等时
			{
				if(S[0][k]==S[1][k])
				{
					b=b+1;
				}
			}
			if(b==N)
			{
				outfile<<"YES"<<endl;
				goto p1;
			}
			else
			{
				outfile<<"NO"<<endl;
				goto p1;
			}
*/
		}










		if(N==2)			//只有2行时
		{
			temp1=S[0][0];
			temp2=S[1][0];
			for(k=1;k<M;k++)		//取出第0行最大值
			{
				if(S[0][k]>=S[0][k-1])
				{
					temp1=S[0][k];
				}
			}
			for(k=0;k<M;k++)		//将最大值的元素赋值为0
			{
				if(S[0][k]==temp1)
				{
					S[0][k]=0;
				}
			}
			for(k=1;k<M;k++)		//取出第1行最大值
			{
				if(S[1][k]>=S[1][k-1])
				{
					temp2=S[1][k];
				}
			}
			for(k=0;k<M;k++)		//将最大值的元素赋值为0
			{
				if(S[1][k]==temp2)
				{
					S[1][k]=0;
				}
			}
			for(k=0;k<M;k++)		//第0行最大值的列必须是第0行的最大值的列
			{
				if(S[0][k]==0)
				{
					if(S[1][k]!=0)
					{
						outfile<<"NO"<<endl;
						goto p1;
					}
				}
			}
			for(k=0;k<M;k++)		//第1行最大值的列必须是第1行最大值的列
			{
				if(S[1][k]==0)
				{
					if(S[0][k]!=0)
					{
						outfile<<"NO"<<endl;
						goto p1;
					}
				}
			}
			for(k=0;k<M;k++)		//不为最大值的列必须相等
			{
				if(S[0][k]!=0)
				{
					if(S[0][k]!=S[1][k])
					{
						outfile<<"NO"<<endl;
						goto p1;
					}
				}
			}
			outfile<<"YES"<<endl;
			goto p1;
		}

		if(M==2)		//只有2列时
		{
			temp1=S[0][0];
			temp2=S[0][1];
			for(k=1;k<N;k++)		//取出第0列最大值
			{
				if(S[k][0]>=S[k-1][0])
				{
					temp1=S[k][0];
				}
			}
			for(k=0;k<N;k++)		//将最大值的元素赋值为0
			{
				if(S[k][0]==temp1)
				{
					S[k][0]=0;
				}
			}
			for(k=1;k<N;k++)		//取出第1列最大值
			{
				if(S[k][1]>=S[k-1][1])
				{
					temp2=S[k][1];
				}
			}
			for(k=0;k<N;k++)		//将最大值的元素赋值为0
			{
				if(S[k][1]==temp2)
				{
					S[k][1]=0;
				}
			}
			for(k=0;k<N;k++)		//第0列最大值的列必须是第1列的最大值的列
			{
				if(S[k][0]==0)
				{
					if(S[k][1]!=0)
					{
						outfile<<"NO"<<endl;
						goto p1;
					}
				}
			}
			for(k=0;k<M;k++)		//第1列最大值的列必须是第0列最大值的列
			{
				if(S[k][1]==0)
				{
					if(S[k][0]!=0)
					{
						outfile<<"NO"<<endl;
						goto p1;
					}
				}
			}
			for(k=0;k<N;k++)		//不为最大值的行必须相等
			{
				if(S[k][0]!=0)
				{
					if(S[k][0]!=S[k][1])
					{
						outfile<<"NO"<<endl;
						goto p1;
					}
				}
			}
			outfile<<"YES"<<endl;
			goto p1;
		}

		for(j=0;j<N;j++)		//行和列都大于等于3的二维数组,先找出行相等的所有行,赋值为0
		{
			m=0;
			temp1=S[j][0];
			for(k=1;k<M;k++)
			{
				if(S[j][k]!=temp1)
				{
					break;
				}
				else
				{
					m=m+1;
				}
			}
			if(m==(M-1))
			{
				for(k=0;k<M;k++)
				{
					B1[j][k]=0;
				}
			}
		}

		for(j=0;j<M;j++)		//找出列相等的所在列，赋值为0
		{
			m=0;
			temp1=S[0][j];
			for(k=1;k<N;k++)
			{
				if(S[k][j]!=temp1)
				{
					break;
				}
				else
				{
					m=m+1;
				}
			}
			if(m==(N-1))
			{
				for(k=0;k<N;k++)
				{
					B1[k][j]=0;
				}
			}
		}


		for(j=0;j<N;j++)		//找出没有行列相等那些元素，这些元素必须是大于等于所在行列的其他元素
						//这些元素必须是且唯一是所在行列的第二种元素
		{
			for(k=0;k<M;k++)		
			{
				if(B1[j][k]!=0)
				{
					temp2=S[j][k];
					for(m=0;m<M;m++)	//检查是不是行中最大的元素
					{
						if(S[j][m]>temp2)
						{
							outfile<<"NO"<<endl;
							goto p1;
						}
					}
					for(m=0;m<M;m++)	//检查行中是不是就这两种元素
					{
						if(S[j][m]!=temp2)
						{
							temp1=S[j][m];
							break;
						}
					}
					for(m=0;m<M;m++)
					{
						if((S[j][m]!=temp1)&&(S[j][m]!=temp2))
						{
							outfile<<"NO"<<endl;
							goto p1;
						}
					}
					B1[j][k]=0;
				}
			}
		}

		for(j=0;j<N;j++)		//找出没有行列相等那些元素，这些元素必须是大于等于所在行列的其他元素
						//这些元素必须是且唯一是所在行列的第二种元素
		{
			for(k=0;k<M;k++)		
			{
				if(B1[j][k]!=0)
				{

					for(m=0;m<N;m++)	//检查是不是列中最大的元素
					{
						if(S[m][k]>temp2)
						{
							outfile<<"NO"<<endl;
							goto p1;
						}
					}


					for(m=0;m<N;m++)	//检查列中是不是就这两种元素
					{
						if(S[m][k]!=temp2)
						{
							temp1=S[m][k];
							break;
						}
					}
					for(m=0;m<N;m++)
					{
						if((S[m][k]!=temp1)&&(S[m][k]!=temp2))
						{
							outfile<<"NO"<<endl;
							goto p1;
						}
					}
					B1[j][k]=0;
				}
			}
		}










/*
		for(j=1;j<N-1;j++)			//对内部的每一个数的横竖行进行判断
		{
			for(k=1;k<M-1;k++)
			{
				m=0;
				n=0;
				a=0;
				b=0;

				for(p=0;p<M;p++)	
				{
					if(S[j][k]==S[j][p])	//第i横行所有数都相等
					{
						m=m+1;
					}
					if(S[j][k]>=S[j][p])	//第i横行最高的草
					{
						a=a+1;
					}
				}
				for(p=0;p<N;p++)	
				{
					if(S[j][k]==S[p][k])	//第k竖列所有数都相等
					{
						n=n+1;
					}
					if(S[j][k]>=S[p][k])	//第k列最高的草
					{
						b=b+1;
					}

				}
				if((m==M)||(n==N))
				{
					continue;
				}
				else
				{
					outfile<<"NO"<<endl;
					goto p1;
				}
			}

		}
*/
		for(j=0;j<N;j++)
		{
			for(k=0;k<M;k++)
			{
				if(B1[j][k]!=0)
				{
					outfile<<"NO"<<endl;
					goto p1;
				}
			}
		}
		outfile<<"YES"<<endl;
p1:
	continue;
	}	
}
