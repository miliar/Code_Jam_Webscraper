#include <stdio.h>
#include <string.h>
#include <algorithm>

long long n, m;

struct node {
  long long o, e, p;

  node(){}
  node(long long _o, long long _e, long long _p): o(_o), e(_e), p(_p){}

  void get() {
    scanf("%lld%lld%lld", &o, &e, &p);
  }

  bool operator < (const node &t) const {
    return o < t.o;
  }
} pn[100010];

int main() {

  int t, kas=0;
  scanf("%d", &t);
  while(t--) {
    scanf("%lld%lld", &n, &m);
    long long sum = 0;
    int cnt = 0;
    for(int i=0;i<m;++i) {
      long long o, e, p;
      scanf("%lld%lld%lld", &o, &e, &p);
      for(int i=0;i<p;++i) {
        pn[cnt++] = node(o, e, 0);
        long long d = e - o;
        sum += (2 * n - d + 1) * d / 2;
        sum %= 1000002013;
      }

    }

    std::sort(pn, pn+cnt);
    long long x = 0;
    for(int i=0;i<cnt;++i) {
      for(int j=i+1;j<cnt;++j)
        if(pn[j].o <= pn[i].e && pn[j].e >= pn[i].e) {
          long long e = pn[j].e;
          pn[j].e = pn[i].e;
          pn[i].e = e;
        }
      long long d = pn[i].e - pn[i].o;
      x += (2 * n - d + 1) * d / 2;
      x %= 1000002013;
    }
    printf("Case #%d: %lld\n", ++kas, sum - x);
  }

  return 0;
}

