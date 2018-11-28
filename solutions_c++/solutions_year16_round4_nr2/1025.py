#include <bits/stdc++.h>
/*
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<string>
#include<complex>
*/
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef complex<double> cplx;

#define sqr(x) ((x)*(x))
#define pb push_back
#define X first
#define Y second
#define sit(a) set<a>::iterator
#define mit(a,b) map<a,b>::iterator

const ll mod=1000000007LL;
const int inf=0x3f3f3f3f;
const int maxn=100005,maxm=1005;
const double eps=1e-10;
const double pi=acos(-1.0);

int T;

int n,m;
double p[205];

int x[205];

double re=0;

double dp[25][25];

void dfs(int dep,int i)
{
	if(dep<m&&i>=n) return;
	if(dep==m)
	{
		memset(dp,0,sizeof(dp));dp[0][0]=1;
		for(int j=1;j<=m;j++)
		{
			for(int k=0;k<=j&&k<=m/2;k++)
			{
				dp[j][k]=max(dp[j][k],(k<j?dp[j-1][k]*(1-p[x[j-1]]):0)+(k>0?dp[j-1][k-1]*p[x[j-1]]:0));
			}
		}
		re=max(re,dp[m][m/2]);
		return;
	}
	for(int j=i;j<n;j++)
	{
		x[dep]=j;dfs(dep+1,j+1);
	}
}

double solve()
{
	int i,j;
	sort(p,p+n);re=0;
	dfs(0,0);
	return re;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++)
	{
		printf("Case #%d: ",ca);
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++) scanf("%lf",p+i);
		printf("%.10lf\n",solve());
	}
	return 0;
}

