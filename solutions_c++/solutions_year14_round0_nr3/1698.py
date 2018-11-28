#include <cstdio>
#include <algorithm>

#define REP(i, n) for(int i = 0; i < (n); i++)

int di[] = { 0, 0, -1, 1, -1, 1, -1, 1 };
int dj[] = { -1, 1, 0, 0, -1, 1, 1, -1 };
  
char grid[20][20];

bool visited[20][20];
void test(int ir, int jc, int r, int c) {
  visited[ir][jc] = true;

  bool isZero = true;
  for (int d = 0; d < 8; d++) {
    int ni = ir + di[d], nj = jc + dj[d];
    if (ni >= 0 && ni < r && nj >= 0 && nj < c &&
        grid[ni][nj] == '*') {
      isZero = false;
      break;
    }
  }

  if (isZero) {
    for (int d = 0; d < 8; d++) {
      int ni = ir + di[d], nj = jc + dj[d];
      if (ni >= 0 && ni < r && nj >= 0 && nj < c &&
          grid[ni][nj] == '.' && !visited[ni][nj]) {
        test(ni, nj, r, c);
      }
    }
  }
}

bool can_win(int ir, int jc, int r, int c) {
  REP(i, r) REP(j, c) {
    visited[i][j] = false;
  }

  test(ir, jc, r, c);

  REP(i, r) REP(j, c) {
    if (grid[i][j] == '.' && !visited[i][j])
      return false;
  }

  return true;
}

bool brute(int ir, int jc, int r, int c, int m) {
  if (m == 0) {
    REP(i, r) REP(j, c) {
      if (grid[i][j] == '.' && can_win(i, j, r, c)) {
        grid[i][j] = 'c';
        return true;
      }
    }

    return false;
  }

  if (jc >= c) {
    jc = 0;
    ir++;
  }

  if (ir >= r) return false;

  grid[ir][jc] = '*';
  if (brute(ir, jc + 1, r, c, m - 1)) return true;
  grid[ir][jc] = '.';
  if (brute(ir, jc + 1, r, c, m)) return true;
  return false;
}

void docase(int tcase) {
  int r, c, m;
  scanf("%d %d %d", &r, &c, &m);

  REP(i, r) REP(j, c) {
    grid[i][j] = '.';
  }

  // special cases
  if (r * c - m == 1) {
    printf("Case #%d:\n", tcase);
    REP(i, r) {
      REP(j, c) {
        if (i == r - 1 && j == c - 1)
          printf("c");
        else
          printf("*");
      }
      printf("\n");
    }
    return;
  }

  if (brute(0, 0, r, c, m)) {
    printf("Case #%d:\n", tcase);
    REP(i, r) {
      REP(j, c) {
        printf("%c", grid[i][j]);
      }
      printf("\n");
    }
  } else {
    printf("Case #%d:\nImpossible\n", tcase);
  }
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; i++) docase(i+1);
}
