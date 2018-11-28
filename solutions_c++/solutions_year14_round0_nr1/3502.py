#include <stdio.h>
#include <algorithm>

int main() {
  int round_1[4][4];
  int round_1_answer;
  int round_2[4][4];
  int round_2_answer;
  int intersection[4];

  int n_round, num;

  scanf("%d", &n_round);
  for (int n = 1; n < n_round + 1; ++n) {
    scanf("%d", &round_1_answer);
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        scanf("%d", &num);
        round_1[i][j] = num;
      }
    }
    for (int i = 0; i < 4; ++i) {
      std::sort(round_1[i], round_1[i] + 4);
    }

    scanf("%d", &round_2_answer);
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        scanf("%d", &num);
        round_2[i][j] = num;
      }
    }
    for (int i = 0; i < 4; ++i) {
      std::sort(round_2[i], round_2[i] + 4);
    }

    int *it = std::set_intersection(round_1[round_1_answer - 1],
                                    round_1[round_1_answer - 1] + 4,
                                    round_2[round_2_answer - 1],
                                    round_2[round_2_answer - 1] + 4,
                                    intersection);

    if (it - intersection == 1) {
      printf("Case #%d: %d\n", n, intersection[0]);
    } else if (it - intersection > 1) {
      printf("Case #%d: Bad magician!\n", n);
    } else {
      printf("Case #%d: Volunteer cheated!\n", n);
    }
  }
}