#include <stdio.h>
#include <assert.h>
#include <cstring>

int main (void) {
  int T;
  int scanned = scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    bool possible[16];
    memset(possible, true, sizeof(bool) * 16);
    for (int i = 0; i < 2; i++) {
      int k;
      scanf("%d", &k);
      for (int j = 1; j <= 4; j++) {
        for (int l = 0; l < 4; l++) {
          int tmp;
          scanf("%d", &tmp);
          if (j != k) {
            possible[tmp-1] = false;
          }
        }
      }
    }
    int k = -1;
    for (int i = 0; i < 16; i++) {
      if (possible[i]) {
        if (k == -1) {
          k = i;
        } else {
          k = -2;
          break;
        }
      }
    }
    if (k == -1) {
      printf("Case #%d: Volunteer cheated!\n", currentcase);
    } else if (k == -2) {
      printf("Case #%d: Bad magician!\n", currentcase);
    } else {
      printf("Case #%d: %d\n", currentcase, k+1);
    }
  }
  return 0;
}
