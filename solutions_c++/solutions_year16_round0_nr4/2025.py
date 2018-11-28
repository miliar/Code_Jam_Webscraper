#include <cstdio>
#include <cstring>

typedef long long LL;

int main() {
  int cas;
  scanf("%d", &cas);
  for (int t = 1; t <= cas; ++t) {
    printf("Case #%d:", t);
    int k, c, s;
    scanf("%d%d%d", &k, &c, &s);
    int m = k / c;
    if (k % c > 0) ++m;
    if (m > s) puts(" IMPOSSIBLE");
    else {
      for (int i = 0; i < k; i += c) {
        LL p = 0;
        for (int j = 0; j < c; ++j) {
          int h = i + j;
          if (h >= k) h = 0;
          p = (p * k) + h;
        }
        printf(" %lld", p + 1);
      }
      puts("");
    }
  }
  return 0;
}