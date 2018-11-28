#include <cstdio>

int main()
{

  int A[5][5];
  int B[5][5];

  int T;
  scanf("%d", &T);

  for (int Ti = 1; Ti <= T; Ti++) {
    int q1, q2;

    scanf("%d", &q1);
    for (int i = 1; i <= 4; i++) {
      scanf("%d %d %d %d", &A[i][1], &A[i][2], &A[i][3], &A[i][4]);
    }

    int S[5] = {0, A[q1][1], A[q1][2], A[q1][3], A[q1][4]};

    scanf("%d", &q2);
    for (int i = 1; i <= 4; i++) {
      scanf("%d %d %d %d", &B[i][1], &B[i][2], &B[i][3], &B[i][4]);
    }

    int tag[5] = {0};

    int ans = 0;
    for (int k = 1; k <= 4; k++) {
      int n = S[k];
      for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
          if (n == B[i][j]) {
            tag[i]++;
            if (i == q2) ans = B[i][j];
          }
        }
      }
    }

    if (tag[q2] > 1) {
      printf("Case #%d: Bad magician!\n", Ti);
    } else if (tag[q2] == 0) {
      printf("Case #%d: Volunteer cheated!\n", Ti);
    } else {
      printf("Case #%d: %d\n", Ti, ans);
    }

  }
  return 0;
}
