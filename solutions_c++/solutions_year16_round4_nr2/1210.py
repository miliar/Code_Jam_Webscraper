#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int K;
double ptie;
double ctie;

void check(const double *x, int k, int r, double p) {
  if (r > k || r < -k) return;

  if (k == 0) {
    ctie += p;
    return;
  }

  check(x + 1, k - 1, r + 1, p * *x);
  check(x + 1, k - 1, r - 1, p * (1.0 - *x));
}

void check(const double *x) {
  ctie = 0.0;
  check(x, K, 0, 1.0);
  ptie = max(ptie, ctie);
}

void takeKofN(int k, int n, const double *p, const double *x, double *ret) {
  if (k > n) return;
  if (k == 0) {
    check(x);
    return;
  }
  takeKofN(k, n - 1, p + 1, x, ret);
  *ret = *p;
  takeKofN(k - 1, n - 1, p + 1, x, ret + 1);
}

void solve() {
  int n, k;
  scanf("%d%d", &n, &k);
  K = k;
  double p[n];
  double pk[n];
  for (int i = 0; i < n; ++i) scanf("%lf", p + i);
  ptie = 0.0;
  takeKofN(k, n, p, pk, pk);
  printf("%.10lf\n", ptie);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
