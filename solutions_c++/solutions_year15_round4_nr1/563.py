#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
char s[105][105];
int aa;
char dir[10]=".^>v<";
int dire[10][2]={{0,0},{-1,0},{0,1},{1,0},{0,-1}};
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int T,ca=0,n,m;
  scanf("%d",&T);
  while(T--)
  {
    aa=0;
    scanf("%d%d",&n,&m);
    for (int i=0;i<n;i++)
      scanf("%s",s[i]);
    for (int i=1;i<=n;i++)
      for (int j=1;j<=m;j++){
        int idd;
        for (int k=0;k<=4;k++)
          if (s[i-1][j-1]==dir[k]) idd=k;
        if (!idd) continue;
        int x=i,y=j;
        int flag=1;
        while(x>0&&x<=n&&y>0&&y<=m)
        {
          if ((x-i)||(y-j))
          if(s[x-1][y-1]!='.') {flag=0;break;}
          x+=dire[idd][0];
          y+=dire[idd][1];
        }
        aa+=flag;
        if (flag){
          int f=1;
          for (int k=1;k<=4;k++){
          int x=i,y=j;
          while(x>0&&x<=n&&y>0&&y<=m)
          {
            if ((x-i)||(y-j))
            if(s[x-1][y-1]!='.') {f=0;break;}
            x+=dire[k][0];
            y+=dire[k][1];
          }
          }
          if (f) aa=100001;
        }
      }
    printf("Case #%d: ",++ca);
    if (aa<10000) 
    printf("%d\n", aa);
    else puts("IMPOSSIBLE");

  }
}