#include <stdio.h>
#include <stdlib.h>

int t;
int n;
int A[1001];
int ans;
int proc;
int tmp;
main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  proc=0;
  ans=100000;
  scanf("%d",&n);
  for(int i=1;i<=n;i++)
  {
   scanf("%d",&A[i]);
  }
  for(int i=1;i<=1000;i++)
  {
    proc=i;
    for(int j=1;j<=n;j++)
    {
     if(A[j]>i){proc+=(A[j]-1)/i;}
    }
    if(proc<ans){ans=proc;}
  }
  printf("Case #%d: %d\n",tests,ans);
 }
 
 return 0;
}
