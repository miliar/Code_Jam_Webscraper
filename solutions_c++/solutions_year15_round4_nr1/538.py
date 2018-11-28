#include <iostream>
#include <string>
#include <list>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

#define FOR(i, n) for (int i = 0; i < n ; ++ i)

char grid[100][100];
int n, m;

bool safe[100][100][5];

int deltas[4][2] = {
  {1, 0},
  {-1, 0},
  {0, 1},
  {0, -1}
};

bool valid(int i, int j, int k, int d) {
  int i2 = i+deltas[k][0]*d;
  int j2 = j+deltas[k][1]*d;

  return i2 >= 0 && j2 >= 0 && i2 < n && j2 < m;
}

int direction(int i, int j) {
  switch (grid[i][j]) {
    case 'v': return 0;
    case '^': return 1;
    case '>': return 2;
    case '<': return 3;
  }

  return -1;
}

void solve(int testcase) {
  cin >> n >> m;
  memset(safe, 0, sizeof(safe));

  FOR(i, n) FOR(j, m) cin >> grid[i][j];

  FOR(i, n)
    FOR(j, m)
      FOR(k, 4)
        for (int d = 1; valid(i, j, k, d); d++)
          if (grid[i+deltas[k][0]*d][j+deltas[k][1]*d] != '.') {
            safe[i][j][k] = true;
            safe[i][j][4] = true;
            break;
          }

  int best = 0;
  bool possible = true;
  FOR(i, n) FOR(j, m)
    if (grid[i][j] != '.' && !safe[i][j][4]) possible = false;

  if (possible)
    FOR(i, n)
      FOR(j, m)
        if (grid[i][j] != '.' && !safe[i][j][direction(i,j)]) best++;

  if (!possible)
  printf("Case #%d: IMPOSSIBLE\n", testcase);
  else
  printf("Case #%d: %d\n", testcase, best);
}

int main() {
  int T;
  cin >> T;
  FOR(i, T) solve(i+1);
  return 0;
}
