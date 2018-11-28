#include <cstdio>

long long work1(int n, long long p) {
  long long N = 1LL << n;
  long long a = 0, b = N - 1;
  while (a != b) {
    long long c = (a + b + 1) / 2, c2 = c;
    for (int i = 0; i < n; ++i) {
      if ((1LL << (n - i - 1)) & ~p) {
        // must win
        break;
      } else {
        c2 = (c2 - 1) / 2;
      }
    }
    if (c2 == 0) {
      a = c;
    } else {
      b = c - 1;
    }
  }
  return a;
}

void work() {
  int n;
  long long p;
  scanf("%d%lld", &n, &p);
  --p;
  printf("%lld", work1(n, p));
  long long N = 1LL << n;
  long long a = 0, b = N - 1;
  while (a != b) {
    long long c = (a + b - 1) / 2, c2 = c;
    long long t = 1;
    for (int i = 0; i < n; ++i) {
      if ((1 << (n - i - 1)) & ~p) {
        // C must win best of t
        c2 -= t;
        t *= 2;
      } else {
        // if C win, possible
        if (c2 >= t) {
          break;
        }
      }
    }
    if (c2 < 0) {
      a = c + 1;
    } else {
      b = c;
    }
  }
  printf(" %lld\n", N - a - 1);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    printf("Case #%d: ", i);
    work();
  }
}
