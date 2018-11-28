#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int T,n,m;
int in[15][15];
int x[30],yes=0;
int rec(int h)
{
  if(yes==1)return 0;
  if(h==n+m+1)
   {
     int i,j;
     for(i=1;i<=n;i++)
      {
        for(j=1;j<=m;j++)
         {
           int k=x[j];
           if(k>x[m+i])k=x[m+i];
           if(k!=in[i][j])return 0;
         }
      }
      yes=1;
      return 1;
   }
  x[h]=1;
  rec(h+1);
  x[h]=2;
  rec(h+1);
}
int main()
{
freopen("B-small-attempt1.in","r",stdin);
freopen("B-small-attempt1.out","w",stdout);
    int i,j,k;
    int p,q,r;
    int t,tt,ttt;
    scanf("%d",&T);
for(int ii=1;ii<=T;ii++)
{
  scanf("%d %d",&n,&m);
  for(i=1;i<=n;i++)
   {
     for(j=1;j<=m;j++)
      {
        scanf("%d",&in[i][j]);
      }
   }
  //printf(">> %d\n",ii);
  yes=0;
  rec(1);
  if(yes==1)printf("Case #%d: YES",ii);
  else printf("Case #%d: NO",ii);
  if(ii<=T-1)printf("\n");
}
    
    scanf(" ");
    return 0;
}
