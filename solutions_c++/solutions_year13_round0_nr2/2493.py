#include <cstdio>
#include <set>

int map[100][100];

int n, m;

int sum_lane(int x, int y, int dx, int dy, int k) {
  for (int i = x, j = y; i < n && j < m; i += dx, j += dy)
    if (map[i][j] > k) 
      return 0;

  int cnt = 0;

  for (int i = x, j = y; i < n && j < m; i += dx, j += dy)
    if (map[i][j] == k) {
      cnt += 1;
      map[i][j] = -1;
    }
  
  return cnt;
}

bool chk(int k) {

  int cnt = 0;

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      if (map[i][j] == k)
	cnt += 1;

  for (int i = 0; i < n; ++i)
    cnt -= sum_lane(i, 0, 0, 1, k);

  for (int i = 0; i < m; ++i)
    cnt -= sum_lane(0, i, 1, 0, k);

  return cnt == 0;
}

bool jizz() {
  scanf("%d%d", &n, &m);

  std::set<int> S;

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      scanf("%d", &map[i][j]), S.insert(map[i][j]);

  for (std::set<int>::iterator it = S.begin(); it != S.end(); ++it)
    if (!chk(*it)) 
      return false;

  return true;
}

int main() {

  int t;
  scanf("%d", &t);

  for (int i = 1; i <= t; ++i)
    printf("Case #%d: %s\n", i, jizz() ? "YES" : "NO");

  return 0;
}
