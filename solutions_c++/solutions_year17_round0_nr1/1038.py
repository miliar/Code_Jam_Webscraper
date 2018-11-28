#include <bits/stdc++.h>

using namespace std;



int solve(string &s, int K) {
  int ret = 0;
  for (int i = 0; i < s.size()-(K-1); ++i) {
    char c = s[i];
    if (c=='-') {
      ret++;
      for (int j = i; j < i+K; ++j) {
        s[j] = s[j]=='-' ? '+' : '-';
      }
    }
  }
  for (auto &c : s) if (c=='-') return -1;
  return ret;
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    string s;
    int K;
    cin >> s >> K;
    int ans = solve(s, K);
    cout << "Case #" << i << ": ";
    if (ans>=0) cout << ans << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}
