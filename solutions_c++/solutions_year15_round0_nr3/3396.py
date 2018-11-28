#include <bits/stdc++.h>

using namespace std;

int multiply(int x, int y) {
  int sign = 1;
  if (x < 0)
    sign *= -1, x *= -1;
  if (y < 0)
    sign *= -1, y *= -1;
  if (x == 1)
    return y * sign;
  if (y == 1)
    return x * sign;
  if (x == y)
    return -1 * sign;
  if (x == 'i') {
    if (y == 'j')
      return 'k' * sign;
    if (y == 'k')
      return -('j') * sign;
  }
  if (x == 'j') {
    if (y == 'i')
      return -('k') * sign;
    if (y == 'k')
      return 'i' * sign;
  }
  if (x == 'k') {
    if (y == 'i')
      return 'j' * sign;
    if (y == 'j')
      return -('i') * sign;
  }
  return -1 * sign;
}

int mul[10004][10004];

int main() {
  freopen("C-small-attempt2.in", "r", stdin);
  freopen("C-small-attempt2.out", "w", stdout);
  int T, tst = 1;
  cin >> T;
  while (T--) {
    int L, X;
    string s;
    cin >> L >> X >> s;
    string tmp = s;
    while (--X)
      s += tmp;
    int n = s.size();
    for (int i = 0; i < n; ++i) {
      int res = 1;
      for (int j = i; j < n; ++j) {
        res = multiply(res, s[j]);
        mul[i][j] = res;
      }
    }
    bool can = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j + 1 < n; ++j) {
        if (mul[0][i] == 'i' && mul[i + 1][j] == 'j' && mul[j + 1][n - 1] == 'k') {
          can = 1;
          break;
        }
      }
      if (can)
        break;
    }
    if (can)
      cout << "Case #" << tst << ": YES\n";
    else
      cout << "Case #" << tst << ": NO\n";
    ++tst;
  }
}



