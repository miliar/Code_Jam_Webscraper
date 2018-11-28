#include <bits/stdc++.h>

using namespace std;

int main() {
#ifdef DEBUG
  freopen("input.txt", "rt", stdin);
#else
  freopen("B.in", "rt", stdin);
  freopen("B.out", "wt", stdout);
#endif
  int t; cin >> t;
  for(int tst = 1; tst <= t; ++tst) {
    string s; cin >> s; s += "+";
    int ans = 0;
    for(int i = 0; i + 1 < (int)s.size(); ++i) {
      ans += s[i] != s[i + 1];
    }
    printf("Case #%d: %d\n", tst, ans);
  }
  return 0;
}
