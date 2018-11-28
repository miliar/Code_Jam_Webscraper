#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long llint;

llint najgori(llint x, int n) {
  if(x == 0) return 1;
  return (1LL<<(n-1)) + najgori((x-1)/2, n-1);
}

llint najbolji(llint x, int n) {
  if(x == 0) return (1LL<<n);
  return najbolji((x-1)/2, n-1);
}
  
int main(void) {
  int t;
  scanf("%d", &t);
  for(int c = 1; c <= t; ++c) {
    int n;
    llint p;
    scanf("%d %lld", &n, &p);

    llint N = (1LL<<n);

    llint lo = 0, hi = N-1;
    while(lo < hi) {
      llint mid = (lo + hi + 1)/2;
      if(najgori(mid, n) <= p) lo = mid; else
        hi = mid-1;
    }

    llint l = 0, h = (1LL<<n)-1;
    while(l < h) {
      llint mid = (l + h + 1)/2;
      if(najbolji(N-1-mid, n) <= p) l = mid; else
        h = mid-1;
    }
    printf("Case #%d: %lld %lld\n", c, lo, l );
  }
  return 0;
}
