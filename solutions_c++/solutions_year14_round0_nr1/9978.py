/*
 * File: .cpp
 * ------------------------------------------------
 * Name: Stacey Tay
 * Solution to Problem A of Google's Code Jam 2014.
 */

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
  // freopen("A.in", "r", stdin);
  int T;
  scanf("%d", &T);
  for (int k = 0; k < T; k++) {
    int row1, row2;
    int cards1[4][4], cards2[4][4];
    scanf("%d", &row1);
    row1--;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
	scanf("%d", &cards1[i][j]);
    scanf("%d", &row2);
    row2--;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
	scanf("%d", &cards2[i][j]);

    int card, numCards = 0;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
	if (cards1[row1][i] == cards2[row2][j]) {
	  numCards++;
	  if (numCards == 1)
	    card = cards1[row1][i];
	}

    if (numCards == 0)
      printf("Case #%d: Volunteer cheated!\n", k + 1);
    else if (numCards == 1)
      printf("Case #%d: %d\n", k + 1, card);
    else
      printf("Case #%d: Bad magician!\n", k + 1);
  }
  return 0;
}
