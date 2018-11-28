#include<cstdio>
#include<algorithm>
#include<string.h>
using namespace std;

int dp[1000001],i=0;

int rev(int n)
{
	int m=0;
	while(n>0)
	{
		m=m*10 + n%10;
		n/=10;
	}
	return m;
}

int calc(int p,int n)
{
	int a,ans=0;
	if(p<=200000)
		return dp[p];
	else
	{
		if(p==n)
			return 1;
		else
		{
			a=rev(p);
			if(a>p&&a<=n)
				return min(1+calc(a,n),1+calc(p+1,n));
			else
				return 1+calc(p+1,n);
		}
	}
}

int main()
{
	int ans,t,n,a,b,c,i,j,k;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		memset(dp,0,sizeof(dp));
		dp[n]=1;
		for(j=n-1;j>=1;j--)
		{
			a=rev(j);
			if(a>j&&a<=n)
				dp[j]=min(1+dp[a],1+dp[j+1]);
			else
				dp[j] = 1+dp[j+1];
		}
		ans=dp[1];		
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
