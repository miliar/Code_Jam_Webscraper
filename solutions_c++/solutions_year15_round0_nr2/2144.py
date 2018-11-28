#include <cstdio>
#include <cassert>

int p[1111];

int Work() {
  int n;
  assert(scanf("%d", &n) == 1);
  int p_max = 0;
  for (int i = 0; i < n; ++i) {
    assert(scanf("%d", p + i) == 1);
    if (p_max < p[i]) p_max = p[i];
  }
  int ret = p_max;
  for (int h = 1; h < p_max; ++h) {
    int now = h;
    for (int i = 0; i < n; ++i)
      now += (p[i] - 1) / h;
    if (ret > now) ret = now;
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
