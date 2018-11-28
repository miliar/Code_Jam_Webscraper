#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int D;
    cin >> D;
    int vals[1005] = {};
    for (int i = 0; i < D; ++i) {
      int v;
      cin >> v;
      vals[v]++;
    }
    int min_time = 1000000000;
    for (int i = 1; i <= 1005; ++i) {
      int total = 0;
      for (int k = i + 1; k < 1005; ++k) {
        total += (k / i + (bool)(k % i) - 1) * vals[k];
      }
      min_time = min(min_time, total + i);
    }
    cout << "Case #" << t << ": " << min_time << endl;
  }
}
