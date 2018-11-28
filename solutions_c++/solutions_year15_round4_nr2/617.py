#include <algorithm>
#include <cmath>
#include <complex>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

const double EPS = 1e-6;

int main() {
  std::ios_base::sync_with_stdio(false);
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    // Input
    int n;
    double v, x;
    std::vector<double> R;
    std::vector<double> C;
    std::cin >> n >> v >> x;
    for (int j = 0; j < n; j++) {
      double r, c;
      std::cin >> r >> c;
      R.push_back(r);
      C.push_back(c);
    }
    // Solve
    double y = 0;
    bool success = false;
    if (n == 1) {
      if (fabs(C[0] - x) < EPS) {
        y = v / R[0];
        success = true;
      }
    } else {  // n == 2
      if (fabs(C[0] - x) < EPS && fabs(C[1] - x) < EPS) {
        y = v / (R[0] + R[1]);
        success = true;
      } else if (fabs(C[0] - x) < EPS) {
        y = v / R[0];
        success = true;
      } else if (fabs(C[1] - x) < EPS) {
        y = v / R[1];
        success = true;
      } else if ((C[0] - x) * (C[1] - x) < 0) {
        double t0 = ((C[1] - x) * v) / ((C[1] - C[0]) * R[0]);
        double t1 = ((C[0] - x) * v) / ((C[0] - C[1]) * R[1]);
        y = std::max(t0, t1);
        success = true;
      }
    }
    // Output
    std::cout << "Case #" << i + 1 << ": ";
    if (success) {
      std::cout << std::fixed << std::setprecision(9) << y;
    } else {
      std::cout << "IMPOSSIBLE";
    }
    std::cout << std::endl;
  }
}
