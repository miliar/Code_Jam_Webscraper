#include <cstdio>
#include <algorithm>
using namespace std;

int n;
long long a[1000*1000];
long long s[1000*1000+1];

void Read() {
  long long p, q, r, s;
  scanf("%d%lld%lld%lld%lld", &n,&p,&q,&r,&s);
  for (int i=0; i<n; ++i)
    a[i] = (i * p + q) % r + s;
}
 

int main() {
  int Z;
  scanf("%d", &Z);
  for (int z=1; z<=Z; ++z) {
    Read();
    s[0] = 0;
    for (int i=0;i<n;++i)
      s[i+1]=s[i]+a[i];
    long long sum = s[n];
    long long best = sum;
    int j=0;
    for (int i=0;i<=n;++i) {
      while(j<i && max(s[j],s[i]-s[j]) > max(s[j+1],s[i]-s[j+1]))
        ++j;
      best = min(best, max(sum-s[i], max(s[j], s[i]-s[j])));
    }
    printf("Case #%d: %0.10llf\n", z, (sum - best) / (long double)sum);
  }
}
