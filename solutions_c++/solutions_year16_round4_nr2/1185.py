#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int n,k;
double dp[210][210],p[210],pp[210];
double max(double c1,double c2)
{
	if(c1<c2)
		return c2;
	return c1;
}
double solve()
{
	int i,j;
	dp[0][0]=1.0;
	for(i=1;i<=k;++i)
		for(j=0;j<=i&&j<=k/2;++j)
		{
			dp[i][j]=dp[i-1][j]*(1.0-pp[i]);
			if(j)
				dp[i][j]+=dp[i-1][j-1]*pp[i];
		//	printf("%d %d %lf\n",i,j,dp[i][j]);
		}
	return dp[k][k/2];
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,tt,i,j,s,top;
	double ans;
	scanf("%d",&tt);
	for(t=1;t<=tt;++t)
	{
		ans=0.0;
		scanf("%d%d",&n,&k);
		for(i=1;i<=n;++i)
			scanf("%lf",p+i);
		sort(p+1,p+n+1);
		for(i=0;i<=k;++i)
		{
			top=0;
			for(j=1;j<=i;++j)
				pp[++top]=p[j];
			for(j=n;top<k;--j)
				pp[++top]=p[j];
			if(ans<solve())
				ans=solve();
		}
		printf("Case #%d: %lf\n",t,ans);
	}
	return 0;
}

