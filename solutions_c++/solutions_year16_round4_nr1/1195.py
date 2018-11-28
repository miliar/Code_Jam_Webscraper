#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
#define all(a) (a).begin(), (a).end()
#define sz(a) ((int)(a.size()))

bool valid(const string &s) {
  if (sz(s) <= 1) return true;
  string n;

  for (int i = 0; i < sz(s); i += 2) {
    if (s[i] == s[i + 1])
      return false;
    else {
      set<char> S;
      S.insert(s.begin() + i, s.begin() + i + 2);
      if (S == set<char>{'P', 'S'}) {
        n += 'S';
      } else if (S == set<char>{'S', 'R'}) {
        n += 'R';
      } else {
        n += 'P';
      }
    }
  }
  return valid(n);
}

int main() {
  ios::sync_with_stdio(0);
  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    int n, r, p, s;
    string ans = "Z";

    cin >> n >> r >> p >> s;

    string cur = "";
    for (int i = 0; i < p; ++i) {
      cur += "P";
    }
    for (int i = 0; i < r; ++i) {
      cur += "R";
    }
    for (int i = 0; i < s; ++i) {
      cur += "S";
    }

    do {
      if (valid(cur)) {
        ans = min(ans, cur);
      }
    } while (next_permutation(all(cur)));

    printf("Case #%d: ", cn);
    if (ans == "Z") {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%s\n", ans.c_str());
    }
  }
  return 0;
}
