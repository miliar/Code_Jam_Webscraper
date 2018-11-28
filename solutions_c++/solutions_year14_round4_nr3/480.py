#include <cstdio>
#include <algorithm>

using namespace std;

char base[505][105];
int tc;
int w,h;

int dir[4][2]=
{
    0,1,
    1,0,
    0,-1,
    -1,0,
};

inline int dfs(int x,int y,int dr)
{
    base[y][x]='#';
    if (y==h)
        return 1;
    for (int i=0; i<4; i++)
    {
        int nx,ny,nd;
        nd=(dr+100+i)%4;
        nx=x+dir[nd][0];
        ny=y+dir[nd][1];
        if (base[ny][nx]=='#' || nx<1 || nx>w || ny<1 || ny>h)
            continue;
        int code=dfs(nx,ny,(nd+99)%4);
        if (code==1)
            return 1;
    }
    return 0;
}

int main()
{
    freopen("D:/in.txt","r",stdin);
    freopen("D:/out.txt","w",stdout);
    scanf("%d",&tc);
    for (int it=1; it<=tc; it++)
    {
        int n;
        scanf("%d%d%d",&w,&h,&n);
        for (int x=1; x<=w; x++)
            for (int y=1; y<=h; y++)
                base[y][x]='.';
        for (int i=1; i<=n; i++)
        {
            int x0,x1,y0,y1;
            scanf("%d%d",&x0,&y0);
            scanf("%d%d",&x1,&y1);
            x0++;
            x1++;
            y0++;
            y1++;
            for (int x=x0; x<=x1; x++)
                for (int y=y0; y<=y1; y++)
                    base[y][x]='#';
        }
        /*
        for (int y=h; y>=1; y--)
        {
            for (int x=1; x<=w; x++)
                printf("%c",base[y][x]);
            printf("\n");
        }
        printf("\n");
        */
        int sol=0;
        for (int pl=1; pl<=w; pl++)
        {
            int dr=0;
            int x=pl;
            int y=1;
            if (base[y][x]=='#')
                continue;
            //printf("RUN %d %d\n",x,y);
            sol+=dfs(x,y,3);
            /*
            for (int y=h; y>=1; y--)
            {
                for (int x=1; x<=w; x++)
                    printf("%c",base[y][x]);
                printf("\n");
            }
            printf("\n");
            */
        }
        printf("Case #%d: %d\n",it,sol);
    }
}
