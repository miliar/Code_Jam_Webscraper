#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int t;
int n;
double naomi[1001];
double ken[1001];
int deceit,war;
int at;
main()
{
 freopen("D-large.in","r",stdin);
 freopen("D-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d",&n);
  war=0;deceit=0;
  for(int i=1;i<=n;i++)
  {
   scanf("%lf",&naomi[i]);
  } 
   for(int i=1;i<=n;i++)
  {
   scanf("%lf",&ken[i]);
  } 
  sort(&naomi[1],&naomi[n+1]);
  sort(&ken[1],&ken[n+1]);
  /* for(int i=1;i<=n;i++)
  {
   printf("%lf ",naomi[i]);
  } 
   printf("\n");
   for(int i=1;i<=n;i++)
  {
   printf("%lf ",ken[i]);
  } 
  printf("\n");*/
  at=n;
  for(int i=n;i>=1;i--)
  {
   if(naomi[i]>ken[at]){war++;}
   else{at--;}
  }
  at=1;
  for(int i=1;i<=n;i++)
  {
   if(naomi[i]>ken[at]){deceit++;at++;}
  }
  printf("Case #%d: %d %d\n",tests,deceit,war);
 }
 return 0;
}
