#include <cstdio>
#include <cassert>

char buffer[1111];

int Work() {
  int n;
  assert(scanf("%d %s", &n, buffer) == 2);
  int ret = 0;
  int now = 0;
  for (int i = 0; i <= n; ++i) {
    int t = buffer[i] - '0';
    if (t) {
      if (now < i) {
        ret += i - now;
        now = i;
      }
      now += t;
    }
  }
  return ret;
}

int main() {
  int cases;
  assert(scanf("%d", &cases) == 1);
  for (int i = 1; i <= cases; ++i)
    printf("Case #%d: %d\n", i, Work());
  return 0;
}
