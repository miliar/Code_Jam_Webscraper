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
int r,n,m,k;
int canget[200][11]={0};
int can[200][5]={0};
int cannow[5]={0};
int cnt=0;
void dfs(int now,int last)
{
	if(now==0)
	{
		++cnt;
		for(int i=1;i<=n;i++)
		{
			can[cnt][i]=cannow[i];
			//printf("%d ",cannow[i]);
		}
		//puts("");
		return;
	}
	for(int i=last;i<=m;i++)
	{
		cannow[now]=i;
		dfs(now-1,i);
	}
}
int main()
{
	int t,cas=0;
	fop;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d%d",&r,&n,&m,&k);
		dfs(n,2);
		//printf("%d\n",cnt);
		for(int i=1;i<=cnt;i++)
		{
			for(int j=0;j<(1<<n);j++)
			{
				int mul=1;
				int temp=j;
				for(int k=1;k<=n;k++)
				{
					//printf("%d ",can[i][k]);
					if(temp%2)
						mul*=can[i][k];
					temp>>=1;
				}
				//printf("%d\n",mul);
				canget[i][j]=mul;
			}
		}	
		int canres[202];
		printf("Case #%d:\n",++cas);
		while(r--)
		{
			for(int i=1;i<=cnt;i++)
				canres[i]=1;
			for(int i=0;i<k;i++)
			{
				int temp;
				scanf("%d",&temp);
				for(int j=1;j<=cnt;j++)
				if(canres[j])
				{
					int flag=1;
					for(int k=0;k<(1<<n);k++)
						if(canget[j][k]==temp)
						{
							flag=0;
							break;
						}
					//for(int k=0;k<(1<<n);k++) printf("%d ",canget[j][k]);
					//printf("%d\n",flag);
					canres[j]-=flag;
				}
				//puts("");
			}
			int flag=0;
			for(int i=1;i<=cnt;i++)
				if(canres[i]>0)
				{
					for(int j=1;j<=n;j++)
						printf("%d",can[i][j]);
					flag=1;
					puts("");
					break;
				}
			if(flag==0)
			{
				for(int i=1;i<=n;i++)
					printf("2");
				puts("");
			}
		}
	}
}