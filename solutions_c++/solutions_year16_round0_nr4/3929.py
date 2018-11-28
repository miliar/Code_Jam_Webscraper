#include <cstdio>
#include <cassert>

int main() {
  int nt;
  assert(scanf("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; ++tt) {
    printf("Case #%d:", tt);
    int k, c, s;
    assert(scanf("%d%d%d", &k, &c, &s) == 3);
    for (int i = 0; i < k; ++i) {
      long long p = i;
      for (int j = 1; j < c; ++j) {
        p = p * k + i;
      }
      printf(" %lld", p + 1);
    }
    printf("\n");
  }
  return 0;
}
