#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1)
#define INF 0x7fffffff
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrvec(x,siz) for(int xx=0;x<=siz;xx++)  x[xx].clear();
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int dp[11][11]={0};
int v[11]={0};
int main()
{
	int t,cas=0;
	fop;
	scanf("%d",&t);
	while(t--)
	{
		int e,r,n;
		scanf("%d%d%d",&e,&r,&n);
		for(int i=1;i<=n;i++)
			scanf("%d",v+i);
		clr_1(dp);
		dp[0][e]=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<=e;j++)
			if(dp[i][j]>=0)
			{
				for(int k=0;k<=j;k++)
					dp[i+1][min(j-k+r,e)]=max(dp[i+1][min(j-k+r,e)],dp[i][j]+v[i+1]*k);
			}
		int maxn=0;
		for(int i=0;i<=e;i++)
			maxn=max(maxn,dp[n][i]);
		printf("Case #%d: %d\n",++cas,maxn);
	}
}