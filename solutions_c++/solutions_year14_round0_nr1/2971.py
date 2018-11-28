#include <iostream>
#include <cstdio>

using namespace std;

#define BAD "Bad magician!"
#define CHEAT "Volunteer cheated!"
#define ROW 4
#define COL 4

int main()
{
	int T, row1, row2;
	int arrangement1[ROW][COL];
	int arrangement2[ROW][COL];
	int selectedNumbers[ROW+COL];
	int i, j, k, index, count;

	scanf("%d",&T);
	for( i = 1; i <= T; i ++ ) {
		/*
		 * Clearing all the arrays
		 */
		for( j = 0; j < (ROW+COL); j ++ ) {
			selectedNumbers[j] = 0;
		}
		
		/*
		 * Reading User Input
		 */ 
		scanf("%d",&row1);
		row1 = row1 - 1;
		for( j = 0; j < ROW; j ++ ) {
			for( k = 0; k < COL; k ++ ) {
				scanf("%d",&arrangement1[j][k]);
			}
		}

		scanf("%d",&row2);
		row2 = row2 - 1;
		for( j = 0; j < ROW; j ++ ) {
			for( k = 0; k < COL; k ++ ) {
				scanf("%d",&arrangement2[j][k]);
			}
		}
		
		/*
		 * Logic
		 */
		index = 0; 
		for( j = 0; j < COL; j ++ ) {
			for( k = 0; k < COL; k ++ ) {
				if( arrangement1[row1][j] == arrangement2[row2][k] ) {
					selectedNumbers[index++] = arrangement1[row1][j];
					break;
				}
			}
		}
		
		count = 0;
		for( j = 0; j < (ROW+COL); j ++ ) {
			if( selectedNumbers[j] == 0 )
				break;
			count ++;
		}
		
		printf("Case #%d: ",i);
		switch(count) {
			case 0:
				printf("%s",CHEAT);
				break;
			case 1:
				printf("%d",selectedNumbers[0]);
				break;
			default:
				printf("%s",BAD);
		}
		printf("\n");
	}

	return 0;
}
