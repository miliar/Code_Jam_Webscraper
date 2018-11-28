#include <cstdio>
#include <cstring>

const int MAXDIM = 105;

int T, N, M;
int lawn[MAXDIM][MAXDIM], lrow[MAXDIM], lcol[MAXDIM];

inline int max(int a, int b) {
  return (a > b) ? a : b; 
}

int main() {

  scanf("%d", &T);

  for (int tt = 1; tt <= T; tt++) {

    memset(lrow, -1, sizeof(lrow));
    memset(lcol, -1, sizeof(lcol));

    scanf("%d %d", &N, &M);

    for (int i = 0; i < N; i++)
      for (int j = 0; j < M; j++) {
        scanf("%d", &lawn[i][j]);
        lrow[i] = max(lrow[i], lawn[i][j]);
        lcol[j] = max(lcol[j], lawn[i][j]);
      }

    bool ok = true;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++) 
          if (lawn[i][j] < lrow[i] && lawn[i][j] < lcol[j]) {
            ok = false;
            goto sol;
        }

  sol:
    printf("Case #%d: %s\n", tt, ok ? "YES" : "NO");  
  }

  return 0;
}
