#include <cstdio>
//#define __STDC_FORMAT_MACROS
#include <cstdint>
#include <vector>
#include <algorithm>

using namespace std;

uint64_t f(uint64_t n) {
  int d[10] = {0};
  int c=0;
  uint64_t xn = n;
  while (true) {
    uint64_t x = xn;
    while (x) {
      uint64_t r = x%10;
      x /= 10;
      if (!d[r]) {
        c++; d[r] = 1;
      }
    }
    if (c==10) return xn;
    xn += n;
  }
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i=0; i<n; ++i) {
    int m; scanf("%d", &m);
    printf("Case #%d: ", i+1);
    if (!m) printf("INSOMNIA\n");
    else printf("%llu\n", f(m));
  }
}
