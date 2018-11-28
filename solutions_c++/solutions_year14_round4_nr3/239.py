#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>

#define INT_INF 0x3fffffff
#define LL_INF 0x3fffffffffffffff
#define EPS 1e-12
#define MOD 1000000007
#define PI 3.141592653579798
#define N 100005
#define E 1000000

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef double DB;
map<int,int>I;
struct Edge
{
    int en,cap,flow,next;
} edge[E];
int head[N] , tot , now[N];
int source,sink,tot_num;
int pre[N] , dis[N] , gap[N];

int dx[4]={0,0,1,-1},dy[4]={1,-1,0,0};

void add_edge(int st,int en,int cap)
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

int sap()
{
    memset(dis,0,sizeof(dis));
    memset(gap,0,sizeof(gap));
    memset(pre,-1,sizeof(pre));
    for(int i=0;i<tot_num;i++)
        now[i]=head[i];
    gap[0]=tot_num;
    int point=source,flow=0,min_flow=INT_INF;
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
                    min_flow=INT_INF;
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

void build(int n)
{
    memset(head,-1,sizeof(head));
    tot=0;
    source=0; sink=500; tot_num=n+2;
    int a,b,c;
    for(int i=1;i<=n;i++)
    {
        scanf("%d%d%d",&a,&b,&c);
        for(int j=1;j<=a;j++)
        {
          scanf("%d",&c);
          if(I[c]==0)
          {
            I[c]=I.size();
            add_edge(I[c],sink,1);
          //  add_edge(sink,I[c],1);
          }
          add_edge(i,I[c],1);
     //     add_edge(I[c],i,1);
        }
        add_edge(source,i,c);
     //   add_edge(i,source,c);
    }
}

int vis[110][510];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int w,h,n,d,i,j,x,y,xx,yy,k;
        scanf("%d%d%d",&w,&h,&n);
        memset(vis,0,sizeof(vis));
        for(i=1;i<=n;i++)
        {
            scanf("%d%d%d%d",&x,&y,&xx,&yy);
            for(j=x;j<=xx;j++)
                for(k=y;k<=yy;k++)
                    vis[j][k]=1;
        }
        memset(head,-1,sizeof(head));
        source=2*w*h;
        sink=2*w*h+1;
        tot_num=2*w*h+2;
        tot=0;
        for(i=0;i<w;i++)
        {
            if(vis[i][0]==0)
                add_edge(source,i*h,1);
        }
        for(i=0;i<w;i++)
            for(j=0;j<h;j++)
            {
                if(vis[i][j]==0)
                {
                    add_edge(i*h+j,h*w+i*h+j,1);
                    for(d=0;d<4;d++)
                    {
                        x=i+dx[d];
                        y=j+dy[d];
                        if(x<0||x>=w)
                            continue;
                        if(y<0||y>=h)
                            continue;
                        if(vis[x][y]==1)
                            continue;
                        add_edge(w*h+i*h+j,x*h+y,1);
                    }
                }
            }
        for(i=0;i<w;i++)
        {
            if(vis[i][h-1]==0)
                add_edge(w*h+i*h+h-1,sink,1);
        }
        int ans=sap();
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
