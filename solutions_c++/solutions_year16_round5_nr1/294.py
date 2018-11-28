#include <bits/stdc++.h>

using namespace std;

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cout << "Case #" << t << ": ";
    string s;
    cin >> s;
    int n = s.size();
    stack<char> p;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (p.size() and p.top() == s[i]) p.pop();
      else p.push(s[i]);
    }
    cout << 5 * n - 5 * (int(p.size()) / 2) << endl;
  }
}