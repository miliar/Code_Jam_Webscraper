#include <stdio.h>

int grid[4][4], row1[4], row2[4];

int main() {
  int T;
  
  scanf("%d", &T);
  
  for(int t = 1; t <= T; t++) {
    int row;

    scanf("%d", &row);

    for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
	scanf("%d", &grid[i][j]);
	if(i == row - 1) row1[j] = grid[i][j];
      }
    }

    scanf("%d", &row);

    for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
	scanf("%d", &grid[i][j]);
	if(i == row - 1) row2[j] = grid[i][j];
      }
    }

    int acc = 0, card;

    for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
	if(row1[i] == row2[j]) {
	  acc++;
	  card = row1[i];
	}
      }
    }

    if(acc == 0) printf("Case #%d: Volunteer cheated!\n", t);
    else if(acc == 1) printf("Case #%d: %d\n", t, card);
    else printf("Case #%d: Bad magician!\n", t);
  }

  return 0;
}
