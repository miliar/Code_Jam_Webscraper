#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int T, ti, L, X;
string s;
char dic[128];
int f[5][5] = {
  {0, 0, 0, 0, 0},
  {0, 1, 2, 3, 4},
  {0, 2, -1, 4, -3},
  {0, 3, -4, -1, 2},
  {0, 4, 3, -2, -1}
};
int a[10002][10002];

inline int mul(int x, int y) {
  return (x * y < 0? -f[abs(x)][abs(y)]: f[abs(x)][abs(y)]);
}

int solve() {
  cin >> L >> X >> s;
  int t = 1;
  for (int i = 0; i < L*X; ++i)
    a[i][i] = dic[s[i%L]], t = mul(t, a[i][i]);
  if (t != -1 || L*X < 3) {
    printf("Case #%d: NO\n", ti);
    return 0;
  }
  for (int i = 0; i < L*X-1; ++i)
    for (int j = i+1; j < L*X; ++j)
      a[i][j] = mul(a[i][j-1], a[j][j]);
  for (int i = 0; i < L*X-2; ++i) {
    if (a[0][i] == 2) {
      for (int j = i+1; j < L*X-1; ++j)
        if (a[i+1][j] == 3 && a[j+1][L*X-1] == 4) {
          // cout << i << " " << j << endl;
          printf("Case #%d: YES\n", ti);
          return 0;
        }
    }
  }
  printf("Case #%d: NO\n", ti);
  return 0;
}

int main() {
    cin >> T;
    dic['i'] = 2;
    dic['j'] = 3;
    dic['k'] = 4;
    for (ti = 1; ti <= T; ti++) {
        solve();
    }
    return 0;
}
