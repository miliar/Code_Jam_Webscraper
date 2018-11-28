#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	char string[1002];
	int m,i,j,ans,s,t,n;
	cin>>t;
	for(j=0;j<t;j++)
	{
		ans=0;s=0;
		cin>>m>>string;
		for(i=0;i<=m;i++)
		{
			if(s+ans<i)
			{
				ans=ans+i-(s+ans);
			}
			s+=(int)string[i]-48;
		}
		printf("Case #%d: %d\n",j+1,ans);
	}
	return 0;
}
