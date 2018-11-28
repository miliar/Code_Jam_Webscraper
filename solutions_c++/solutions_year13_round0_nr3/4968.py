#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

main()
{
	int i,j,k;
	int m,n,p,q;
	long Num=0;
	float Num2;
	int Num3;
	char HuiWen1[3],HuiWen2[3];
	int T;
	long A,B;
	ifstream infile("input");
	ofstream outfile("output",ios_base::app);
	infile>>T;
	for(i=0;i<T;i++)
	{
		Num=0;
		infile>>A;
		infile>>B;
		for(j=A;j<=B;j++)
		{
//先判断j本身是不是回文
			if(j==1000)
			{
				break;
			}
			else if(j>=100)
			{
				HuiWen1[0]=j/100;
				HuiWen1[1]=(j%100)/10;
				HuiWen1[2]=j%10;
				if(HuiWen1[0]!=HuiWen1[2])
				{
					continue;
				}
				Num2=sqrt(j);
				if((Num2-(int)Num2)!=0)
				{
					continue;
				}
				Num3=Num2;
				HuiWen2[0]=Num2/10;
				HuiWen2[1]=Num3%10;
				if(HuiWen2[0]!=HuiWen2[1])
				{
					continue;
				}
				Num=Num+1;
			}
			else if(j>=10)
			{
				HuiWen1[0]=j/10;
				HuiWen1[1]=j%10;
				if(HuiWen1[0]!=HuiWen1[1])
				{
					continue;
				}
				Num2=sqrt(j);
				if((Num2-(int)Num2)!=0)
				{
					continue;
				}
				Num=Num+1;
			}
			else
			{
				Num2=sqrt(j);
				if((Num2-(int)Num2)!=0)
				{
					continue;
				}
				Num=Num+1;
			}
		}
		outfile<<"Case #"<<i+1<<": ";
		outfile<<Num<<endl;
	}
}
