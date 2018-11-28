#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const double EPS = 0.00000001;

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int n;
    double v, x;
    cin >> n >> v >> x;
    vector<double> rate(n, 0.0);
    vector<double> temp(n, 0.0);
    for (int i = 0; i < n; ++i) {
      cin >> rate[i] >> temp[i];
    }

    if (n == 1) {
      if (std::abs(temp[0] - x) < EPS) {
        cout << "Case #" << tt << ": " << setprecision(16) << (v / rate[0]) << endl;
      } else {
        cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
      }
    } else if (n == 2) {
      if (std::abs(temp[0] - x) < EPS && std::abs(temp[1] - x) < EPS) {
        cout << "Case #" << tt << ": " << setprecision(16) << (v / (rate[0] + rate[1])) << endl;
      } else if (std::abs(temp[0] - x) < EPS) {
        cout << "Case #" << tt << ": " << setprecision(16) << (v / rate[0]) << endl;
      } else if (std::abs(temp[1] - x) < EPS) {
        cout << "Case #" << tt << ": " << setprecision(16) << (v / rate[1]) << endl;
      } else {
        if (temp[0] > temp[1]) {
          double tmp = temp[0]; temp[0] = temp[1]; temp[1] = tmp;
          tmp = rate[0]; rate[0] = rate[1]; rate[1] = tmp;
        }
        if (temp[0] < x && x < temp[1]) {
          double vol0 = ((temp[1] - x) / (temp[1] - temp[0])) * v;
          double vol1 = ((x - temp[0]) / (temp[1] - temp[0])) * v;
          cout << "Case #" << tt << ": " << setprecision(16)
               << std::max(vol0 / rate[0], vol1 / rate[1]) << endl;
        } else {
          cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
        }
      }
    } else {
      cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
    }  
  }
  return 0;
}
