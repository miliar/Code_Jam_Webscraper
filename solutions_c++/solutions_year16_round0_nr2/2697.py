#include <bits/stdc++.h>

using namespace std;

struct Initializer {
  Initializer() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    cout << fixed << setprecision(15);
  }
} initializer;

int solve() {
  string s;
  cin >> s;
  int res = 0;
  for (int i = 0; i < (int)s.size() - 1; ++i) {
    if (s[i] != s[i + 1]) ++res;
  }
  if (s.back() == '-') ++res;
  return res;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) cout << "Case #" << i << ": " << solve() << endl;
}
