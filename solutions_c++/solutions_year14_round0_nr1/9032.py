#include <stdio.h>

int main() {
  int T, n, m;
  scanf("%d", &T);
  int i, j, k;
  int a, b, res = -1;
  int arr[4];
  bool flag[17];
  for (i = 1;i <= T; ++i) {
    res = -1;
    for (j = 1;j < 17; ++j) flag[j] = false;
    scanf("%d", &a);
    for (j = 1;j <= 4; ++j) {
      scanf("%d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3]);
      if (j == a) {
        for (k = 0;k < 4; ++k) flag[arr[k]] = true;
      }
    }
    scanf("%d", &b);
    for (j = 1;j <= 4; ++j) {
      scanf("%d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3]);
      if (j == b) {
        for (k = 0;k < 4; ++k) {
          if (flag[arr[k]]) {
            if (res != -1) {
              res = -2;
            } else {
              res = arr[k];
            }
          } 
        }
      }
    }
    printf("Case #%d: ", i); 
    if (res == -2) 
      printf("Bad magician!\n"); 
    else if (res == -1) 
      printf("Volunteer cheated!\n");
    else 
      printf("%d\n", res);
  }
  return 0;
}

