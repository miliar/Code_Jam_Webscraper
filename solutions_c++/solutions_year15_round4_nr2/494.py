#include <bits/stdc++.h>
  
using namespace std;

template<class T> inline T sqr(const T& a) { return a * a; }
  
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
  
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 100;

ld rate[N];
ld temper[N];

inline ld Avg2(ld v0, ld v1) {
  return (v0 * temper[0] + v1 * temper[1]) / (v0 + v1);
}

void Solve() {
  int n;
  ld v, x;
  cin >> n >> v >> x;
  assert(n <= 2);
  ld mint = 1000, maxt = 0;
  for (int i = 0; i < n; ++i) {
    cin >> rate[i] >> temper[i];      
    mint = min(mint, temper[i]);
    maxt = max(maxt, temper[i]);
  }
  if (n > 1 && temper[0] > temper[1] + EPS) {
    swap(temper[0], temper[1]);
    swap(rate[0], rate[1]);
  }
  if (x < mint - EPS || x > maxt + EPS) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  if (n == 1) {
    cout << fixed << v / rate[0] << endl;
    return;
  }
  if (fabs(temper[0] - temper[1]) < EPS) {
    cout << fixed << v / (rate[0] + rate[1]) << endl;
    return;
  }
  for (int i = 0; i < n; ++i) {
    if (fabs(x - temper[i]) < EPS) {
      cout << fixed << v / rate[i] << endl;
      return;
    }  
  }
  ld lf = 0, rg = 1e9;
  for (int itt = 0; itt < 100; ++itt) {
    ld mid = (lf + rg) / 2;
    ld val = Avg2(1.0, mid);
    if (val < x)
      lf = mid;
    else
      rg = mid;
  }
  cerr.precision(12);
  cerr << fixed << "error value for lf=" << lf << ": " << x - Avg2(1.0, lf) << endl;
  ld v0 = 1.0 * v / (1.0 + lf);
  ld v1 = lf * v / (1.0 + lf);
  ld ans = max(v0 / rate[0], v1 / rate[1]);
  cout << fixed << ans << endl;
}

int main() {
  int tests;
  cin >> tests;
  cout.precision(9);
  for (int it = 1; it <= tests; ++it) {
    cout << "Case #" << it << ": ";
    Solve();
  }

  return 0;
}
