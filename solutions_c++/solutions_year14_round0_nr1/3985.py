// Solution to google code jam 2014 Round 1, Problem A

#include <set>
#include <iostream>
#include <stdio.h>

using namespace std;

#define SQUARE_SIZE 4

int main() {
  int cases;
  cin >> cases;
  for (int i = 1; i < cases + 1; i++) {
    int first_row_nums[SQUARE_SIZE];
    int row_num[2];
    int common = 0;
    int answer;
    for (int v = 0; v < 2; v++) {
      cin >> row_num[v];
      for (int current_row = 0; current_row < SQUARE_SIZE; current_row++) {
        // we are on the row of interest
        if (current_row + 1 == row_num[v]) {
          for (int ii = 0; ii < SQUARE_SIZE ; ii++) {
            if (v == 0) {
              cin >> first_row_nums[ii];
            } else {
              int targetNum;
              cin >> targetNum;
              // linear search for the same number
              for (int iii = 0; iii < SQUARE_SIZE; iii++) {
                if (first_row_nums[iii] == targetNum) {
                  common++;
                  answer = targetNum;
                }
              }
            }
          }
        } else {
          cin.get();
          cin.ignore(256, '\n');
        }
      }
    }
    if (common == 1) {
      printf("Case #%d: %d\n", i, answer);
    } else if (!common) {
      printf("Case #%d: Volunteer cheated!\n", i);
    } else {
      printf("Case #%d: Bad magician!\n", i);
    }
  }
}
