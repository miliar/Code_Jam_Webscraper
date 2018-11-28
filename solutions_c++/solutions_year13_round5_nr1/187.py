#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int n;
long long b, x[64];
pair<long, int> y[64];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    cin >> b >> n;
    for (int i = 0; i < n; i++) cin >> x[i];
    for (int i = n; i < 37; i++) x[i] = 0;
    sort(x, x+37);

    int yi = 0;
    for (int i = 0; i < 37; i++) {
      int j = i;
      while (j < 37 && x[j] == x[i]) j++;
      y[yi++] = make_pair(x[i], j-i);
      i = j-1;
    }

    double best = 0;
    long long totb = 0;
    int win = 0;
    for (int i = 0; i < yi-1; i++) {
      win += y[i].second;

      for (int j = 0; j < win; j++) {
        if (totb + j <= b) {
          long long addbs[] = { 0, min((b - totb - j) / win, (long long) (y[i+1].first - y[i].first - 1)) };
          for (int l = 0; l < 2; l++) {
            long long addb = addbs[l];
            long long winb = totb + win * addb;
            long long cost = 0;
            for (int k = 0; k < j; k++) cost += (y[i].first + addb - x[win-1-k]);
            // cout << i << " " << j << " " << (36.0 / (win - j) - 1) * (winb - cost) - cost - j << endl;
            best = max(best, (36.0 / (win - j) - 1) * (winb - cost) - cost - j);
          }
        }
      }

      // cout << "loop: " << i << " " << y[i].first << " " << y[i].second << " " << win << " " << totb << << " " << best << endl;

      long long delta = win * (y[i+1].first - y[i].first);
      if (totb + delta > b) break;
      totb += delta;
    }

    cout << fixed << setprecision(10) << "Case #" << c << ": " << best << endl;
  }
  return 0;
}
