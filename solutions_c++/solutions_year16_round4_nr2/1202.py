#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

const int maxN = 17;
int tests, n, K;
double prob[maxN];

double solve() {
  double ret = 0;
  for (int mask = 0; mask < (1 << n); ++mask) {
    if (__builtin_popcount(mask) == K) {
      double tmp = 0;
      for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
        if (__builtin_popcount(sub) == K / 2) {
          double tmp2 = 1;
          for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
              if ((sub >> i) & 1) tmp2 *= prob[i+1];
              else tmp2 *= (1 - prob[i+1]);
            }
          }
          tmp += tmp2;
        }
      }
      ret = max(tmp, ret);
    }
  }
  return ret;
}

int main() {
  freopen("B-small-attempt0.in", "r", stdin);

  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    rd(n, K);
    for (int i = 1; i <= n; ++i) {
      rd(prob[i]);
    }
    printf("Case #%d: %.10f\n", tt, solve());
  }

  return 0;
}
