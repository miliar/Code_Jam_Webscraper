#include <iostream>
#include <vector>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int d;
    cin >> d;
    vector<int> num(d);
    for (int i = 0; i < d; ++i) {
      cin >> num[i];
    }
    int max = num[0];
    for (int i = 0; i < d; ++i) {
      if (max < num[i]) {
        max = num[i];
      }
    }
    for (int i = 1; i < max; ++i) {
      int cur = i;
      for (int j = 0; j < d; ++j) {
        cur += (num[j] - 1) / i;
      }
      if (cur < max) max = cur;
    }
    cout << "Case #" << tt << ": " << max << endl;
  }
  return 0;
}
