#include <bits/stdc++.h>

using namespace std;

const int w[] = {1, 2, 0};
const string ch[] = {"P", "R", "S"};

int n;
int used[3];
int have[3];
int t[1 << 15];

void dfs(int x, int v) {
  if (x > (1 << (n + 1)) - 1) {
    return;
  }
  t[x] = v;
  dfs(2 * x, v);
  dfs(2 * x + 1, w[v]);
}

string solve(string s) {
  int len = s.length();
  if (len == 1) {
    return s;
  }
  string x = solve(s.substr(0, len / 2));
  string y = solve(s.substr(len / 2, len / 2));
  return x < y ? x + y : y + x;
}

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  freopen("log", "w", stderr);
  int tt;
  scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    printf("Case #%d: ", cc);
    scanf("%d %d %d %d", &n, have + 1, have + 0, have + 2);
    string ans = "IMPOSSIBLE";
    for (int it = 0; it < 3; ++it) {
      dfs(1, it);
      memset(used, 0, sizeof used);
      string cur = "";
      for (int i = (1 << n); i < (1 << (n + 1)); ++i) {
        ++used[t[i]];
        cur += ch[t[i]];
      }
      bool ok = true;
      for (int i = 0; i < 3; ++i) {
        if (used[i] > have[i]) {
          ok = false;
        }
      }
      if (!ok) {
        continue;
      }

      cur = solve(cur);
      if (ans == "IMPOSSIBLE") {
        ans = cur;
      } else {
        if (cur < ans) {
          ans = cur;
        }
      }
    }
    printf("%s\n", ans.c_str());
  }
  return 0;
}