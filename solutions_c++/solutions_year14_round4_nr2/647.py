#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

//int dp[1001][2];
int t;
int n;
struct node{
int ind;
int val;
bool operator < (const node & o) const{return val<o.val;}
}A[1001];
int lefts[1001];
int rights[1001]; 
int ans;
main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d",&n);
  for(int i=1;i<=n;i++)
  {
   scanf("%d",&A[i].val);
   A[i].ind=i;
  }
  sort(&A[1],&A[n+1]);
  for(int i=1;i<=n;i++)
  {
   lefts[i]=0;
   rights[i]=0;
  }
  ans=0;
  for(int i=1;i<=n;i++)
  {
   if((A[i].ind-1-lefts[A[i].ind])<(n-A[i].ind-rights[A[i].ind])){ans=ans+(A[i].ind-1-lefts[A[i].ind]);}
   else{ans=ans+(n-A[i].ind-rights[A[i].ind]);}
  // printf("%d = l %d r %d\n",A[i].val,(A[i].ind-1-lefts[A[i].ind]),(n-A[i].ind-rights[A[i].ind]));
   for(int j=1;j<A[i].ind;j++)
   {
    rights[j]++;
   }
   for(int j=A[i].ind+1;j<=n;j++)
   {
    lefts[j]++;
   }
 //  printf("%d : %d\n",i,ans);
  }
  printf("Case #%d: %d\n",tests,ans);
 }
 return 0;
}
