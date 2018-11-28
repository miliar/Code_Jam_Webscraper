#include<stdio.h>
#include<vector>
#include<list>
#include<algorithm>
using namespace std;

void go(int t) {
  long long a,b,n,p,i;
  scanf("%lld %lld",&n,&p);
  if(p == ((long long)1<<n) ) {
    printf("Case #%d: %lld %lld\n",t,p-1,p-1);
    return;
  }
  p--;
  for(i=1;i<=n;i++) if(! (p & ((long long)1<<(n-i)) ) ) break;
  a = ((long long)1<<i)-2;
  p++;
  for(i=1;i<=n;i++) if((p & ((long long)1<<(n-i)))) break;
  b = ((long long)1<<n) - ((long long)1<<(i));
  printf("Case #%d: %lld %lld\n",t,a,b);
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) go(t);
  return 0;
}
