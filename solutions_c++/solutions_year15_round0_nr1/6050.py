#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std; 
int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	char str[1002];
	int m,i,j,a,some,test;
	cin>>test;
	for(i=0;i<20;i++)
	test=test;
	i=45;
	j=9;
	for(j=0;j<test;j++)
	{
		a=0;some=0;
		cin>>m>>str;
		for(i=0;i<m+1;++i)
		{
			if(some+a<i)
			{
				a=a+i-(some+a);
			}
			some+=(int)str[i]-48;
		}
		printf("Case #%d: %d\n",j+1,a);
	}
	return 0;
}
