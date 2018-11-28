#include <iostream>
#include <iomanip>

double lower_bound(double C, double F, double X) {
  double z = 0.0;
  double cps = 2.0;

  while (true) {
    double win_now = X / cps;
    double tt_farm = C / cps;
    cps += F;
    double win_later = tt_farm + (X / cps);

    if (win_now < win_later) {
      return z + win_now;
    } else {
      z += tt_farm;
    }
  }
}

int main() {
  using namespace std;

  int T;
  cin >> T;

  cout << fixed << setprecision(7);
  for (int t = 0; t < T; ++t) {
    double C, F, X;
    cin >> C >> F >> X;

    double r = lower_bound(C, F, X);
    cout << "Case #" << (t + 1) << ": " << r << endl;
  }
}

