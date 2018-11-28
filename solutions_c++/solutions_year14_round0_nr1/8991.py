#include <iostream>
#include <cstdio>

using namespace std;

int T;

int a[4][4];
int b[4][4];
int r1;
int r2;

int main() {
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    scanf("%d", &r1);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%d", &a[i][j]);
      }
    }

    scanf("%d", &r2);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%d", &b[i][j]);
      }
    }

    int cnt = 0;
    int pos = 0;
    for (int i = 0; i < 4; i++) {
      bool flag = 0;
      for (int j = 0; j < 4; j++) {
        if (a[r1-1][i] == b[r2-1][j]) {
          flag = 1;
          pos = i;
        }
      }
      if (flag) {
        cnt++;
      }
    }
    printf("Case #%d: ", t);

    if (cnt == 1) {
      printf("%d", a[r1-1][pos]);
    } else if (cnt > 1) {
      printf("Bad magician!");
    } else {
      printf("Volunteer cheated!");
    }

    printf("\n");
  }

}
