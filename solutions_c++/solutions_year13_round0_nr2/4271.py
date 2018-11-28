#include <stdio.h>

#define MIN(x,y) ((x)<(y)?(x):(y))

int main() {

  int lawn[101][101];
  int T;

  scanf("%d", &T);

  for (int t = 0; t < T; t++) {
    int N, M;
    bool satisfied[101][101];

    scanf("%d%d", &N, &M);

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        satisfied[i][j] = false;
        scanf("%d", &lawn[i][j]);
      }
    }

    for (int h = 1; h <= 100; h++) {
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
          if (!satisfied[i][j] && lawn[i][j] != h) {
            goto nextrow;
          }
        }

        for (int j = 0; j < M; j++) {
          satisfied[i][j] = true;
        }
nextrow:
        ;
      }

      for (int j = 0; j < M; j++) {
        for (int i = 0; i < N; i++) {
          if (!satisfied[i][j] && lawn[i][j] != h) {
            goto nextcol;
          }
        }

        for (int i = 0; i < N; i++) {
          satisfied[i][j] = true;
        }
nextcol:
        ;
      }
    }

    bool ok = true;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (!satisfied[i][j]) {
          ok = false;
          goto end;
        }
      }
    }

end:

    printf("Case #%d: %s\n", t + 1, ok ? "YES" : "NO");
  }

  return 0;
}
