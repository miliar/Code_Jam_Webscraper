#include <bits/stdc++.h>
using namespace std;
template<typename T> inline void checkMin(T &a, T b) { if(b<a) a=b; }
template<typename T> inline void checkMax(T &a, T b) { if(a<b) a=b; }
#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

double calc(double d1, double d2, double p1, double p2, double v) {
  double t = p1 * d2 + p2 * d1;
  double t1 = v * d2 / t;
  double t2 = v * d1 / t;
  return max(t1, t2);
}

void solve() {
  int n, c1 = 0, c2 = 0, c3 = 0;
  double v, x, r[128], c[128];
  scanf("%d%lf%lf", &n, &v, &x);
  double d1 = 0, d2 = 0, p1 = 0, p2 = 0, p3 = 0;
  REP (i, n) {
    scanf("%lf%lf", &r[i], &c[i]);
    if (c[i] > x) {
      d1 += (c[i] - x) * r[i];
      p1 += r[i];
      ++c1;
    } else if (c[i] < x) {
      d2 += (x - c[i]) * r[i];
      p2 += r[i];
      ++c2;
    } else {
      p3 += r[i];
      ++c3;
    }
  }

  if (c3 == 0 && (d1 == 0 || d2 == 0)) {
    printf("IMPOSSIBLE\n");
    return;
  }

  if (c3 == 0) {
    printf("%.10lf\n", calc(d1, d2, p1, p2, v));
  } else {
    double l = 0, r = v / p3;
    while (r - l > 1e-9) {
      double t3 = (l + r) * 0.5;
      double t12 = calc(d1, d2, p1, p2, v - p3 * t3);
      if (t12 < t3) {
        r = t3;
      } else {
        l = t3;
      }
    }
    printf("%.10lf\n", (l + r) * 0.5);
  }
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: ", index);
    solve();
  }
  return 0;
}
