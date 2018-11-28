#include <cstdio>
#pragma warning(disable : 4996)

using namespace std;

int M, R, C;

bool check(int r, int c, int m, char board[50][50]) {
  if (r * c <= m) return false;
  if (r == 1 && c == 1) {
    if (m == 0) {
      board[0][0] = 'c';
      return true;
    }
    else return false;
  }
  if (r + c - 1 - m >= 4 && r - m <= 1 && c -m <= 1&& r >= 3 && c >= 3) {
    for (int i = 2; i < r && m > 0; i++) {
      board[i][c - 1] = '*';
      m--;
    }
    for (int i = c - 2; i >= 2 && m > 0; i--) {
      board[r - 1][i] = '*';
      m--;
    }
    board[0][0] = 'c';
    return true;
  }
  if (m < 0) {
    if (m == -1) return false;
    if (r != R && r <= 1) return false;
    if (c != C && c <= 1) return false;
    if (r >= -m && c < C) {
      for (int i = 0; i < -m; i++) {
        board[i][c] = '.';
      }
      board[0][0] = 'c';
      return true;
    }
    else if(c >= -m && r < R) {
      for (int i = 0; i < -m; i++) {
        board[r][i] = '.';
      }
      board[0][0] = 'c';
      return true;
    }
    else {
      return false;
    }
  }
  else if (m == 0) {
    if (r != R && r == 1) return false;
    if (c != C && c == 1) return false;
    if (r >= 2 && c >= 2 ||
      c == C && c == 1 || r == R && r == 1) {
      board[0][0] = 'c';
      return true;
    }
    else return false;
  }
  for (int i = 0; i < c; i++) board[r - 1][i] = '*';
  if (check(r - 1, c, m - c, board)) return true;
  for (int i = 0; i < c; i++) board[r - 1][i] = '.';
  for (int i = 0; i < r; i++) board[i][c - 1] = '*';
  if (check(r, c - 1, m - r, board)) return true;
  for (int i = 0; i < r; i++) board[i][c - 1] = '.';
  return false;
}

int main(void) {
  int T;
  scanf("%d", &T);
  for (int case_n = 1; case_n <= T; case_n++) {
    scanf("%d%d%d", &R, &C, &M);
    int cells = R * C;
    printf("Case #%d:\n", case_n);
    char board[50][50];
    for (int i = 0; i < 50; i++) {
      for (int j = 0; j < 50; j++) {
        board[i][j] = '.';
      }
    }
    //printf("R:%d C:%d M:%d\n", R, C, M);
    if (check(R, C, M, board)) {
      for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
          putchar(board[i][j]);
        }
        putchar('\n');
      }
    }
    else {
      puts("Impossible");
    }
  }
  return 0;
}