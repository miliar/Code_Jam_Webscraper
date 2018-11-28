#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

main() {
  int T, N, prob=1;
  for (cin >> T; T--;) {
    double V, X;
    cin >> N >> V >> X;
    vector<pair<double, double> > CR(N);
    bool lt = false, gt = false;
    for (int i = 0; i < N; i++) {
      cin >> CR[i].second >> CR[i].first;
      if (CR[i].first == X) {
        lt = gt = true;
      } else if (CR[i].first < X) {
        lt = true;
      } else {
        gt = true;
      }
    }
    if (!lt || !gt) {
      printf("Case #%d: IMPOSSIBLE\n", prob++);
      continue;
    }
    sort(CR.begin(), CR.end());

    vector<double> F(N);
    double tot = 0.0;
    for (int i = 0; i < N; i++) {
      F[i] = CR[i].second;
      tot += F[i] * (CR[i].first - X);
    }
    for (int i = 0; tot < 0.0; i++) {
      double delta = X - CR[i].first;
      if (delta == 0.0) break;
      if (tot + delta * F[i] >= 0.0) {
        F[i] -= -tot/delta;
        tot = 0.0;
        break;
      } else {
        tot += delta * F[i];
        F[i] = 0.0;
      }
    }
    for (int i = N-1; tot > 0.0; i--) {
      double delta = CR[i].first - X;
      if (delta == 0.0) break;
      if (tot - delta * F[i] <= 0.0) {
        F[i] -= tot/delta;
        tot = 0.0;
        break;
      } else {
        tot -= delta * F[i];
        F[i] = 0.0;
      }
    }

    double totf = 0.0;
    for (int i = 0; i < N; i++) totf += F[i];
    printf("Case #%d: %.9lf\n", prob++, V/totf);
  }
}
