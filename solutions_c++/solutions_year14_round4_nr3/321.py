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
#define fop   freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
#define E 10000011
#define N 150055
typedef long long LL;
typedef unsigned long long ULL;
typedef double DB;
struct Edge
{
    int en,cap,flow,next;
} edge[E];
int head[N] , tot , now[N];
int source,sink,tot_num;
int pre[N] , dis[N] , gap[N];
struct node
{
     int x,y,z,f,l;
}p[122];
void add(int st,int en,int cap)
{
    edge[tot].en=en;
    edge[tot].cap=cap;
    edge[tot].flow=0;
    edge[tot].next=head[st];
    head[st]=tot++;

    edge[tot].en=st;
    edge[tot].cap=0;
    edge[tot].flow=0;
    edge[tot].next=head[en];
    head[en]=tot++;
}

void augment(int flow)
{
    for(int i=source;i!=sink;i=edge[now[i]].en)
    {
        edge[now[i]].flow+=flow;
        edge[now[i]^1].flow-=flow;
    }
}
int summ=0;
int sap()
{
    memset(dis,0,sizeof(dis));
    memset(gap,0,sizeof(gap));
    memset(pre,-1,sizeof(pre));
    for(int i=0;i<tot_num;i++)
        now[i]=head[i];
    gap[0]=tot_num;
    int point=source,flow=0,min_flow=INF;
    while(dis[source]<tot_num)
    {
        bool fg=false;
        for(int i=now[point];i!=-1;i=edge[i].next)
            if(edge[i].cap-edge[i].flow>0 && dis[point]==dis[edge[i].en]+1)
            {
                min_flow=min(min_flow,edge[i].cap-edge[i].flow);
                now[point]=i;
                pre[edge[i].en]=point;
                point=edge[i].en;
                if(point==sink)
                {
                    flow+=min_flow;
                    augment(min_flow);
                    point=source;
                    min_flow=INF;
                }
                fg=true;
                break;
            }
        if(fg) continue;
        if(--gap[dis[point]]==0) break;
        int Min=tot_num;
        for(int i=head[point];i!=-1;i=edge[i].next)
            if(edge[i].cap-edge[i].flow>0 && Min>dis[edge[i].en])
            {
                Min=dis[edge[i].en];
                now[point]=i;
            }
        gap[dis[point]=Min+1]++;
        if(point!=source) point=pre[point];
    }
    return flow;
}
int n,m;
int mp[1011][1011];
int id[1011][1011];
int dx[4]={-1,1,0,0};
int dy[4]={0,0,1,-1};
void build()
{
    int n,m,b;
    clr(mp);
    clr(id);
    scanf("%d%d%d",&n,&m,&b);
    for(int i=0;i<b;i++)
    {
        int x1,x2,y1,y2;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        for(int j=x1;j<=x2;j++)
            for(int k=y1;k<=y2;k++)
                mp[j][k]=1;
    }
	tot=0;
	tot_num=2;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(mp[i][j]==0)
            {
                id[i][j]=tot_num/2;
                tot_num+=2;
	        }
    sink=tot_num-1;
	source=0;
    clr_1(head);
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        if(mp[i][j]==0)
        {
            if(j==0)
                add(0,id[i][j]*2,1);
            add(id[i][j]*2,id[i][j]*2-1,1);
            for(int k=0;k<4;k++)
            {
                int nx=i+dx[k];
                int ny=j+dy[k];
                if(nx<0||nx>=n||ny<0||ny>=m||mp[nx][ny])
                    continue;
                add(id[i][j]*2-1,id[nx][ny]*2,1);
            }
            if(j==m-1)
                add(id[i][j]*2-1,sink,1);
        }
}
int main()
{
	fop;
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
    	build();
    	printf("Case #%d: %d\n",++cas,sap());
    }
}