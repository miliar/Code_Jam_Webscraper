#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

bool table[5][5][5];

int main(void) {
  table[2][1][1] = true;
  table[2][1][3] = true;
  table[2][3][1] = true;
  table[2][3][3] = true;
  for(int i = 1; i <= 4; ++i)
    for(int j = 1; j <= 4; ++j) {
      table[3][i][j] = true;
      table[4][i][j] = true;
    }
  table[3][2][3] = false;
  table[3][3][2] = false;
  table[3][3][4] = false;
  table[3][4][3] = false;
  table[3][3][3] = false;
  //table[3][4][4] = false;
  table[4][3][4] = false;
  table[4][4][3] = false;
  table[4][4][4] = false;

  int T;
  scanf("%d", &T);
  for(int kase = 1; kase <= T; ++kase) {
    int X, R, C;
    scanf("%d %d %d", &X, &R, &C);
    printf("Case #%d: ", kase);
    if(!table[X][R][C])
      printf("GABRIEL\n");
    else
      printf("RICHARD\n");
  }
  return 0;
}
