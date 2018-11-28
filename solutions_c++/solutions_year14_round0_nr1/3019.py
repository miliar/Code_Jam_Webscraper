#include <stdio.h>

using namespace std;


int main()
{
  int T;

  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small-attempt0.out", "w", stdout);

  scanf("%d", &T);

  int first_ans, second_ans;
  int first[4][4], second[4][4];

  for (int cn = 1; cn <= T; cn++) {
    scanf("%d", &first_ans);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%d", &first[i][j]);
      }
    }
    scanf("%d", &second_ans);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%d", &second[i][j]);
      }
    }

    first_ans--;
    second_ans--;

    int out = 0, cnt = 0;
    for (int i = 0; i < 4; i++) {
      int ans = first[first_ans][i];
      for (int j = 0; j < 4; j++) {
        if (ans == second[second_ans][j]) {
          out = ans;
          cnt++;
        }
      }
    }

    printf("Case #%d: ", cn);
    if (cnt == 1) {
      printf("%d\n", out);
    } else if (cnt == 0) {
      printf("Volunteer cheated!\n");
    } else {
      printf("Bad magician!\n");
    }
  }
  return 0;
}