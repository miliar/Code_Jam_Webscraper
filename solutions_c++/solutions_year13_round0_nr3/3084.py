#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
const int MaxN = 105;

LL int_sqrt(LL x) {
  LL res = max(1LL, (LL)sqrt(x) - 2);
  while (res * res < x) ++res;
  return res;
}

bool check(LL n) {
  static char buf[20];
  sprintf(buf, "%I64d", n);
  for (int i = 0, j = strlen(buf) - 1; i < j; ++i, --j)
    if (buf[i] != buf[j])
      return false;
  return true;
}

int main() {
  int T;
  LL l, r;
  int ret;

  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);
  
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    scanf("%I64d%I64d", &l, &r);
    ret = 0;
    for (LL i = int_sqrt(l); i * i <= r; ++i) {
      ret += check(i) && check(i * i);
    }
    printf("Case #%d: %d\n", cas, ret);
  }

  return 0;
}

