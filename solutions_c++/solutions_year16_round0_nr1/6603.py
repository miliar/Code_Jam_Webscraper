#include <cstdio>
#include <cassert>

int main() {
  int nt;
  assert(scanf("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; ++tt) {
    int n;
    assert(scanf("%d", &n) == 1);
    printf("Case #%d: ", tt);
    if (n == 0) {
      printf("INSOMNIA\n");
    } else {
      long long x = n;
      bool a[10] = {false};
      while (true) {
        long long y = x;
        while (y > 0) {
          a[y % 10] = true;
          y /= 10;
        }
        bool ok = true;
        for (int i = 0; i < 10; ++i) {
          if (!a[i]) {
            ok = false;
          }
        }
        if (ok) {
          break;
        }
        x += n;
      }
      printf("%lld\n", x);
    }
  }
  return 0;
}
