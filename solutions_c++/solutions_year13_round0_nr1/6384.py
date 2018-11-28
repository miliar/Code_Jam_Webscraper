#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define rep(i,n) for(i=0;i<n;i++)
#define xrep(i,a,b) for(i=(a);i<=(b);i++)
#define SD(x) scanf("%d",&x)
#define SS(x) scanf("%s",x)
char grid[6][6];
char grid2[6][6];
int x[] = {-1,1,-1,1,-1,1,0,0};
int y[] = {0,0,1,1,-1,-1,1,-1};
inline bool valid(int r,int c)
{
    if(r<0 || r>=4) return false;
    if(c<0 || c>=4) return false;
    return true;
}
bool incomplete(void)
{
    int i,j;
    rep(i,4) rep(j,4) if(grid[i][j]=='.') return true;
    return false;
}
bool winX(void)
{
    int i,j,k,I,J,dir;
    rep(i,4)rep(j,4)
        grid2[i][j] = grid[i][j] == 'T' ? 'X' : grid[i][j] ;
    rep(I,4) rep(J,4)
    {
        if(grid2[I][J]!='X') continue;
        rep(dir,8)
        {
            int x_ = I,y_ = J;
            rep(i,3)
                if(valid(x_+x[dir] , y_+y[dir]) && grid2[x_+x[dir]][y_+y[dir]] == 'X') x_+=x[dir] , y_+=y[dir];
                else break;
            if(i==3) return true;
        }
    }
    return false;
}
bool winO(void)
{
    int i,j,k,I,J,dir;
    rep(i,4)rep(j,4)
        grid2[i][j] = grid[i][j] == 'T' ? 'O' : grid[i][j] ;
    rep(I,4) rep(J,4)
    {
        if(grid2[I][J]!='O') continue;
        rep(dir,8)
        {
            int x_ = I,y_ = J;
            rep(i,3)
                if(valid(x_+x[dir] , y_+y[dir]) && grid2[x_+x[dir]][y_+y[dir]] == 'O') x_+=x[dir] , y_+=y[dir];
                else break;
            if(i==3) return true;
        }
    }
    return false;
}
int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("A-largeout.txt","w",stdout);
    int i,j,k;int t,kase=0;
    SD(t);
    while(t--)
    {
        rep(i,4) SS(grid[i]);
        //rep(i,4) puts(grid[i]);
        //puts("");
        printf("Case #%d: ",++kase);
        if(winX()) printf("X won\n");
        else if(winO()) printf("O won\n");
        else if(incomplete()) printf("Game has not completed\n");
        else printf("Draw\n");
        //SS(grid[0]);
    }

    return 0;
}
