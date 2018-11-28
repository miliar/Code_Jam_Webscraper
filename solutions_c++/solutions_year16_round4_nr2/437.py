#include <bits/stdc++.h>

using namespace std;

const int N = 222;

double p[N];
double f[N][N];

double solve(int n) {
  for (int i = 0; i <= n; ++i) {
    for (int j = 0; j <= n / 2; ++j) {
      f[i][j] = 0.0;
    }
  }
  f[0][0] = 1.0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j <= n / 2; ++j) {
      f[i + 1][j] += f[i][j] * (1.0 - p[i]);
      if (j < n / 2) {
        f[i + 1][j + 1] += f[i][j] * p[i];
      }
    }
  }
  return f[n][n / 2];
}

int a[N];

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  freopen("log", "w", stderr);
  int tt;
  scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    printf("Case #%d: ", cc);
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; ++i) {
      double foo;
      scanf("%lf", &foo);
      a[i] = (int)(foo * 100 + 0.5);
    }
    sort(a, a + n);
    double ans = 0.0;
    for (int i = 0; i + i <= k; ++i) {
      for (int j = 0; j < i; ++j) {
        p[j + j] = a[j] / 100.0;
        p[j + j + 1] = a[n - 1 - j] / 100.0;
      }
      for (int j = i; j < n - i; ++j) {
        if (n - i - j < k - i - i) {
          break;
        }
        for (int jj = 0; jj < k - i - i; ++jj) {
          p[i + i + jj] = a[j + jj] / 100.0;
        }
        ans = max(ans, solve(k));
      }
    }
    printf("%.15f\n", ans);
  }
  return 0;
}