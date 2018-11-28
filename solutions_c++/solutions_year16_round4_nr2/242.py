#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
double p[210];
double pp[100010];
int qq;
int n,k;
double ans;
double dp[210][210];
void solve()
{
	for(int i=0;i<=k;i++)
		for(int j=0;j<=k;j++)
			dp[i][j]=0;
	dp[0][0]=1.0;
	for(int i=0;i<k;i++)
		for(int j=0;j<=i && j<=k/2;j++)
		{
			dp[i+1][j+1]+=dp[i][j]*pp[i];
			dp[i+1][j]+=dp[i][j]*(1.0-pp[i]);
		}
//	for(int i=0;i<k;i++)
//		printf("%.4f ",pp[i]);
//	printf("\n");
//	printf("%.6f\n",dp[k][k/2]);
	ans=max(ans,dp[k][k/2]);
}
int main()
{
	freopen("B-large.in","r",stdin);
//	freopen("A.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%d %d",&n,&k);
		for(int i=0;i<n;i++)
			scanf("%lf",&p[i]);
		sort(p,p+n);
		ans=0;
		for(int end=0;end<=k;end++)
		{
			qq=0;
			for(int i=0;i<end;i++)
				pp[qq++]=p[i];
			int at=n-1;
			while(qq < k)
				pp[qq++]=p[at--];
			solve();
		}
		printf("Case #%d: %.12f\n",cc,ans);
	}
	return 0;
}
/*
3
2 2
0.50 0.50
4 2
0.00 0.00 1.00 1.00
3 2
0.75 1.00 0.50

1
3 2
0.04 0.02 0.01

 */
