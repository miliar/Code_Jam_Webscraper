#include <cstdio>
#include <cassert>

bool check(int n, int p) {
  long long d[11];
  for (int b = 2; b <= 10; ++b) {
    long long v = 0;
    for (int i = n - 1; i >= 0; --i) {
      v = v * b + ((p >> i) & 1);
    }
    d[b] = -1;
    for (long long q = 2; q * q <= v; ++q) {
      if (v % q == 0) {
        d[b] = q;
        break;
      }
    }
    if (d[b] == -1) {
      return false;
    }
  }
  for (int i = n - 1; i >= 0; --i) {
    printf("%d", (p >> i) & 1);
  }
  for (int b = 2; b <= 10; ++b) {
    printf(" %lld", d[b]);
  }
  printf("\n");
  return true;
}

int main() {
  int n, left;
  assert(scanf("%d%d", &n, &left) == 2);
  printf("Case #1:\n");
  for (int i = (1 << (n - 1)) + 1; i < (1 << n) && left > 0; i += 2) {
    if (check(n, i)) {
      --left;
    }
  }
  return 0;
}
