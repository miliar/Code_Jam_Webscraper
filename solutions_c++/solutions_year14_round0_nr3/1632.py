#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

char board[100][100];

void blit(int r, int c) {
  for (int rr = 0; rr < r; ++rr) {
    for (int cc = 0; cc < c; ++cc) {
      board[rr][cc] = '.';
    }
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int R, C, M;
    scanf("%d %d %d", &R, &C, &M);
    int N = R * C - M;

    bool possible = false;
    memset(board, '*', sizeof(board));
    for (int r = 1; r <= R; ++r) {
      for (int c = 1; c <= C; ++c) {
        int area = r * c;
        if (area > N) {
          continue;
        }
        int nn = N;
        nn -= area;

        if (nn >= r + c) {
          continue;
        }

        if (r == 1) {
          if (R != 1 || nn != 0) {
            continue;
          } else {
            possible = true;
            blit(r, c);
            goto done;
          }
        }
        if (c == 1) {
          if (C != 1 || nn != 0) {
            continue;
          } else {
            possible = true;
            blit(r, c);
            goto done;
          }
        }

        if (nn == 0) {
          possible = true;
          blit(r, c);
          goto done;
        }

        if (r == R && c < C) {
          if (nn >= 2 && nn <= R) {
            possible = true;
            blit(r, c);
            for (int i = 0; i < nn; ++i) {
              board[i][c] = '.';
            }
            goto done;
          } else {
            continue;
          }
        }

        if (c == C && r < R) {
          if (nn >= 2 && nn <= C) {
            possible = true;
            blit(r, c);
            for (int i = 0; i < nn; ++i) {
              board[r][i] = '.';
            }
            goto done;
          } else {
            continue;
          }
        }

        if (nn == 1) {
          continue;
        }
        if (nn == 3 && r < 3 && c < 3) {
          continue;
        }

        possible = true;
        blit(r, c);
        if (nn == 3) {
          board[r][0] = board[r][1] = board[r][2] = '.';
          goto done;
        }

        board[r][0] = board[r][1] = '.';
        nn -= 2;
        int col = std::min(r, nn);
        nn -= col;
        for (int i = 0; i < col; ++i) {
          board[i][c] = '.';
        }
        for (int i = 0; i < nn; ++i) {
          board[r][i+2] = '.';
        }
        goto done;
      }
    }
    done:
    printf("Case #%d:\n", t);
    if (possible || N == 1) {
      board[0][0] = 'c';
      for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
          putchar(board[r][c]);
        }
        putchar('\n');
      }
    } else {
      printf("Impossible\n");
    }
  }
}
