#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

char brd[64][64];
int vis[64][64][4];
int px[64],py[64],pp[64];
int r,c,n,v;

int getdir(int x)
{
    if((x>=1)&&(x<=c))
    {
        return 2;
    }
    else if((x>=c+1)&&(x<=r+c))
    {
        return 3;
    }
    else if((x>=r+c+1)&&(x<=r+c+c))
    {
       return 0;
    }
    else
    {
        return 1;
    }
}

const int dx[4]={-1,0,1,0};
const int dy[4]={0,1,0,-1};

int DFS(int sx,int sy,int sz,int ex,int ey,int ez)
{
    if((sx==ex)&&(sy==ey)&&(sz==ez))
    {
        return 1;
    }
    if((sx<1)||(sx>r)||(sy<1)||(sy>c)||(vis[sx][sy][sz]==v))
    {
        return 0;
    }
    vis[sx][sy][sz]=v;
    if(brd[sx][sy]=='/')
    {
        return DFS(sx+dx[sz],sy+dy[sz],sz^2,ex,ey,ez)||DFS(sx,sy,sz^3,ex,ey,ez);
    }
    else
    {
        return DFS(sx+dx[sz],sy+dy[sz],sz^2,ex,ey,ez)||DFS(sx,sy,sz^1,ex,ey,ez);
    }
}

int check(int s,int e)
{
    int sx,sy,sz,ex,ey,ez;
    sx=px[s];
    sy=py[s];
    sz=getdir(s);
    ex=px[e];
    ey=py[e];
    ez=getdir(e);
    v++;
    vis[sx][sy][sz]=1;
    return DFS(sx+dx[sz],sy+dy[sz],sz^2,ex,ey,ez);
}

int DFS(int k)
{
    int i;
    if(k==n)
    {
        return 1;
    }
    if(check(pp[k],pp[k+1])==0)
    {
        return 0;
    }
    return DFS(k+2);
}

int DFS(int x,int y)
{
    if(x>r)
    {
        return DFS(0);
    }
    if(y>c)
    {
        return DFS(x+1,1);
    }
    brd[x][y]='/';
    if(DFS(x,y+1)==1)
    {
        return 1;
    }
    brd[x][y]='\\';
    if(DFS(x,y+1)==1)
    {
        return 1;
    }
    return 0;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int p,q,i,j;
    scanf("%d",&q);
    for(p=0;p<q;p++)
    {
        scanf("%d %d",&r,&c);
        n=0;
        for(j=1;j<=c;j++)
        {
            n++;
            px[n]=0;
            py[n]=j;
        }
        for(i=1;i<=r;i++)
        {
            n++;
            px[n]=i;
            py[n]=c+1;
        }
        for(j=c;j>=1;j--)
        {
            n++;
            px[n]=r+1;
            py[n]=j;
        }
        for(i=r;i>=1;i--)
        {
            n++;
            px[n]=i;
            py[n]=0;
        }
        for(i=0;i<n;i++)
        {
            scanf("%d",&pp[i]);
        }
        memset(vis,-1,sizeof(vis));
        v=0;
        printf("Case #%d:\n",p+1);
        if(DFS(1,1)==1)
        {
            for(i=1;i<=r;i++)
            {
                for(j=1;j<=c;j++)
                {
                    printf("%c",brd[i][j]);
                }
                printf("\n");
            }
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
