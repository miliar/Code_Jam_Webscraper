//CONTEST SOURCE
#include <cstring>
#include <iostream>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000
int n, t, r, p, s;
char tmp[4444], check[4444];
bool generate(int n, int p, int r, int s, int cur) {
  if ((1 << n) == cur) {
    for(int i = 0; i < (1 << n); ++i) check[i] = tmp[i];
    for(int jmp = 2; jmp <= (1 << n); jmp *= 2) {
      for(int pos = 0; pos < (1 << n); pos += jmp) {
        if (check[pos] == check[pos + jmp / 2]) return 0;
        if (check[pos] == 'R' && check[pos + jmp / 2] == 'P') check[pos] = 'P'; else
        if (check[pos] == 'S' && check[pos + jmp / 2] == 'R') check[pos] = 'R'; else
        if (check[pos] == 'P' && check[pos + jmp / 2] == 'S') check[pos] = 'S';
      }
    }
    return 1;
  }
  if (p && (cur == 0 || tmp[cur - 1] != 'P')) {
    tmp[cur] = 'P';
    if (generate(n, p - 1, r, s, cur + 1)) return 1;
  }
  if (r && (cur == 0 || tmp[cur - 1] != 'R')) {
    tmp[cur] = 'R';
    if (generate(n, p, r - 1, s, cur + 1)) return 1;
  }
  if (s && (cur == 0 || tmp[cur - 1] != 'S')) {
    tmp[cur] = 'S';
    if (generate(n, p, r, s - 1, cur + 1)) return 1;
  }
  return 0;
}
string opt[13][3];
int main() {
  opt[0][0] = "R";
  opt[0][1] = "S";
  opt[0][2] = "P";
  for(int len = 1; len <= 12; ++len) {
    opt[len][0] = min(opt[len - 1][0] + opt[len - 1][1], opt[len - 1][1] + opt[len - 1][0]);
    opt[len][1] = min(opt[len - 1][1] + opt[len - 1][2], opt[len - 1][2] + opt[len - 1][1]);
    opt[len][2] = min(opt[len - 1][2] + opt[len - 1][0], opt[len - 1][0] + opt[len - 1][2]);
  }
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);
  for(int tc = 1; tc <= t; ++tc) {
    scanf("%d%d%d%d", &n, &r, &p, &s);
    string ans = "";
    for(int j = 0; j < 3; ++j) {
      int mr = 0, mp = 0, ms = 0;
      for(int i = 0; i < (1 << n); ++i) {
        if (opt[n][j][i] == 'R') ++mr; else
          if (opt[n][j][i] == 'P') ++mp; else
            ++ms;
      }
      if (mr == r && mp == p && ms == s && (ans == "" || ans > opt[n][j])) ans = opt[n][j];
    }
    cout << "Case #" << tc << ": ";
    if (ans == "") cout << "IMPOSSIBLE\n"; else cout << ans << endl;
  }
}

