#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

#define LOG(x) cerr << #x << " = " << (x) << "\n"

typedef long long llint;
typedef pair<int,int> pii;
const int MAXN = 110;
int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };

int r, c;
char a[MAXN][MAXN];

int calc(int y, int x) {
  if (a[y][x] == '.') return 0;
  int dir = string("<>^v").find(a[y][x]);

  int ny = y + dy[dir];
  int nx = x + dx[dir];
  while (ny >= 0 && ny < r && nx >= 0 && nx < c) {
    if (a[ny][nx] != '.') return 0;
    ny += dy[dir];
    nx += dx[dir];
  }

  for (int i = 0; i < 4; ++i) {
    int ny = y + dy[i];
    int nx = x + dx[i];
    while (ny >= 0 && ny < r && nx >= 0 && nx < c) {
      if (a[ny][nx] != '.') return 1;
      ny += dy[i];
      nx += dx[i];
    }
  }

  return -1;
}

void solve() {
  scanf("%d%d", &r, &c);
  for (int i = 0; i < r; ++i)
    scanf("%s", a[i]);

  int ans = 0;
  for (int i = 0; i < r; ++i)
    for (int j = 0; j < c; ++j) {
      int t = calc(i, j);
      if (t == -1) {
        printf("IMPOSSIBLE\n");
        return;
      }
      ans += t;
    }

  printf("%d\n", ans);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; ++i) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}

