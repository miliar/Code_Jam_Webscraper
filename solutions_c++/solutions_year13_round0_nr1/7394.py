#include <stdio.h>


int main() {
	int caseNo, caseCount, i, j, tx, ty;
	char board[5][5], temp;
	bool emptyCell, XWon, OWon;

	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);

	scanf("%d\n", &caseNo);
	caseCount = 1;
	while (caseNo--) {
		//for (i = 0; i < 4; i++) {
		//	gets(board[i]);
		//}

		tx = ty = -1;
		emptyCell = false;

		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf("%c", &board[i][j]);
				if (board[i][j] == 'T') {
					tx = i;
					ty = j;
				} else if (board[i][j] == '.') {
					emptyCell = true;
				} 
			}
			scanf("%c", &temp);
		}
		

		/*for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				printf("%c", board[i][j]);
			}
			printf("\n");
		}*/

		if (tx != -1 && ty != -1) {
			board[tx][ty] = 'X';
		}

		XWon = false;
		OWon = false;
		if ((board[0][0] == 'X' && board[0][1] == 'X' && board[0][2] == 'X' && board[0][3] == 'X') ||
			(board[1][0] == 'X' && board[1][1] == 'X' && board[1][2] == 'X' && board[1][3] == 'X') ||
			(board[2][0] == 'X' && board[2][1] == 'X' && board[2][2] == 'X' && board[2][3] == 'X') ||
			(board[3][0] == 'X' && board[3][1] == 'X' && board[3][2] == 'X' && board[3][3] == 'X') ||

			(board[0][0] == 'X' && board[1][0] == 'X' && board[2][0] == 'X' && board[3][0] == 'X') ||
			(board[0][1] == 'X' && board[1][1] == 'X' && board[2][1] == 'X' && board[3][1] == 'X') ||
			(board[0][2] == 'X' && board[1][2] == 'X' && board[2][2] == 'X' && board[3][2] == 'X') ||
			(board[0][3] == 'X' && board[1][3] == 'X' && board[2][3] == 'X' && board[3][3] == 'X') ||
			
			(board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X' && board[3][3] == 'X') ||
			(board[0][3] == 'X' && board[1][2] == 'X' && board[2][1] == 'X' && board[3][0] == 'X')) {
			XWon = true;
		} 
		
		if (tx != -1 && ty != -1) {
			board[tx][ty] = 'O';
		}
		if ((board[0][0] == 'O' && board[0][1] == 'O' && board[0][2] == 'O' && board[0][3] == 'O') ||
			(board[1][0] == 'O' && board[1][1] == 'O' && board[1][2] == 'O' && board[1][3] == 'O') ||
			(board[2][0] == 'O' && board[2][1] == 'O' && board[2][2] == 'O' && board[2][3] == 'O') ||
			(board[3][0] == 'O' && board[3][1] == 'O' && board[3][2] == 'O' && board[3][3] == 'O') ||

			(board[0][0] == 'O' && board[1][0] == 'O' && board[2][0] == 'O' && board[3][0] == 'O') ||
			(board[0][1] == 'O' && board[1][1] == 'O' && board[2][1] == 'O' && board[3][1] == 'O') ||
			(board[0][2] == 'O' && board[1][2] == 'O' && board[2][2] == 'O' && board[3][2] == 'O') ||
			(board[0][3] == 'O' && board[1][3] == 'O' && board[2][3] == 'O' && board[3][3] == 'O') ||
			
			(board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O' && board[3][3] == 'O') ||
			(board[0][3] == 'O' && board[1][2] == 'O' && board[2][1] == 'O' && board[3][0] == 'O')) {
			OWon = true;
		}


		if (XWon) {
			printf("Case #%d: X won\n", caseCount++);
		} else if (OWon) {
			printf("Case #%d: O won\n", caseCount++);
		} else if (!emptyCell) {
			printf("Case #%d: Draw\n", caseCount++);
		} else {
			printf("Case #%d: Game has not completed\n", caseCount++);
		}
		gets(board[i]);
	}
	return 0;
}
