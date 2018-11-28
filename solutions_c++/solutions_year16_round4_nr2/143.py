#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int n,k;
double a[1000];
double dp[1000][1000];

double test(int T)
{
	int m=0;
	double p[1000];
	for (int i=0;i<n;i++)
		if (T&(1<<i)) p[++m]=a[i+1];
	if (m!=k) return 0;
	dp[0][0]=1;
	for (int i=1;i<=m;i++)
		for (int j=0;j<=i;j++)
		{
			dp[i][j]=dp[i-1][j]*(1-p[i]);
			if (j) dp[i][j] += dp[i-1][j-1]*p[i];
		}
	return dp[m][k/2];
}

double work()
{
	cin>>n>>k;
	for (int i=1;i<=n;i++) cin>>a[i];
	sort(a+1,a+n+1);
	/*
	double ma=0;
	int best=0;
	for (int i=0;i<(1<<n);i++)
	{
		if (test(i) > ma) best = i;
		ma=max(ma,test(i));
	}
	
	return ma;
	*/
	double ma=0;
	for (int D=0;D<=k;D++)
	{
	int m=0;
	double p[1000];
	for (int i=1;i<=n;i++)
		if (i<=D||i>=n-(k-D)+1) p[++m]=a[i];
	dp[0][0]=1;
	for (int i=1;i<=m;i++)
		for (int j=0;j<=i;j++)
		{
			dp[i][j]=dp[i-1][j]*(1-p[i]);
			if (j) dp[i][j] += dp[i-1][j-1]*p[i];
		}
		ma=max(ma,dp[m][k/2]);
	}
	return ma;
}

int main()
{
	freopen ("bb.in", "r",stdin);
	freopen ("bbb.out","w",stdout);
	int T;
	cin>>T;
	for (int i=1;i<=T;i++)
	{
		cout <<"Case #"<<i<<": ";
		printf("%.15lf\n",work());
	}
	return 0;
}