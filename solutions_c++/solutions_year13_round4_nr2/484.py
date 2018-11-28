#include <cstdio>

int main () {
  int tc;
  scanf ("%d", &tc);
  for (int tn = 1; tn <= tc; tn++) {
    long long n;
    long long p;
    scanf ("%lld %lld", &n, &p);
    long long q = p, r1 = 0, r2 = 0;
    long long t = n - 1;
    while (q > 1) {
      r1 += (1LL << t);
      --t;
      q >>= 1;
    }
    t = 1;
    --p;
    while (t <= n && (p & (1LL << (n - t)))) {
      r2 += 1LL << t;
      ++t;
    }
    if (r2 >= (1LL << n)) r2 = (1LL << n) - 1;
    printf ("Case #%d: %lld %lld\n", tn, r2, r1);
  }
  return 0;
}
