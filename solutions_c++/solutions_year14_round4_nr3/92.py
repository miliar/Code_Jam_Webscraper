#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using std::string;
using std::vector;
using std::queue;

int w, h, n;
int d[1111][1111];
int dis[1111];
int building[1111][4];
bool b[1111];
queue<int> que;

int Distance(int a, int b) {
  int ans = 1000000000;
  for (int i = 0; i < 4; i += 2) {
    for (int j = 1; j < 4; j += 2) {
      int x = building[a][i];
      int y = building[a][j];
      if (building[b][0] <= x && x <= building[b][2]) {
        ans = std::min(ans, abs(building[b][1] - y) - 1);
        ans = std::min(ans, abs(building[b][3] - y) - 1);
      }
      if (building[b][1] <= y && y <= building[b][3]) {
        ans = std::min(ans, abs(building[b][0] - x) - 1);
        ans = std::min(ans, abs(building[b][2] - x) - 1);
      }
      for (int p = 0; p < 4; p += 2) {
        for (int q = 1; q < 4; q += 2) {
          ans = std::min(ans, std::max(abs(building[b][p] - x), abs(building[b][q] - y)) - 1);
        }
      }
    }
  }
  return ans;
}

int Work() {
  scanf("%d%d%d", &w, &h, &n);
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j < 4; ++j) {
      scanf("%d", &building[i][j]);
    }
  }
  d[0][n + 1] = d[n + 1][0] = w;
  for (int i = 1; i <= n; ++i) {
    d[0][i] = d[i][0] = building[i][0];
    d[n + 1][i] = d[i][n + 1] = w - building[i][2] - 1;
  }
  for (int i = 1; i <= n; ++i) {
    for (int j = i + 1; j <= n; ++j) {
      d[i][j] = d[j][i] = std::min(Distance(i, j), Distance(j, i));
    }
  }
  memset(b, 0, sizeof(b));
  memset(dis, 63, sizeof(dis));
  que.push(0);
  b[0] = true;
  dis[0] = 0;
  while (!que.empty()) {
    int p = que.front();
    que.pop();
    b[p] = false;
    for (int i = 0; i <= n + 1; ++i) {
      if (dis[p] + d[p][i] < dis[i]) {
        dis[i] = dis[p] + d[p][i];
        if (!b[i]) {
          que.push(i);
          b[i] = true;
        }
      }
    }
  }
  return dis[n + 1];
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; ++i)
    printf("Case #%d: %d\n", i, Work());
  return 0;
}
