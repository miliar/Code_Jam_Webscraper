#pragma comment(linker,"/STACK:102400000,1024000")
#include <iostream>
#include<stdio.h>
using namespace std;
bool d;
int dir,a[200][200],flg[200][200],g[30000],f[30000];
int c[][2]={{0,0},{0,1},{0,-1},{1,0},{-1,0}};
int n,m,tot;
char ch[1000];
int _find(int x)
{
    if (f[x]==x) return x;
    f[x]=_find(f[x]);
    return f[x];
}
void dfs(int x,int y,int z,int w)
{
    int index;
    if (a[x][y]!=0)
    {
        dir=a[x][y];
        flg[x][y]=z;
        w++;
    }
    if (x+c[dir][0]>=1&&x+c[dir][0]<=n&&y+c[dir][1]>=1&&y+c[dir][1]<=m)
    {
        if (flg[x+c[dir][0]][y+c[dir][1]]==0)
            dfs(x+c[dir][0],y+c[dir][1],z,w);
        else
        {
      //      index=_find(flg[x+c[dir][0]][y+c[dir][1]]);
      //      g[index]+=w;
     //       f[z]=index;
            return ;
        }
    }
    else
    {
     //   g[z]=w;
        tot++;
    }
}
int main()
{
    int ii,t1,i,j,tt,t2,t4,t3,k;
    freopen("111.txt","r",stdin);
    freopen("222.txt","w",stdout);
    scanf("%d",&tt);
    for(ii=1;ii<=tt;ii++)
    {
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
        {
            scanf("%s",ch);
            for(j=1;j<=m;j++)
            {
                if (ch[j-1]=='.') a[i][j]=0;
                if (ch[j-1]=='>') a[i][j]=1;
                if (ch[j-1]=='<') a[i][j]=2;
                if (ch[j-1]=='v') a[i][j]=3;
                if (ch[j-1]=='^') a[i][j]=4;
            }
        }
        d=true;
        tot=0;
        t1=0;
        t2=0;
        for(i=1;i<=n;i++)
        {
            t3=0;
            t4=0;
            for(j=1;j<=m;j++)
                if (a[i][j]!=0) {t3++;k=j;}
            if (t3==1)
            {
                for(j=1;j<=n;j++)
                    if (a[j][k]!=0) t4++;
                if (t4==1) d=false;
            }
        }
        if (d==false)
        {
            printf("Case #%d: IMPOSSIBLE\n",ii);
            continue;
        }
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
            {
                ++t2;
                f[t2]=t2;
                flg[i][j]=0;
                g[t2]=0;
            }
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
            {
                if (a[i][j]==0) continue;
                if (flg[i][j]!=0) continue;
                dfs(i,j,++t1,0);
            }
  //      for(i=1;i<=n*m;i++)
  //          if (g[i]==1) tot++;

        printf("Case #%d: %d\n",ii,tot);
    }
    return 0;
}



/*
4 4
>>>>
^^><
....
^>^^

4 4
>>>>
^^>>
....
^>^^

4 4
>>>>
^^>v
....
^>^<

4 4
>>>>
^^>v
..>.
^>^<

4 4
>>>>
^^>v
.>..
^>^<
*/
