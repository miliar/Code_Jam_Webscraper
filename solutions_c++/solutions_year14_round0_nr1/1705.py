#include <stdio.h>
#include <string.h>
#define MAXN 4

int carda[MAXN][MAXN];
int cardb[MAXN][MAXN];

int main() {
  int t, rowa, rowb;
  scanf("%d", &t);
  for (int cases = 1; cases <= t; ++ cases) {
    scanf("%d", &rowa);
    
    for (int i = 0; i < MAXN; ++ i)
      for (int j = 0; j < MAXN; ++ j)
        scanf("%d", &carda[i][j]);

    scanf("%d", &rowb);
    for (int i = 0; i < MAXN; ++ i)
      for (int j = 0; j < MAXN; ++ j)
        scanf("%d", &cardb[i][j]);

    int findCount = 0, findVal;
    for (int i = 0; i < 4; ++ i)
      for (int j = 0; j < 4; ++ j)
        if (carda[rowa - 1][i] == cardb[rowb - 1][j]) {
          findCount ++;
          findVal = carda[rowa - 1][i];
        }

    printf("Case #%d: ", cases);
    if (findCount == 0) printf("Volunteer cheated!\n");
    else if (findCount == 1) printf("%d\n", findVal);
    else printf("Bad magician!\n");
  }
  return 0;
}
