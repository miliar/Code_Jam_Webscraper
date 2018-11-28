#include <iostream>
#include <string>
using std::min;
using std::max;

const int MAXN = 128;
const int INF = 1e8;

int n, f[MAXN][2];
std::string s;

int solve(std::string s) {
  f[0][0] = f[0][1] = 0;
  for (int i = 1; i <= s.size(); i++) {
    f[i][0] = f[i][1] = INF;
    for (int j = i; j; j--) {
      if (s[j - 1] != s[i - 1]) break;
      if (s[i - 1] == '+') {
        f[i][0] = min(f[i][0], f[j - 1][0]);
        f[i][0] = min(f[i][0], f[j - 1][1] + 1);
        f[i][1] = min(f[i][1], f[j - 1][0] + 1);
        f[i][1] = min(f[i][1], f[j - 1][1] + 2);
      } else {
        f[i][0] = min(f[i][0], f[j - 1][0] + 2);
        f[i][0] = min(f[i][0], f[j - 1][1] + 1);
        f[i][1] = min(f[i][1], f[j - 1][0] + 1);
        f[i][1] = min(f[i][1], f[j - 1][1]);
      }
    }
  }
  return min(f[s.size()][0], f[s.size()][1] + 1);
}

int main() {
  std::cin >> n;
  for (int i = 0; i < n; i++) {
    std::cin >> s;
    printf("Case #%d: %d\n", i + 1, solve(s));
  }
}
