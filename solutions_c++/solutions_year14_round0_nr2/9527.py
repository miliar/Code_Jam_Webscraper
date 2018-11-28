#include <stdio.h>

void f1() {
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; i++) {
    int row1;
    scanf("%d", &row1);
    --row1;
    int mat1[4][4];
    for (int j = 0; j < 4; j++) {
      scanf("%d %d %d %d", &mat1[j][0], &mat1[j][1], &mat1[j][2], &mat1[j][3]);
    }
    int row2;
    scanf("%d", &row2);
    --row2;
    int mat2[4][4];
    for (int j = 0; j < 4; j++) {
      scanf("%d %d %d %d", &mat2[j][0], &mat2[j][1], &mat2[j][2], &mat2[j][3]);
    }
    int opts1 = 0;
    int opts2 = 0;
    for (int j = 0; j < 4; j++) {
      opts1 |= 1 << (mat1[row1][j]);
      opts2 |= 1 << (mat2[row2][j]);
    }
    opts1 &= opts2;
    printf("Case #%d: ", i);
    if (opts1 == 0) {
      printf("Volunteer cheated!\n");
    } else if ((opts1 & (opts1 - 1)) == 0) {
      for (int j = 0; j < 4; j++) {
        if (opts1 & (1 << (mat1[row1][j]))) {
          printf("%d\n", mat1[row1][j]);
          break;
        }      
      }
    } else {
      printf("Bad magician!\n");
    }
  }
}

void f2() {
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; i++) {
    double c, f, x;
    scanf("%lf %lf %lf", &c, &f, &x);
    double res = 0;
    double speed = 2.0f;
    while (true) {
      double opt1 = x / speed;
      double opt2 = c / speed + x / (speed + f);
      if (opt1 < opt2) {
        res += opt1;
        break;
      } else {
        res += c / speed;
        speed += f;
      }
    }
    printf("Case #%d: %.7lf\n", i, res);
  }    
}

int main() {
  f2();
}