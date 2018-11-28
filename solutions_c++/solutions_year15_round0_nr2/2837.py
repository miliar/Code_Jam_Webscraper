#include <iostream>
#include <queue>
using namespace std;

int p[1010];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n; cin >> n;
    for (int i = 0; i < n; i++) cin >> p[i];

    int res = 1000;
    for (int i = 1; i <= 1000; i++) {
      int cur = 0;
      for (int j = 0; j < n; j++) cur += (p[j] - 1) / i;
      res = min(res, cur + i);
    }
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
