#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int k;
    string s;
    cin >> k >> s;
    vector<int> sums(s.size());
    sums[0] = s[0] - '0';
    for (int i = 1; i < s.size(); ++i) {
      sums[i] = sums[i - 1] + s[i] - '0';
    }
    int res = 0;
    for (int i = 1; i < s.size(); ++i) {
      res = max(res, i - sums[i - 1]);
    } 
    cout << "Case #" << test_index + 1 << ": " << res << "\n";
  }
  return 0;
}
