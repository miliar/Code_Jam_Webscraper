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
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int H[155];
int G[155];
int res=0;
int P[2],N;
int dp[111][1111];
void dfs(int p,int sum)
{
	int ss=0;
	for(int i=0;i<N;i++)
		if(H[i]>0)
		{
			ss+=G[i];
		}
	if(ss+sum<=res)
		return;
	int flag=0;
	for(int i=0;i<N;i++)
	if(H[i]>0)
	{
		flag=1;
		H[i]-=P[p];
		if(H[i]<=0&&p==0)
		{
			dfs(1-p,sum+G[i]);
			H[i]+=P[p];
		}
		else if(H[i]>0&&p==0)
		{
			dfs(1-p,sum);
			H[i]+=P[p];
		}
		else if(p==1)
		{
			dfs(1-p,sum);
			H[i]+=P[p];
			break;
		}
	}
	if(flag==0)
	{
		res=max(res,sum);
		return;
	}
	if(p==0)
		dfs(1-p,sum);
	return ;
}
int main()
{
	fop;
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		res=0;
		scanf("%d%d%d",&P[0],&P[1],&N);
		int sp=0;
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",&H[i],&G[i]);
			sp+=G[i];
		}
		printf("Case #%d: ",++cas);
		clr_1(dp);
		dp[0][1]=0;
		for(int i=0;i<N;i++)
			for(int j=0;j<=1000;j++)
				if(dp[i][j]!=-1)
				{
					// printf("%d %d %d\n",i,j,dp[i][j]);
					int tac=H[i]/P[1];
					int rst=H[i]%P[1];
					if(rst==0)
					{
						tac--;
						rst=P[1];
					}
					dp[i+1][j+(int)ceil(H[i]/(P[1]+0.0))]=max(dp[i+1][j+(int)ceil(H[i]/(P[1]+0.0))],dp[i][j]);
					for(int l=0;l<=tac;l++)
					{
						int need=ceil(rst/(P[0]+0.0));
						if(need<=tac+j)
						{
							dp[i+1][j+tac-need]=max(dp[i+1][j+tac-need],dp[i][j]+G[i]);
						}
						rst+=P[1];
					}
				}
		int res=0;
		for(int i=0;i<=1000;i++)
			res=max(res,dp[N][i]);
		printf("%d\n",res);
	}
}