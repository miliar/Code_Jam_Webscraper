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
pair<char,int> P[100111];
map<int,int>mp;
int dp[16][1<<16];
int main()
{
	fop;
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		mp.clear();
		int N;
		int cnt=0;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		{
			char s[3]={0};
			int p;
			scanf("%s%d",s,&p);
			P[i]=make_pair(s[0],p);
			if(p!=0&&mp[p]==0)
				mp[p]=mp.size();
			if(P[i].second!=0)
				P[i].second=mp[p];
			// printf("%c %d\n",P[i].first,P[i].second);
		}
		cnt=15;
		clr(dp);
		clr_1(dp[0]);
		for(int i=0;i<N;i++)
			for(int j=0;j<(1<<cnt);j++)
				if(dp[i][j])
				{
					if(P[i].second==0)
					{
						for(int k=0;k<cnt;k++)
							if(P[i].first=='E'&&(j&(1<<k))==0)
								dp[i+1][j|(1<<k)]=1;
							else if(P[i].first=='L'&&(j&(1<<k)))
								dp[i+1][j^(1<<k)]=1;
					}
					else
					{
						if(P[i].first=='E'&&(j&(1<<P[i].second-1))==0)
							dp[i+1][j|(1<<P[i].second-1)]=1;
						if(P[i].first=='L'&&(j&(1<<P[i].second-1)))
							dp[i+1][j^(1<<P[i].second-1)]=1;

					}
				}
		int minn=0x3f3f3f3f;
		for(int i=0;i<(1<<cnt);i++)
			if(dp[N][i])
				minn=min(minn,__builtin_popcount(i));
		printf("Case #%d: ",++cas);
		if(minn==0x3f3f3f3f)
			puts("CRIME TIME");
		else printf("%d\n",minn);
	}
}