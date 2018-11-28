#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int solve(string s) {
  int n = s.size();
  int res = 0;
  for (int i = n-1; i >= 0; --i) {
    if (s[i] == '+') continue;
    res++;
    for (int j = 0; j <= i; ++j) {
      if (s[j] == '+') s[j] = '-';
      else s[j] = '+';
    }
  }
  return res;
}

int main() {
  int T; cin >> T;
  for (int tt = 1; tt <= T; ++tt) {
    string s; cin >> s;
    int res = solve(s);
    cout << "Case #" << tt << ": " << res << '\n';
  }
  return 0;
}
