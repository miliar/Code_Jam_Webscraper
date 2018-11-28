#include <cstdio>
#include <cstdlib>
int t;
int a[4], b[4];
int qa, qb;
int equ, tmp;
int main() {
  scanf("%d", &t);
  for (int k = 1; k <= t; ++k) {
    scanf("%d", &qa);
    for (int i = 1; i <= 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        scanf("%d", &tmp);
        if (i == qa)
          a[j] = tmp;
      }
    }
    scanf("%d", &qb);
    for (int i = 1; i <= 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        scanf("%d", &tmp);
        if (i == qb)
          b[j] = tmp;
      }
    }
    equ = 0;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        if (a[i] == b[j]) {
          equ++;
          tmp = a[i];
          break;
        }
      }
    }
    printf("Case #%d: ", k);
    if (equ == 1)
      printf("%d\n", tmp);
    else if (equ == 0)
      printf("Volunteer cheated!\n");
    else
      printf("Bad magician!\n");
  }
}