#include <stdio.h>
#include <string.h>
int col[200], row[200];
int lawn[110][110];

int main () {
    int kase, h = 1;
    int n, m;
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d %d", &n, &m);
          memset(row,0,sizeof(row));
          memset(col,0,sizeof(col));
          for (int i = 0; i < n; ++i) {
              for (int j = 0; j < m; ++j) {
                  scanf("%d", &lawn[i][j]);
                  if (row[i] < lawn[i][j]) {
                     row[i] = lawn[i][j];
                  }
                  if (col[j] < lawn[i][j]) {
                     col[j] = lawn[i][j];
                  }
              }
          }
          bool yes= true;
          for (int i = 0; i < n; ++i) {
              for (int j = 0; j < m; ++j) {
                  if (lawn[i][j] == row[i] || lawn[i][j] == col[j]) continue;
                  yes = false;
                  break;
              }
              if (!yes) break;
          }
          printf("Case #%d: ",h++);
          if (yes) {
             printf("YES\n");
          }
          else {
               printf("NO\n");
          }
    }
    return 0;
}
