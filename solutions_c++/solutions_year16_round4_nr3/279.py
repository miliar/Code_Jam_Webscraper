#include <vector>
#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string.h>
#include <set>


using namespace std;

const int N=205;


#define POS(i,j) ((i)*m+(j))

int n,m;
int a[N];
int mp[N];

pair<int,int> g[22];

int b[22][22];


int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};


vector<int> V[111];

void add(int u,int v)
{
    V[u].push_back(v);
}

int visit[N];

int get(int x)
{
    if(x<=m)
    {
        int xx=0,yy=x-1;
        return POS(xx,yy)*2;
    }
    else if(x<=n+m)
    {
        x-=m;
        int xx=x-1,yy=m-1;
        if(b[xx][yy]==0) return POS(xx,yy)*2+1;
        else             return POS(xx,yy)*2;
    }
    else if(x<=m+n+m)
    {
        x-=n+m;
        int xx=n-1,yy=m-1-(x-1);
        return POS(xx,yy)*2+1;
    }
    else
    {
        x-=m+n+m;
        int xx=n-1-(x-1),yy=0;
        if(b[xx][yy]==0) return POS(xx,yy)*2;
        else             return POS(xx,yy)*2+1;
    }
}

int dfs(int u,int T)
{
    if(u==T) return 1;
    visit[u]=1;
    for(int i=0;i<V[u].size();i++)
    {
        int v=V[u][i];
        if(!visit[v]&&dfs(v,T)) return 1;
    }
    return 0;
}

int check()
{
    int S=n*m*2;
    for(int i=0;i<S;i++) V[i].clear();
    for(int i=0;i<n;i++) for(int j=0;j<m;j++)
    {
        int u1=POS(i,j)*2;
        int u2=u1+1;

        for(int k=0;k<4;k++)
        {
            int ii=i+dx[k];
            int jj=j+dy[k];
            if(ii>=0&&ii<n&&jj>=0&&jj<m)
            {
                int v1=POS(ii,jj)*2;
                int v2=v1+1;
                if(b[i][j]==0)
                {
                    if(k==0)
                    {
                        if(b[ii][jj]==0) add(u2,v1);
                        else add(u2,v2);
                    }
                    else if(k==1)
                    {
                        if(b[ii][jj]==0) add(u1,v2);
                        else add(u1,v1);
                    }
                    else if(k==2)
                    {
                        add(u2,v1);
                    }
                    else
                    {
                        add(u1,v2);
                    }
                }
                else
                {
                    if(k==0)
                    {
                        if(b[ii][jj]==0) add(u1,v1);
                        else add(u1,v2);
                    }
                    else if(k==1)
                    {
                        if(b[ii][jj]==0) add(u2,v2);
                        else add(u2,v1);
                    }
                    else if(k==2)
                    {
                        add(u2,v1);
                    }
                    else
                    {
                        add(u1,v2);
                    }
                }
            }
        }
    }

    memset(visit,0,sizeof(visit));
    for(int i=1;i<=2*(n+m);i++) if(mp[i]>i)
    {
        int u=i;
        int v=mp[i];
        int x=get(u);
        int y=get(v);
        if(!dfs(x,y)) return 0;
    }
    return 1;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("ans","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        printf("Case #%d:\n",tt);
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n+m;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            mp[x]=y;
            mp[y]=x;
        }
        for(int i=0,id=0;i<n;i++) for(int j=0;j<m;j++)
        {
            g[id++]=make_pair(i,j);
        }
        int ok=0;
        for(int i=0;i<(1<<(n*m));i++)
        {
           // i=6;
            for(int j=0;j<(n*m);j++)
            {
                if(i&(1<<j)) b[g[j].first][g[j].second]=1;
                else b[g[j].first][g[j].second]=0;
            }
            if(check())
            {
                ok=1;
                break;
            }
        }
        if(!ok)
        {
            puts("IMPOSSIBLE");
            continue;
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(b[i][j]) putchar('\\');
                else putchar('/');
            }
            puts("");
        }
    }
}

