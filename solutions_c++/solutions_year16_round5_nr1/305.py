#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

string s;
int dp[20005][20005][2];
int n;

int DFS(int b, int e, int k) {
  if (b == e) {
    return 0;
  }
  if (dp[b][e][k] >= 0) {
    return dp[b][e][k];
  }
  int ans = 0;
  if (k == 0) {
    for (int i = b + 2; i < e; i += 2) {
      ans = max(ans, DFS(b, i, 1) + DFS(i, e, 0));
    }
  }
  ans = max(ans, DFS(b + 1, e - 1, 0) + (s[b] == s[e - 1] ? 10 : 5));
  return dp[b][e][k] = ans;
}

void Solve() {
  cin >> s;
  n = s.size();
  for (int i = 0; i <= n; ++i) {
    for (int j = 0; j <= n; ++j) {
      for (int k = 0; k < 2; ++k) {
        dp[i][j][k] = -1;
      }
    }
  }
  cout << DFS(0, n, 0) << endl;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
