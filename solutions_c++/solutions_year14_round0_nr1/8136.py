#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int a[4][4], b[4][4], answer1, answer2;
int main() {
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int totCas;
  scanf("%d", &totCas);
  for (int cas = 1; cas <= totCas; cas++) {
    scanf("%d", &answer1);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%d", &a[i][j]);
      }
    }
    scanf("%d", &answer2);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%d", &b[i][j]);
      }
    }

    int ans, cnt = 0;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        if (a[answer1 - 1][i] == b[answer2 - 1][j]) {
          ans = a[answer1 - 1][i];
          cnt++;
        }
      }
    }
    printf("Case #%d: ", cas);
    if (cnt == 0) {
      printf("Volunteer cheated!\n");
    } else if (cnt == 1) {
      printf("%d\n", ans);
    } else {
      printf("Bad magician!\n");
    }
  }
  return 0;
}
