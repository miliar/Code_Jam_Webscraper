// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

const double eps = 1e-9;

typedef pair<double, double> pdd;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n;
    cin >> n;
    double v, x;
    cin >> v >> x;
    vector<pdd> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i].first >> a[i].second;
    }
    if (n == 1) {
      if (fabs(a[0].second - x) > eps) {
        cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
      } else {
        cout << "Case #" << t << ": " << fixed << setprecision(9) << v / a[0].first << endl;
      }
    } else if (n == 2) {
      bool ok = false;
      double ans = 1e100;
      if (fabs(a[0].second - x) < eps) {
        ok = true;
        ans = min(ans, v / a[0].first);
      }
      if (fabs(a[1].second - x) < eps) {
        ok = true;
        ans = min(ans, v / a[1].first);
      }
      {
        if (a[0].second > a[1].second) {
          swap(a[0], a[1]);
        }
        if (a[1].second >= x && a[0].second <= x) {
          if (fabs(a[1].second - x) > eps) {
            double v0 = 1.0;
            double v1 = (x - a[0].second) / (a[1].second - x);
            double k = v / (v0 + v1);
            ok = true;
            ans = min(ans, k * max(v0 / a[0].first, v1 / a[1].first));
          } else if (fabs(a[0].second - x) > eps) {
            double v0 = (a[1].second - x) / (x - a[0].second);
            double v1 = 1.0;
            double k = v / (v0 + v1);
            ok = true;
            ans = min(ans, k * max(v0 / a[0].first, v1 / a[1].first));
          } else {
            ok = true;
            ans = min(ans, v / (a[0].first + a[1].first));
          }
        }
      }
      if (ok) {
        cout << "Case #" << t << ": " << fixed << setprecision(9) << ans << endl;
      } else {
        cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
      }
    } else {
      assert(0);
      /* */
    }
  }
  return 0;
}

