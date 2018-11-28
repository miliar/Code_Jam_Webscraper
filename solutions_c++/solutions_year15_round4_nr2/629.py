#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

void solve() {
  int n;
  double V, T;
  cin >> n >> V >> T;
  if (n == 1) {
    double r1, t1;
    cin >> r1 >> t1;
    if (t1 == T) {
      cout << V/r1 << endl;
    }
    else {
      cout << "IMPOSSIBLE" << endl;
    }
    return;
  }
  double r1, t1, r2, t2;
  cin >> r1 >> t1 >> r2 >> t2;

  if (t2 != t1) {
    double v2 = V*(T - t1)/(t2 - t1);
    double v1 = V - v2;
    if (v1 + 1e-7 >= 0 and v2 + 1e-7 >= 0) cout << max(v1/r1, v2/r2) << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
  else if (t1 == T) {
    cout << V/(r1 + r2) << endl;
  }
  else cout << "IMPOSSIBLE" << endl;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(9);
  int casos;
  cin >> casos;
  for (int cas = 1; cas <= casos; ++cas) {
    cout << "Case #" << cas << ": ";
    solve();
  }
}
