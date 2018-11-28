#include <iostream>
#include <vector>

using namespace std;

int main() {
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int d;
    cin >> d;
    vector<int> p(d);
    for (int i = 0; i < d; ++i) {
      cin >> p[i];
    }
    int res = 1000;
    for (int h = 1; h <= 1000; ++h) {
      int curr_res = h;
      for (int i = 0; i < d; ++i) {
        if (p[i] <= h) { continue; }
        curr_res += (p[i] - 1) / h;
      }
      res = min(res, curr_res);
    }
    cout << "Case #" << test_index + 1 << ": " << res << "\n";
  }
  return 0;
}
