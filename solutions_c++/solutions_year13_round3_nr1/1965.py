#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char s[1000005];
long long dp[1000005];
long long total[1000005];
int main()
{
	freopen("D:OUTPUT.txt", "w", stdout);
	int t;
	cin>>t;
	int i,j,n,l;
	int ca=1;
	while(t--)
	{
		scanf("%s%d",s,&n);
		l=strlen(s);
		for(i=0;i<l;i++)
		{

			if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u')
			{
				dp[i]=0;
			}
			else if(i==0)
			{
				dp[i]=1;
			}
			else
			{
				dp[i]=dp[i-1]+1;
			}
		}
		long long x;
		int lasti;
		memset(total,0,sizeof(total));
		total[0]=dp[0]>=n?1:0;
		if(dp[0]>=n)
			lasti=0;
		else
			lasti=-1;
		for(i=1;i<l;i++)
		{
			if(dp[i]>=n)
			{
				total[i]+=(i-n+2);
				lasti=i;
			}
			else
			{
				if(lasti==-1)
					continue;
				else
				{
					total[i]+=(lasti-n+2);
				}
			}
		}
		for(i=1;i<l;i++)
		{
			total[i]+=total[i-1];
		}
		printf("Case #%d: %lld\n",ca++,total[l-1]);
	}
	return 0;
}
