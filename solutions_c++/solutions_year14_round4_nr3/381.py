#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <queue>

#define mp make_pair
#define pb push_back

using namespace std;

typedef long long big;
const int inf=0x3f3f3f3f;
const int N=140020,M=N*20;
int head[N],nxt[M],v[M],c[M],t=1;
int dis[N],q[N];
int g[1020][1020];
int S,T;
int W,H,B;
void add(int x,int y,int z)
{
	nxt[++t]=head[x];v[t]=y;c[t]=z;head[x]=t;
	nxt[++t]=head[y];v[t]=x;c[t]=0;head[y]=t;
}
bool bfs()
{
	int h,tail,s,i;
	memset(dis,-1,sizeof(dis));
	dis[S]=0;
	q[h=tail=1]=S;
	while(h<=tail)
	{
		s=q[h++];
		for(i=head[s];i;i=nxt[i])
			if(c[i]&&dis[v[i]]==-1)
			{
				dis[v[i]]=dis[s]+1;
				if(v[i]==T)return true;
				q[++tail]=v[i];
			}
	}
	return false;
}
int aug(int x,int sum)
{
	if(x==T)return sum;
	int os=sum,a,i;
	for(i=head[x];i&&sum;i=nxt[i])
	if(dis[v[i]]==dis[x]+1&&c[i])
	{
		a=aug(v[i],min(sum,c[i]));
		sum-=a;
		c[i]-=a;
		c[i^1]+=a;
	}
	if(os==sum)dis[x]=-1;
	return os-sum;
}
int ID[522][522][2];
int id(int x,int y,int z)
{
	return ID[x][y][z];
	return (x-1)*H+y+z*W*H;
}
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
int maxflow()
{
	int res=0;
	while(bfs())
		res+=aug(S,inf);
	return res;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int i,cas,cass,j,k,mx,ans=inf,x1,y1,x2,y2,x,y;
	scanf("%d",&cas);
	for(cass=1;cass<=cas;cass++)
	{
		scanf("%d%d%d",&W,&H,&B);
		memset(head,0,sizeof(head));
		memset(g,0,sizeof(g));
		t=1;
		S=0;T=0;
		for(i=1;i<=W;i++)
			for(j=1;j<=H;j++)
				ID[i][j][0]=++T,ID[i][j][1]=++T;
		T++;
		for(i=1;i<=W;i++)
			add(S,id(i,1,0),1);
		for(i=1;i<=W;i++)
			add(id(i,H,1),T,1);
		for(i=1;i<=B;i++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			x1++;x2++;y1++;y2++;
			for(x=x1;x<=x2;x++)
				for(y=y1;y<=y2;y++)
					g[x][y]=1;
		}
		for(i=1;i<=W;i++)
			for(j=1;j<=H;j++)
				if(!g[i][j])
					add(id(i,j,0),id(i,j,1),1);
		for(x=1;x<=W;x++)
			for(y=1;y<=H;y++)
			{
				for(k=0;k<4;k++)
				{
					int xx=x+dx[k];
					int yy=y+dy[k];
					if(xx>=1&&xx<=W&&yy>=1&&yy<=H&&!g[x][y]&&!g[xx][yy])
						add(id(x,y,1),id(xx,yy,0),inf);
				}
			}
		printf("Case #%d: ",cass);
		printf("%d\n",maxflow());
	}
}
