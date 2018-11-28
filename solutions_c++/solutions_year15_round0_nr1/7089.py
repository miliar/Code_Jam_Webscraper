#include<iostream>
#define I 100
#define J 1001
using namespace std;
int main()
{
	int t,smax[I],i,j,count,result[I],s[J],temp;
	char schar[I][J];
	cin>>t;
	for(i=0;i<t;i++)
		cin>>smax[i]>>schar[i];
	for(i=0;i<t;i++)
	{
		count=0;
		result[i]=0;
		for(j=0;j<=smax[i];j++)
		{
			s[j]=(int)schar[i][j]-48;
			if(j<=count)
				count+=s[j];
			else
			{
				temp=j-count;
				result[i]+=temp;
				count+=temp;
				count+=s[j];
			}
		}
	}
	for(i=0;i<t;i++)
		cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
	return 0;
}

