#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int ms[102];
int dp[102];

int main()
{
	int t,cas = 1;
	scanf("%d",&t);
	while(t--)
	{
		int a,n,i;
		scanf("%d%d",&a,&n);
		memset(dp,0,sizeof(dp));
		for(i=0;i<n;i++)
		{
			scanf("%d",&ms[i]);
		}
		sort(ms,ms+n);
		if(a==1)
		{
			printf("Case #%d: %d\n",cas++,n);
			continue;
		}
		for(i=0;i<n;i++)
		{
			if(ms[i]<a)
				a += ms[i];
			else
			{
				int tmp = 0;
				while(a<=ms[i])
				{
					tmp ++;
					a += a-1;
				}
				a += ms[i];
				dp[i] = tmp;
				//cout<<tmp<<endl;
			}
		}
		for(i=n-1;i>=0;i--)
			dp[i] = min(dp[i]+dp[i+1],n-i);
		printf("Case #%d: %d\n",cas++,dp[0]);
	}
	return 0;
}
