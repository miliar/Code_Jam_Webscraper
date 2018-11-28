#include<stdio.h>
int t,c,r,m;
char map[100][100];
int mapc[100][100];
bool vis[100][100];
int dx[8]={0,0,-1,-1,-1,1,1,1};
int dy[8]={1,-1,0,1,-1,0,1,-1};
bool inmap(int x,int y)
{
     return x>=0&&x<r&&y>=0&&y<c;
}
int dfs2(int x,int y)
{
     if(vis[x][y])return 0;
     vis[x][y]=true;
     int re=1;
     for(int i=0;i<8;i++)
     if(inmap(dx[i]+x,dy[i]+y))
     if(mapc[dx[i]+x][dy[i]+y]) return 1;
     for(int i=0;i<8;i++)
     if(inmap(dx[i]+x,dy[i]+y))
     re+=dfs2(dx[i]+x,dy[i]+y);
     return re;
}
bool dfs(int v,int L)
{
     if(!v)
     {
      for(int i=0;i<r;i++)
      for(int j=0;j<c;j++)
      if(!mapc[i][j])
      {
       for(int x=0;x<r;x++)
       for(int y=0;y<c;y++)
       vis[x][y]=false;
       if(dfs2(i,j)==r*c-m)
       {
        for(int x=0;x<r;x++)
        for(int y=0;y<c;y++)
        if(mapc[x][y]) map[x][y]='*';
        else map[x][y]='.';
        map[i][j]='c';
        return true;
       }
      }
      return false;
     }
     for(int i=L+1;i<=r*c-v;i++)
     {
      mapc[i/c][i%c]=1;
      if(dfs(v-1,i))return true;
      mapc[i/c][i%c]=0;
     }
     return false;
}
int main()
{
    //freopen("ios.in","r",stdin);
    //freopen("ios.out","w",stdout);
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
     for(int i=0;i<100;i++)
     for(int j=0;j<100;j++)
      mapc[i][j]=0;
     scanf("%d%d%d",&r,&c,&m);
     printf("Case #%d:\n",ca);
     if(dfs(m,-1))
     for(int i=0;i<r;i++)
     {
      for(int j=0;j<c;j++)
      printf("%c",map[i][j]);
      printf("\n");
     }
     else printf("Impossible\n");
    }
}
