#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main ()
{
  freopen ("in.txt", "r", stdin);
  freopen ("ou.txt", "w", stdout);

  int T, N, M;
  int mat[100][100], x[100], y[100];

  scanf ("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf ("%d%d", &N, &M);
    fill (x, x + N, 0);
    fill (y, y + M, 0);
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        scanf ("%d", mat[i] + j);
        if (mat[i][j] > x[i]) x[i] = mat[i][j];
        if (mat[i][j] > y[j]) y[j] = mat[i][j];
      }
    }
    int res = 1;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (mat[i][j] < x[i] && mat[i][j] < y[j]) {
            res = 0;
        }
      }
    }
    printf ("Case #%d: ", t);
    if (res) printf ("YES\n"); else printf ("NO\n");
  }
}
