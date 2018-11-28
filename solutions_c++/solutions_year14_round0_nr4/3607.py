#include<cstdio>
#include<algorithm>

using namespace std;

int t,n,l;
double N[1005],K[1005];

void solve1()
{
  int curr=0,count=0;
  for(int i=0;i<n;i++){
    if(N[i]<K[curr])
      count++;
    else
      curr++;
  }
  printf("Case #%d: %d ",l,n-count);
}

void solve2()
{
  int i=0,j=0,count=0;
  while(i<n&&j<n){
    if(N[i]<K[j]){
      i++;j++;
    }
    else {
      j++;
      count++;
    }
  }
  printf("%d\n",count);
}

int main()
{
  scanf("%d",&t);
  for(l = 1;l<=t;l++){
    scanf("%d",&n);
    for(int i=0;i<n;i++)
      scanf("%lf",&N[i]);
    for(int i=0;i<n;i++)
      scanf("%lf",&K[i]);
    sort(N,N+n);
    sort(K,K+n);
    solve1();
    solve2();
  }
}
