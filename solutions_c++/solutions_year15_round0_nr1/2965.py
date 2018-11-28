#include <iostream>
using namespace std;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n; string s; cin >> n >> s;
    int res = 0, acc = 0;
    for (int i = 0; i <= n; i++) {
      res += max(0, i - acc);
      acc = max(acc, i);
      acc += s[i] - '0';
    }
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
