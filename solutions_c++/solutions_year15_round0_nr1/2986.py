#include <iostream>

using namespace std;

void solve() {
  int n;
  cin >> n;
  string s;
  cin >> s;
  int res = 0, cnt = 0;
  for (int i = 0; i <= n; ++i) {
    cnt += s[i] - '0';
    --cnt;
    if (cnt < 0) {
      ++res;
      ++cnt;
    }
  }
  cout << res << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
}
