#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;
char A[1001][101];
int pre[1001][101];
int len[101];
int perm[1001];
int buc[1001];
int num[1001];
int cntserv;
int serv,n,t;
int maxs;
int ans;
int cnt;
int sc;
bool ext;
int nc;
int cnttrie;
int lasts;
void pri()
{
 for(int i=1;i<=n;i++)
 {
  printf("%d ",perm[i]);
 }
 printf(": %d\n",maxs);
}
void calc()
{
 cnttrie=serv;
 for(int i=1;i<=serv;i++)
 {
 cntserv=0;
  for(int j=1;j<=n;j++)
  {
   if(perm[j]==i)
   {
    cntserv++;
    num[cntserv]=j;
   }
  }
  for(int j=1;j<=10;j++)
  {
   nc=0;
   for(int k=1;k<=cntserv;k++)
   {
   if(pre[num[k]][j]!=(-1))
   {
    nc++;
    buc[nc]=pre[num[k]][j];
   }
   }
   if(nc>0)
   {
   sort(&buc[1],&buc[nc+1]);
   lasts=(-1);
   for(int l=1;l<=nc;l++)
   {
    if(lasts!=buc[l]){cnttrie++;lasts=buc[l];}
   }
   }
  }
 }
 if(cnttrie>maxs)
 {
 maxs=cnttrie;cnt=1;
 //pri();
 }
 else if(cnttrie==maxs)
 {
 cnt++;
 cnt=cnt%1000000007;
 //pri();
 }
}
bool chk()
{
 if(n>1)
 {
  for(int i=1;i<=serv;i++)
  {
   for(int j=1;j<=n;j++)
   {
    if(perm[j]==i){break;}
    else if(j==n){return false;}
   }
  }
 }
 return true;
}
main()
{
 freopen("D-small-attempt1.in","r",stdin);
 freopen("D-small-attempt1.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d%d",&n,&serv);
  for(int i=1;i<=n;i++)
  {
   scanf("%s",A[i]);
   len[i]=strlen(A[i]);
   for(int j=0;j<len[i];j++)
   {
    sc=A[i][j]-'A';
    pre[i][j+1]=(pre[i][j]*26)+sc;
   }
   for(int j=len[i]+1;j<=10;j++)
   {
    pre[i][j]=(-1);
   }
  }
  maxs=0;
  cnt=0;
  for(int i=1;i<=n;i++)
  {
   perm[i]=1;
  }
  ext=true;
  while(ext)
  {
   if(chk()||serv==1)
   {
   calc();
   }
   for(int i=n;i>=1;i--)
   {
    if(perm[i]!=serv)
    {
     perm[i]++;
     for(int j=i+1;j<=n;j++)
     {
      perm[j]=1;
     }
     break;
    }
    else if(i==1){ext=false;}
   }
  }
  printf("Case #%d: %d %d\n",tests,maxs,cnt);
 }
 return 0;
}
