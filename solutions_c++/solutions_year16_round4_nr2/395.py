#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <time.h>
using namespace std;
//r<p<s r=0,p=1,s=2
#define eps 1e-10
double p[222];
int n,k;
double sc[222];
double dp[222][222];
double DP()
{
	for(int i=0;i<=k;i++)
	for(int j=0;j<=k;j++)dp[i][j]=0;
	dp[0][0]=1;
	for(int i=0;i<k;i++)
		for(int j=0;j<=i;j++)
		{
			dp[i+1][j]+=dp[i][j]*(1-sc[i+1]);
			dp[i+1][j+1]+=dp[i][j]*sc[i+1];
		}
	return dp[k][k/2];
}
int main()
{
	int T,cas=0;
	clock_t st=clock();
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	
	while(T--)
	{
		scanf("%d%d",&n,&k);
		for(int i=1;i<=n;i++)scanf("%lf",&p[i]);
		sort(p+1,p+1+n);
		int tot=1;
		double ans=0;
		for(int i=0;i<=k;i++)
		{
			tot=1;
			for(int j=1;j<=i;j++)
			{
				sc[tot++]=p[j];
			}
			for(int j=n;j>n-(k-i);j--)
			{
				sc[tot++]=p[j];
			}
			ans=max(ans,DP());
		}
		printf("Case #%d: %.12f\n",++cas,ans);
	}
//	printf("%dms\n",clock()-st);
	
}