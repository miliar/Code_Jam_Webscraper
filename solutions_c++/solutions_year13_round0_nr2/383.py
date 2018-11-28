#include <stdio.h>

int a[111][111], row[111], col[111];

int main() {
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i=0;i<n;i++)
      for (int j=0;j<m;j++) scanf("%d", &a[i][j]);
    for (int i=0;i<n;i++) row[i] = 0;
    for (int i=0;i<m;i++) col[i] = 0;
    for (int i=0;i<n;i++)
      for (int j=0;j<m;j++) {
        if (a[i][j] > row[i]) row[i] = a[i][j];
        if (a[i][j] > col[j]) col[j] = a[i][j];
      }
    int ok = 1;
    for (int i=0;i<n;i++)
      for (int j=0;j<m;j++)
        if (a[i][j] != row[i] && a[i][j] != col[j]) ok = 0;
    printf("Case #%d: ", qq);
    if (ok) puts("YES");
    else puts("NO");
  }
  return 0;
}
