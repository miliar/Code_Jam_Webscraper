#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const int N = 100+5;
int grid[N][N];
bool seen[N][N];
void solve() {
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      scanf("%d", &grid[i][j]);
    }
  }

  memset(seen, 0, sizeof seen);
  int p = 0;
  while (true) {
    int x = -1, y = -1;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (!seen[i][j] && (grid[i][j] < grid[x][y] || x == -1)) {
          x = i;
          y = j;
        }
      }
    }
    if (x == -1) break;
    bool colfail = false;
    for (int j = 0; j < m; j++) {
      if (!seen[x][j] && grid[x][j] > grid[x][y]) {
        colfail = true; break;
      }
    }
    bool rowfail = false;
    for (int i = 0; i < n; i++) {
      if (!seen[i][y] && grid[i][y] > grid[x][y]) {
        rowfail = true; break;
      }
    }
    if (!colfail) {
      for (int j = 0; j < m; j++) {
        seen[x][j] = true;
      }
    } else if (!rowfail) {
      for (int i = 0; i < n; i++) {
        seen[i][y] = true;
      }
    }
    if (rowfail && colfail) {
      printf("NO\n");
      return;
    }
  }
  printf("YES\n");
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}

