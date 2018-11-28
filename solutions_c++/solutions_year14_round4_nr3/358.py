#include <iostream>
#include <cstdio>
#include <string.h>
#include <vector>
using namespace std;
#define inf 1000000000
#define MAXN 200100
#define MAXM 800010


int N,M,link1[MAXN],p;

struct edge
{
    int v,nxt;
    int f;
}e[MAXM];

void add(int x,int y,int f,int nf=0)
{
    e[p].v=y;
    e[p].f=f;
    e[p].nxt=link1[x];
    link1[x]=p++;
    e[p].v=x;
    e[p].f=nf;
    e[p].nxt=link1[y];
    link1[y]=p++;
}

int q[MAXN],lv[MAXN];
int S , T;
bool bfs()
{
    memset(lv,-1,sizeof(lv));
    q[0]=S;
    int head=0,tail=1,x,v;
    lv[S]=0;

    while(head<tail)
    {
         x=q[head++];
         if(x==T) return true;
         for(int i=link1[x];i!=-1;i=e[i].nxt)
         {
             v=e[i].v;
             if(lv[v]==-1&&e[i].f>0)
             {
                 lv[v]=lv[x]+1;
                 q[tail++]=v;
             }
         }
    }
    return false;
}

int dfs(int x,int UP)
{
    if(UP==0||x==T) return UP;
    int ret=0,tmp;
    int v;
    for(int i=link1[x];i!=-1;i=e[i].nxt)
    {
        v=e[i].v;
        //cout<<x<<" "<<v<<" "<<e[i].f<<" "<<lv[x]<<" "<<lv[v]<<endl;
        if(lv[v]==lv[x]+1&&e[i].f>0)
        {

            tmp=dfs(v,min(e[i].f,UP-ret));

            ret+=tmp;
            e[i].f-=tmp;
            e[i^1].f+=tmp;
        }
    }
    if(ret==0) lv[x]=-1;
    return ret;
}



bool mp[512][128];
int R,C,B;

int dx[] = {0,1};
int dy[] = {1,0};

bool inrange(int xx,int yy)
{
    return xx>=0&&xx<R&&yy>=0&&yy<C;
}

int ID(int xx,int yy)
{
    return xx*C+yy;
}

int solve()
{
    memset(link1,-1,sizeof(link1));
    p=0;
    S = MAXN - 10;
    T = MAXN - 9;
    for(int i=0;i<R;i++)
    for(int j=0;j<C;j++)
    {
        if(mp[i][j]) continue;
        for(int k=0;k<2;k++)
        {
            int ii = i+dx[k];
            int jj = j+dy[k];
            if(inrange(ii,jj)&&mp[ii][jj]==false)
            {
                add(ID(i,j),ID(ii,jj),1,1);
            }
        }
    }
    //cout<<p<<" p"<<endl;
    while(bfs())
    {
        tmp=dfs(1,inf);
        sum+=tmp;
        //cout<<tmp<<endl;
        if(tmp<eps) break;
    }
    if(sum<2*eps) return true;
    return false;
}

int main()
{
    freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int casT;
    scanf("%d",&casT);
    int lx,rx,ly,ry;
    for(int cas=1;cas<=casT;cas++)
    {
        scanf("%d%d%d",&C,&R,&B);
        memset(mp,0,sizeof(mp));
        for(int i=0;i<B;i++)
        {
            scanf("%d%d%d%d",&ly,&lx,&ry,&rx);
            for(int r=lx;r<=rx;r++)
            for(int c=ly;c<=ry;c++)
            {
                mp[r][c] = true;
            }
        }

        int ans = solve();

        printf("Case #%d: %d\n",cas,ans);

    }
    return 0;
}
