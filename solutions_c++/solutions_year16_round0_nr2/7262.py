#include <bits/stdc++.h>
using namespace std;


string s;
int main() {
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    cin >> s;
    int ans = 0;
    for (int i = (int)s.size() - 1; i >= 0; --i) {
      if (s[i] == '-') {
        ++ans;
        for (int j = 0; j <= i; ++j) {
          if (s[j] == '-') {
            s[j] = '+';
          } else {
            s[j] = '-';
          }
        }
      }
    }
    cout << "Case #" << tc << ": " << ans << '\n';
  }
}
