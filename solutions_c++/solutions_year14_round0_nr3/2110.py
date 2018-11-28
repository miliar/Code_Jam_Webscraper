#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<string>
#include<cctype>
#include<cmath>
using namespace std;
#define LL long long
#define CLR(x,y) memset(x,y,sizeof(x))
template<class T> inline int maximize(T& a,T b){if(a<b){a=b;return 1;}return 0;}
template<class T> inline int minimize(T& a,T b){if(a>b){a=b;return 1;}return 0;}
const int N=111,INF=0x3f3f3f3f;

int R,C,M,G[11][11],dx[8]={0,0,1,1,1,-1,-1,-1},dy[8]={1,-1,1,-1,0,1,-1,0};

int check(int x,int y)
{
    if(1<=x&&x<=R&&1<=y&&y<=C) return 1;
    return 0;
}

int vis[11][11],X,Y;

void DFS(int x,int y)
{
    vis[x][y]=1;
    for(int k=0;k<8;++k)
    {
        int nx=x+dx[k],ny=y+dy[k];
        if(check(nx,ny)&&G[nx][ny]==0&&!vis[nx][ny]) DFS(nx,ny);
    }
}

int connect()
{
    int x,y;
    CLR(vis,0);
    for(int i=1;i<=R;++i)
    {
        for(int j=1;j<=C;++j)
        {
            if(G[i][j]==0)
            {
                x=i;y=j;
            }
        }
    }
    DFS(x,y);
    for(int i=1;i<=R;++i)
        for(int j=1;j<=C;++j)
            if(G[i][j]==0&&vis[i][j]==0) return 0;
    return 1;
}

void pick(int x,int y)
{
    vis[x][y]=1;
    if(G[x][y]==2) return;
    for(int k=0;k<8;++k)
    {
        int nx=x+dx[k],ny=y+dy[k];
        if(check(nx,ny)&&G[nx][ny]!=1&&!vis[nx][ny]) pick(nx,ny);
    }
}

int dfs(int x,int y)
{
    if(x>R)
    {
        if(M!=0) return 0;
        for(int i=1;i<=R;++i)
        {
            for(int j=1;j<=C;++j)
            {
                if(G[i][j]==0)
                {
                    for(int k=0;k<8;++k)
                    {
                        int nx=i+dx[k],ny=j+dy[k];
                        if(check(nx,ny)&&G[nx][ny]==1) G[i][j]=2;
                    }
                }

            }
        }
        for(int i=1;i<=R;++i)
        {
            for(int j=1;j<=C;++j)
            {
                if(G[i][j]==1) continue;
                CLR(vis,0);
                pick(i,j);
                int f=1;
                for(int l=1;l<=R;++l)
                {
                    for(int r=1;r<=C;++r)
                    {
                        if(G[l][r]!=1&&vis[l][r]==0) f=0;
                    }
                }
                if(f)
                {
                    X=i;Y=j;
                    return 1;
                }
            }
        }
        for(int i=1;i<=R;++i)
            for(int j=1;j<=C;++j)
                if(G[i][j]==2) G[i][j]=0;
        return 0;
    }
    int nx=x,ny=y+1;
    if(ny>C) ++nx,ny=1;
    if(dfs(nx,ny)) return 1;
    if(M>0)
    {
        G[x][y]=1;
        --M;
        if(dfs(nx,ny))return 1;
        ++M;
        G[x][y]=0;
    }
    return 0;
}

int isok()
{
    for(int i=1;i<=R;++i)
    {
        for(int j=1;j<=C;++j)
        {
            if(G[i][j]==0)
            {
                for(int k=0;k<8;++k)
                {
                    int nx=i+dx[k],ny=j+dy[k];
                    if(check(nx,ny)&&G[nx][ny]==1)
                    {
                        G[i][j]=2;
                    }
                }
            }
        }
    }
    int flag=1;
    for(int i=1;i<=R;++i)
    {
        for(int j=1;j<=C;++j)
        {
            if(G[i][j]==2)
            {
                int f=1;
                for(int k=0;k<8;++k)
                {
                    int nx=i+dx[k],ny=j+dy[k];
                    if(check(nx,ny)&&G[nx][ny]==0)
                    {
                        f=0;break;
                    }
                }
                if(f) flag=0;
            }
        }
        if(flag==0) break;
    }
    if(flag)
    {
        if(!connect()) flag=0;
    }
    return flag;
}

int solve()
{
    for(LL i=0;i<1LL<<R*C;++i)
    {
        LL t=i;
        int cnt=0;
        while(t) {if(t&1)++cnt;t>>=1;}
        if(cnt!=M) continue;
        int x=1,y=1;
        for(int j=0;j<R*C;++j)
        {
            if(i&(1<<j)) G[x][y]=1;
            else G[x][y]=0;
            ++y;
            if(y>C) ++x,y=1;
        }
        if(isok()) return 1;
    }
    return 0;
}
void print()
{
    G[X][Y]=3;
    for(int i=1;i<=R;++i,printf("\n"))
    {
        for(int j=1;j<=C;++j)
        {
            if(G[i][j]==1) printf("*");
            else if(G[i][j]==3) printf("c");
            else printf(".");
        }
    }
}

int main()
{
    freopen("C-small-attempt5.in","r",stdin);
    freopen("yy.out","w",stdout);
    int T;cin>>T;
    for(int cs=1;cs<=T;++cs)
    {
        cin>>R>>C>>M;
        CLR(G,0);
        printf("Case #%d:\n",cs);
        if(dfs(1,1)) print();
        else printf("Impossible\n");
    }
    return 0;
}
