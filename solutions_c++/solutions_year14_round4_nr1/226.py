/*
Author: elfness@UESTC
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
using namespace std;
typedef long long LL;
const int V=10010;
int _,a[V],n,X,dp[V][V];
int dfs(int l,int r)
{
	if(l>=r)return r-l+1;
	if(dp[l][r]!=-1)return dp[l][r];
	dp[l][r]=r-l+1;
	if(a[l]+a[r]<=X)dp[l][r]=min(dp[l][r],dfs(l+1,r-1)+1);
	dp[l][r]=min(dp[l][r],dfs(l+1,r)+1);
	dp[l][r]=min(dp[l][r],dfs(l,r-1)+1);
	return dp[l][r];
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&_);
	for(int ca=1;ca<=_;ca++)
	{
		scanf("%d%d",&n,&X);
		for(int i=0;i<n;i++)
		scanf("%d",&a[i]);
		sort(a,a+n);
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",ca,dfs(0,n-1));
	}
	return 0;
}
