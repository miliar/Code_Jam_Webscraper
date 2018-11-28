#include <cstdio>
#include <memory.h>

struct Answer {
};

int main() {
  int nCase;
  int row;
  int cards[4][4];
  bool bad[17];
  scanf("%d", &nCase);

  for (int iCase = 0; iCase < nCase; ++iCase) {
    memset(bad, 0, sizeof(bad));

    for (int i = 0; i < 2; ++i) {
      scanf("%d", &row);
      --row;
      for(int j = 0; j < 4; ++j) {
        for(int k = 0; k < 4; ++k) {
          scanf("%d", &cards[j][k]);
          if (row != j) {
            bad[cards[j][k]] = true;
          }
        }
      }
    }

    int sol = -1;
    for (int i = 1; i <= 16; ++i) {
      if (!bad[i]) {
        if (sol == -1) sol = i;
        else {
          sol = -2;
          break;
        }
      }
    }
    if (sol == -1) {
      printf("Case #%d: Volunteer cheated!\n", iCase + 1);
    }
    else if (sol == -2) {
      printf("Case #%d: Bad magician!\n", iCase + 1);
    }
    else {
      printf("Case #%d: %d\n", iCase + 1, sol);
    }
  }
  
  return 0;
}
