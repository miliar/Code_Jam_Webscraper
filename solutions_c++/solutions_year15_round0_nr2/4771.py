#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T ; ++t) {
    int D;
    vector<int> P;
    cin >> D;
    for (int d = 0; d < D; ++d) {
      int p;
      cin >> p;
      P.push_back(p);
    }
    int max_value = *max_element(P.begin(), P.end());
    int ans = 10000;
    for (int p = 1; p <= max_value; ++p) {
      int special_mins = 0;
      for (int i = 0; i < P.size(); ++i) {
        if (P[i] > p) {
          special_mins += floor((double)(P[i]-1) / p);
        }
      }
      if (ans > special_mins + p)
        ans = special_mins + p;
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
