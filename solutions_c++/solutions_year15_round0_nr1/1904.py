#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int n;
    cin >> n;
    char c;
    int res = 0;
    int sum = 0;
    for (int i = 0; i <= n; ++i) {
      cin >> c;
      int k = (int)(c - '0');
      sum -= 1;
      sum += k;
      if (sum == -1) {
        ++res;
        ++sum;
      }
    }
    cout << "Case #" << tt << ": " << res << endl;
  }
  return 0;
}
