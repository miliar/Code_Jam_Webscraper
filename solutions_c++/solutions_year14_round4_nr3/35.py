#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <climits>
#include <cassert>

#define INF (INT_MAX/2)

#define MAXB 10
#define MAXW 100
#define MAXH 500

typedef long long lint;

using namespace std;

int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};

int w, h;
int field[MAXH][MAXW];

bool canmove(int y, int x, int d) {
  y += dy[d], x += dx[d];
  return 0 <= y && y < h && 0 <= x && x < w && field[y][x] != 1;
}

int go(int origx) {
  const int origy = h-1;

  int y = origy, x = origx, d = 0, nmove = 0;

  if (field[y][x] == 1) return 0;

  vector <pair <int, int> > path;

  while (y != 0) {
    if (y == origy && x == origx && nmove) return 0;
    field[y][x] = 2;

    path.push_back(make_pair(y, x));
    
    int delta;
    for (delta = -1; delta < 3; delta++)
      if (canmove(y, x, (d + delta + 8)%4)) {
	d = (d + delta + 8) % 4;
	y += dy[d], x += dx[d];
	break;
      }

    if (delta == 3 && !nmove) return 0;
    assert(delta != 3);

    nmove++;
  }

  for (int i = 0; i < (int)path.size(); i++) {
    int y = path[i].first, x = path[i].second;
    field[y][x] = 1;
  }

  return 1;
}

int main() {
  int ntest;

  scanf("%d", &ntest);

  for (int t = 0; t < ntest; t++) {
    int nb;

    scanf("%d %d %d", &w, &h, &nb);

    memset(field, 0, sizeof(field));

    for (int b = 0; b < nb; b++) {
      int x0, y0, x1, y1;
      scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
      if (x0 > x1) swap(x0, x1);
      if (y0 > y1) swap(y0, y1);
      for (int y = y0; y <= y1; y++)
	for (int x = x0; x <= x1; x++)
	  field[y][x] = 1;
    }

    int result = 0;

    for (int x = 0; x < w; x++) result += go(x);

    printf("Case #%d: %d\n", t+1, result);    
  }

  return 0;
}
