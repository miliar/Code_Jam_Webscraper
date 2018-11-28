#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define rep(i,n) for(i=0;i<n;i++)
#define xrep(i,a,b) for(i=(a);i<=(b);i++)
#define SD(x) scanf("%d",&x)
#define SS(x) scanf("%s",x)

const int mx = 100;
int r,c;
int grid[mx+10][mx+10];
int grid2[mx+10][mx+10];
bool mark[102];
bool canDo(int x)
{
    int i,j,k;
    rep(i,r)
    {
        rep(j,c) if( grid[i][j] != x ) break;
        if(j==c) rep(j,c) grid2[i][j] = -1;
    }
    rep(j,c)
    {
        rep(i,r) if( grid[i][j] != x ) break;
        if(i==r) rep(i,r) grid2[i][j] = -1;
    }
    //rep(i,r) {rep(j,c) printf("%d ",grid2[i][j]);puts("");}
    rep(i,r) rep(j,c) if(grid2[i][j]!=-1) return false;
    return true;

}
bool check()
{
    int i,j;
    rep(i,r)rep(j,c) if(mark[grid[i][j]] && grid2[i][j] != -1) return false;
    return true;
}
int main(void)
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-out.txt","w",stdout);
    int i,j,k,t,kase=0;
    SD(t);
    while(t--)
    {
        SD(r) , SD(c);
        memset(mark,0,sizeof(mark));
        memset(grid2,0,sizeof(grid2));
        rep(i,r) rep(j,c) SD(grid[i][j]) , mark[grid[i][j]] = true;
        for(i=100;i>=1;i--) if(mark[i]) break;
        mark[i] = false;
        xrep(i,1,100) if(mark[i]) if(!canDo(i)) break;

        printf("Case #%d: %s\n",++kase, check() ? "YES":"NO");
    }
    return 0;
}
