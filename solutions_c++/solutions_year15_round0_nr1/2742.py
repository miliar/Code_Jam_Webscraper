#include<iostream>
#include<cstdio>
using namespace std;
char ch[3009];
int n;
int main()
{
	int t,cas=0;
	scanf("%d",&t);
	while(t--)
	{
		int ans=0;
		scanf("%d%s",&n,ch);
		int sum=0;
		for(int i=0;i<=n;i++)
		{
			int u = ch[i]-'0';
			if(u>0)
			{
				if(sum<i)ans+=i-sum,sum+=i-sum;
				sum += u;
			}
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}

