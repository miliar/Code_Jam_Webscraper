//Khagan

#include <algorithm>
#include <stdio.h>
#define  maxn      1000
using    namespace std;

int T,n;
int ar[maxn];

int f(int x)
{
  int sum=0;
  for(int i=0 ; i<n ; i++)
    sum+=(ar[i]-1)/x;
  return sum+x;
}

int main()
{
  freopen("B-large.in","r",stdin);
  freopen("cikti.txt","w",stdout);
  scanf("%d",&T);
  for(int t=1 ; t<=T ; t++)
  {
    scanf("%d",&n);
    for(int i=0 ; i<n ; i++)
      scanf("%d",&ar[i]);
    sort(ar,ar+n);
    int mx=ar[n-1];
    int ans=mx;
    for(int i=1 ; i<mx ; i++)
      ans=min(ans,f(i));
    printf("Case #%d: %d\n",t,ans);
  }
  return 0;
}
