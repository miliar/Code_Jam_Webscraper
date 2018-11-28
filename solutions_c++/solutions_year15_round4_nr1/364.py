#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int r, c;
char grid[104][104];

bool checkImposible(int i, int j) {
  if (grid[i][j] == '.') return false;
  int x = 0;
  for (int k = 0; k < r; ++k)
    if (grid[k][j] != '.') ++x;
  for (int k = 0; k < c; ++k)
    if (grid[i][k] != '.') ++x;
  return x == 2;
}

bool checkImposible() {
  for (int i = 0; i < r; ++i) {
    for (int j = 0; j < c; ++j) {
      if (checkImposible(i, j)) return true;
    }
  }
  return false;
}

bool change(int i, int j, char x) {
  if (grid[i][j] == '.') return false;
  if (grid[i][j] != x) return true;
  grid[i][j] = 'X';
  return true;
}

void printGrid() {
  printf("\n");
  for (int i = 0; i < r; ++i) printf("%s\n", grid[i]);
  printf("\n");
}

int change() {
  int ret = 0;
  for (int i = 0; i < r; ++i) {
    for (int j = 0; j < c; ++j) {
      if (change(i, j, '<')) break;
    }
    for (int j = c - 1; j >= 0; --j) {
      if (change(i, j, '>')) break;
    }
  }
  for (int j = 0; j < c; ++j) {
    for (int i = 0; i < r; ++i) {
      if (change(i, j, '^')) break;
    }
    for (int i = r - 1; i >= 0; --i) {
      if (change(i, j, 'v')) break;
    }
  }
  for (int i = 0; i < r; ++i) 
    ret += count(grid[i], grid[i] + c, 'X');
  return ret;
}

void solve() {
  scanf("%d%d", &r, &c);
  for (int i = 0; i < r; ++i) {
    scanf("%s", grid[i]);
  }
  if (checkImposible()) {
    printf("IMPOSSIBLE\n");
    return;
  }
  printf("%d\n", change());
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
