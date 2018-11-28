#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long LL;

LL A, n;
LL a[5000];

LL g(LL x, LL y) {
  for (LL i = 1; i < 13; ++i) {
    LL tmp = x + ((1ll << i) - 1) * (x - 1);
    if (tmp > y) return i;
  }
}


LL f() {
  if (A == 1) return n;
  LL cnt = 0;
  for (LL i = 0; i < n; ++i) {
    if (A > a[i]) {
      A += a[i];
    } else {
      LL tmp = g(A, a[i]);
      //printf("%lld\n", tmp);
      if (tmp >= n - i) {
        return cnt + n - i;
      }
      cnt = cnt + tmp;
      A += ((1ll << tmp) - 1) * (A - 1) + a[i];
    }
  }
  return cnt;
}

int main() {
  int cas = 0;
  int T; scanf("%d", &T);
  while (T--) {
    scanf("%lld%lld", &A, &n);
    for (LL i = 0; i < n; ++i) {
      scanf("%lld", &a[i]);
    }
    sort(a, a + n);
    printf("Case #%d: ", ++cas);
    printf("%lld\n", f());
  }
  return 0;
}
