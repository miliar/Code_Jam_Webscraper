#include <cstdio>
#include <algorithm>

using namespace std;

const int auxx[5]={0,-1,0,1,0},auxy[5]={0,0,1,0,-1};
int v[110][110],vaz[110][110],n,m,sol,impos;
char sir[110];

int bun(int x,int y)
{
    if(x<1 || x>n | y<1 || y>m) return 0;
    return 1;
}

void traseu(int x,int y)
{
    int dir=v[x][y];
    vaz[x][y]=1;
    x+=auxx[dir];y+=auxy[dir];
    while(bun(x,y))
    {
        if(v[x][y])
        {
            if(vaz[x][y])
            {
                vaz[x][y]=2;
                return;
            }
            vaz[x][y]=2;
            dir=v[x][y];
        }
        x+=auxx[dir];y+=auxy[dir];
    }
}

void traseu1(int x,int y)
{
    pair<int,int> dir;
    int x1=x,y1=y;
    dir.second=v[x][y];
    vaz[x][y]=3;
    x+=auxx[dir.second];y+=auxy[dir.second];
    while(bun(x,y))
    {
        if(v[x][y])
        {
            if(vaz[x][y]==3) return;
            vaz[x][y]=3;
            dir.first=dir.second;
            dir.second=v[x][y];
            x1=x;y1=y;
        }
        x+=auxx[dir.second];y+=auxy[dir.second];
    }
    if(dir.first==0) vaz[x1][y1]=4;
    else
    {
        sol++;
        v[x1][y1]=dir.first+2;
        if(v[x1][y1]>4) v[x1][y1]-=4;
    }
}

int traseu2(int x,int y,int dir)
{
    x+=auxx[dir];y+=auxy[dir];
    while(bun(x,y))
    {
        if(v[x][y]) return 1;
        x+=auxx[dir];y+=auxy[dir];
    }
    return 0;
}

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        scanf("%d%d",&n,&m);
        sol=impos=0;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++) vaz[i][j]=0;
        for(int i=1;i<=n;i++)
        {
            scanf("\n%s",sir+1);
            for(int j=1;j<=m;j++)
                if(sir[j]=='.') v[i][j]=0;
                else if(sir[j]=='^') v[i][j]=1;
                else if(sir[j]=='>') v[i][j]=2;
                else if(sir[j]=='v') v[i][j]=3;
                else if(sir[j]=='<') v[i][j]=4;
        }
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++) if(!vaz[i][j] && v[i][j]) traseu(i,j);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                if(vaz[i][j]==1) traseu1(i,j);
        for(int i=1;i<=n && !impos;i++)
            for(int j=1;j<=m && !impos;j++)
                if(vaz[i][j]==4)
                {
                    int ok=0;
                    for(int q=1;q<=4;q++) if(traseu2(i,j,q)) {ok=1;break;}
                    if(!ok) impos=1;
                    else sol++;
                }
        if(impos) printf("Case #%d: IMPOSSIBLE\n",t);
        else printf("Case #%d: %d\n",t,sol);

    }
    return 0;
}
