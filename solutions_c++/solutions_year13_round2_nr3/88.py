#include <stdio.h>
#include <memory.h>
#include <string.h>

char word[555555][42];
int len[555555];
int f[5555][6];
char s[5555];

int main() {
  freopen("dict", "r", stdin);
  int m = 0;
  while (scanf("%s", word[m]) == 1) {
    len[m] = strlen(word[m]);
    m++;
  }
  fclose(stdin);
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    scanf("%s", s);
    int n = strlen(s);
    memset(f, 50, sizeof(f));
    f[0][0] = 0;
    for (int i=0;i<n;i++) {
      fprintf(stderr, "%d\n", i);
      for (int j=0;j<=4;j++)
        if (f[i][j] < 1000000) {
          for (int k=0;k<m;k++) {
            if (i+len[k] > n) continue;
            int need = j, ok = 1, ft = f[i][j];
            for (int q=0;q<len[k];q++)
              if (word[k][q] != s[i+q]) {
                if (need > 0) {
                  ok = 0;
                  break;
                }
                need = 4;
                ft++;
              }
              else need--;
            if (need < 0) need = 0;
            if (ok && ft < f[i+len[k]][need]) {
              f[i+len[k]][need] = ft;
            }
          }
        }
    }
    int ans = 10000000;
    for (int j=0;j<=4;j++)
      if (f[n][j] < ans) ans = f[n][j];
    printf("%d\n", ans);
    fflush(stdout);
  }
  return 0;
}
