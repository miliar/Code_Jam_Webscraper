#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cout.tie(0);cin.tie(0);
using namespace std;

void solve() {
  int ans = 0;
  string s;
  vector<char> f;

  cin >> s;

  for (int i = 0; i < s.length(); i++) {
    int c = 0;
    while (i < s.length() && s[i] == '-') {
      c++; i++;
    }
    if (c > 0) {
      f.push_back('-');
    }
    c = 0;
    while (i < s.length() && s[i] == '+') {
      c++; i++;
    }
    if (c > 0) {
      f.push_back('+');
      i--;
    }
  }

  for (int i = 0; i < f.size(); i += 2) {
    if (i+1 == f.size()) {
      ans += f[i] == '-';
    }
    else if (f[i] == '+' && f[i+1] == '-') {
      ans++;
      if (i+2 <= f.size()) ans++;
    } 
    else if (f[i] == '-' && f[i+1] == '+') {
      ans++;
      if (i+2 < f.size()) ans++;
    }
  }
  cout << ans << "\n";
}

int main() { _
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; t++) {
    cout << "Case #" << t << ": ";
    solve();
  }
  return 0;
}
