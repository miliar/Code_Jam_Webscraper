#include <iostream>

using namespace std;

double
solve(double C, double F, double X) {
  double res = X / 2.0;
  double t = 0.0;
  double r = 2.0;
  for (int f = 1;; ++f) {
    t += C / r;
    r += F;

    if (t + X / r <= res) {
      res = t + X / r;
    } else {
      break;
    }
  }

  return res;
}

int
main() {
  int T;
  cin >> T;
  
  cout.precision(7);
  for (int t = 1; t <= T; ++t) {
    double C, F, X;
    cin >> C >> F >> X;
    cout << "Case #" << t << ": " 
         << fixed << solve(C, F, X) << endl;
  }

  return 0;
}
