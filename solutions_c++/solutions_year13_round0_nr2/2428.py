/*
 * Lawnmower.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: admin
 */

#include <cstdio>

#define SIZE 100

bool mow(int lawn[SIZE][SIZE], int N, int M) {
  int hV[SIZE] = { 0 };
  int hH[SIZE] = { 0 };

  for (int n = 0; n < N; ++n) {
    for (int m = 0; m < M; ++m) {
      if (lawn[n][m] > hV[m])
        hV[m] = lawn[n][m];
      if (lawn[n][m] > hH[n])
        hH[n] = lawn[n][m];
    }
  }

  for (int n = 0; n < N; ++n) {
    for (int m = 0; m < M; ++m) {
      int min = hV[m] < hH[n] ? hV[m] : hH[n];
      if (lawn[n][m] != min)
        return false;
    }
  }

  return true;
}

int main() {
  int numTest;
  scanf("%d", &numTest);
  int lawn[SIZE][SIZE];

  for (int t = 1; t <= numTest; ++t) {
    printf("Case #%d: ", t);
    int N, M;
    scanf("%d%d", &N, &M);
    for (int n = 0; n < N; ++n) {
      for (int m = 0; m < M; ++m) {
        scanf("%d", &lawn[n][m]);

      }
    }
    printf("%s\n", mow(lawn, N, M) ? "YES" : "NO");
  }
  return 0;
}

