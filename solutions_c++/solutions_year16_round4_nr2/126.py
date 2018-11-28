#include <cstdio>
#include <cstring>
#include <algorithm>

const int N = 200 + 10;

int n, k;
double p[N];

inline void check(double &lhs, double rhs) { if (rhs > lhs) lhs = rhs; }

int m;
double q[N];

double solve() {
  static double f[N][N];
  memset(f, 0, sizeof f);
  f[0][0] = 1;
  for (int i = 0; i < k; ++i) {
    for (int j = 0; j <= i; ++j) {
      double cur = f[i][j];
      f[i + 1][j + 1] += cur * q[i];
      f[i + 1][j] += cur * (1. - q[i]);
    }
  }
  return f[k][k / 2];
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) scanf("%lf", &p[i]);
    std::sort(p, p + n);
    double ans = 0.;
    for (int i = 0; i <= k; ++i) {
      int j = k - i;
      m = 0;
      for (int t = 0; t < i; ++t) q[m++] = p[t];
      for (int t = 0; t < j; ++t) q[m++] = p[n - 1 - t];
      ans = std::max(ans, solve());
    }
    printf("Case #%d: %.10f\n", tid, ans);
  }
  return 0;
}
