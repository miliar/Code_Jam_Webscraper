#include <cstdio>

int v[30];

int main() {
  int t, n, d;
  scanf("%d", &t);
  for (int cas = 1; cas <= t; cas++) {
    int k = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
      scanf("%d", &v[i]);


    printf("Case #%d:", cas);
    int max1 = -1, max2 = -1, max3 = -1;
    int i1 = 0, i2 = 0, i3 = 0;
    bool started = false;
    while (max1 != 0) {
      if (started)
        if (max1 == 1 && max2 == 1 && max3 == 1) {
          v[i1]--;
          printf(" %c", 'A' + i1);
        } else if (max1 == 2 && max2 == 1) {
          v[i1]--;
          printf(" %c", 'A' + i1);
        } else if (max1 >= 1 && max2 >= 1) {
          v[i1]--;
          v[i2]--;
          printf(" %c%c", 'A' + i1, 'A' + i2);
        } else {
          v[i1]--;
          printf(" %c", 'A' + i1);
        }
      started = true;
      max1 = max2 = max3 = -1;
      i1 = i2  = i3 = 0;
      for (int i = 0; i < n; i++) {
        if (v[i] > max1) {
          max3 = max2; max2 = max1; max1 = v[i];
          i3 = i2; i2 = i1; i1 = i;
        } else if (v[i] > max2) {
          max3 = max2; max2 = v[i];
          i3 = i2; i2 = i;
        } else if (v[i] > max3)
          max3 = v[i];
          i3 = i;
      }
    }
    printf("\n");
  }
  return 0;
}
