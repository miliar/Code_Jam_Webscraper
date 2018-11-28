// Warm up question.

#include <iostream>
#include <vector>

using namespace std;

int main() {
  int TC;
  int rowA, rowB;
  int A[4][4], B[4][4];
  scanf("%d ", &TC);
  for (int tc = 1; tc <= TC; ++tc) {
    scanf("%d ", &rowA);
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        scanf("%d ", &A[i][j]);
      }
    }
    scanf("%d ", &rowB);
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        scanf("%d ", &B[i][j]);
      }
    }
    vector<int> sols;
    for (int guess = 1; guess <= 16; ++guess) {
      bool inA = false;
      for (int i = 0; i < 4; ++i) {
        if (A[rowA - 1][i] == guess) {
          inA = true;
        }
      }
      bool inB = false;
      for (int i = 0; i < 4; ++i) {
        if (B[rowB - 1][i] == guess) {
          inB = true;
        }
      }
      if (inA && inB) {
        sols.push_back(guess);
      }
    }
    printf("Case #%d: ", tc);
    if (sols.size() == 0) {
      printf("Volunteer cheated!\n");
    } else if (sols.size() == 1) {
      printf("%d\n", sols.back());
    } else {
      printf("Bad magician!\n");
    }
  }
  return 0;
}
