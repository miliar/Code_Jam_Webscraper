#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; ++tt) {
    cerr << tt << endl;
    string s;
    cin >> s;
    string res;
    for (char c : s) {
      res = max(res + c, c + res);
    }
    cout << "Case #" << tt << ": " << res << endl;
  }
  return 0;
}
