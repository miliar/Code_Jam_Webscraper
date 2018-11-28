//shjj-mine

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int tx[8]={-1,-1,-1,0,0,1,1,1};
const int ty[8]={-1,0,1,-1,1,-1,0,1};

int qx[30000],qy[30000];
int a[300][300],n,m,nn;
bool vis[300][300],g[300][300];

bool C(int x,int y)
{
memset(vis,0,sizeof(vis));
qx[1]=x,qy[1]=y;vis[x][y]=1;
for (int l=0,r=1;l<r;)
  {
  int x=qx[++l],y=qy[l];
  if (a[x][y]) continue;
  for (int i=0;i<8;i++)
    {
	int x3=x+tx[i],y3=y+ty[i];
	if (x3<1||x3>n||y3<1||y3>m) continue;
	if (g[x3][y3]) continue;
	if (vis[x3][y3]) continue;
	vis[x3][y3]=1;
	qx[++r]=x3,qy[r]=y3;
	}
  }
for (int i=1;i<=n;i++)
  for (int j=1;j<=m;j++)
    if (!g[i][j]&&!vis[i][j]) return 0;
return 1;
}

bool check()
{
for (int i=1;i<=n;i++)
  for (int j=1;j<=m;j++)
    if (!g[i][j]) a[i][j]=g[i-1][j-1]+g[i-1][j]+g[i-1][j+1]+g[i][j-1]+g[i][j+1]+g[i+1][j-1]+g[i+1][j]+g[i+1][j+1];
	  else a[i][j]=0;
for (int i=1;i<=n;i++)
  for (int j=1;j<=m;j++)
    if (!g[i][j]&&C(i,j))
	  {
	  for (int ii=1;ii<=n;ii++)
	    {
	    for (int jj=1;jj<=m;jj++)
		  if (g[ii][jj]) printf("*");
		    else if (ii==i&&jj==j) printf("c");
			       else printf(".");
		puts("");
		}
	  return 1;
	  }
return 0;
}

bool dfs(int x,int y,int _s)
{
if (_s>nn) return 0;
if (y>m) x++,y=1;
if (x>n)
  {
  if (_s!=nn) return 0;
  return check();
  }
g[x][y]=1;
if (dfs(x,y+1,_s+1)) return 1;
g[x][y]=0;
if (dfs(x,y+1,_s)) return 1;
return 0;
}

int main()
{
//freopen("mine.in","r",stdin);
//freopen("mine.out","w",stdout);
int Test,tt=0;scanf("%d",&Test);
for (;Test--;)
  {
  scanf("%d%d%d",&n,&m,&nn);
  printf("Case #%d:\n",++tt);
  memset(g,0,sizeof(g));
  if (!dfs(1,1,0)) puts("Impossible");
  }
}