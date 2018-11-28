#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

#define EPS 1e-9

int main() {
  int t; cin >> t;
  for (int test = 1; test <= t; ++test) {
    int n; cin >> n;
    double vol, temp; cin >> vol >> temp;
    vector<double> rates, temps;
    for (int i = 0; i < n; ++i) {
      double ri, ci; cin >> ri >> ci;
      rates.push_back(ri);
      temps.push_back(ci);
    }

    cout << "Case #" << test << ": ";
    if (n == 1) {
      if (abs(temps[0] - temp) < EPS) {
        cout << fixed << setprecision(8) << (vol / rates[0]);
      } else {
        cout << "IMPOSSIBLE";
      }
    } else { // n == 2
      if (abs(temps[0] - temp) < EPS &&
          abs(temps[1] - temp) < EPS) {
        cout << fixed << setprecision(9) << (vol / (rates[0] + rates[1]));
      } else if (abs(temps[0] - temp) < EPS) {
        cout << fixed << setprecision(9) << (vol / rates[0]);
      } else if (abs(temps[1] - temp) < EPS) {
        cout << fixed << setprecision(9) << (vol / rates[1]);
      } else {
        double alpha = (temp - temps[1]) / (temps[0] - temps[1]);
        if (alpha < -EPS || alpha > 1 + EPS) {
          cout << "IMPOSSIBLE";
        } else {
          double rate0 = rates[0];
          double rate1 = min(rates[1], rate0 / alpha * (1 - alpha));
          rate0 = min(rate0, rate1 / (1 - alpha) * alpha);
          cout << fixed << setprecision(9) << (vol / (rate0 + rate1));
        }
      }
    }

    cout << endl;
  }
  return 0;
}