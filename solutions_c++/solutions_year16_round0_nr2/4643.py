#include <bits/stdc++.h>
using namespace std;

int solve() {
  string s;
  cin >> s;

  string finish(s.size(), '+');

  int ans = 0;
  while (s != finish) {
    int np = 0;
    while (s[np] == '+') {
      ++np;
    }
    if (np > 0) {
      for (int i = 0; i < np; ++i) {
        s[i] = '-';
      }
      ++ans;
    }
    while (np < s.size() && s[np] == '-') {
      ++np;
    }
    for (int i = 0; i < np; ++i) {
      s[i] = '+';
    }
    ++ans;
  }
  return ans;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    cout << "Case #" << test << ": " << solve() << endl;
  }
}
