#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
	int T;
	char temp;
	scanf("%d", &T);
	scanf("%c", &temp);
	for (int z = 0; z < T; z++) {
		int numDots = 0;
		bool result = false;
		char board[4][4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%c", &board[i][j]);
				if (board[i][j] == '.') {
					numDots ++;
				}
			}
			scanf("%c", &temp);			
		}
		/*for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				printf("%c", board[i][j]);
			}
			printf("\n");		
		}*/
		scanf("%c", &temp);
		printf("Case #%d: ", (z + 1));
		for (int i = 0; i < 4; i++) {
			int rowX = 0;
			int rowO = 0;
			int rowT = 0;
			for (int j = 0; j < 4; j++) {
				if (board[i][j] == 'X') {
					rowX++;
				}
				if (board[i][j] == 'O') {
					rowO++;
				}
				if (board[i][j] == 'T') {
					rowT ++;
				}
			}
			if ((rowX == 4) || ((rowX == 3) && (rowT == 1))) {
				result = true;
				printf("X won\n");
				break;
			}
			if ((rowO == 4) || ((rowO == 3) && (rowT == 1))) {
				result = true;
				printf("O won\n");
				break;
			}
		}
		if (result) {
			continue;
		}
		for (int i = 0; i < 4; i++) {
			int colX = 0;
			int colO = 0;
			int colT = 0;
			for (int j = 0; j < 4; j++) {
				if (board[j][i] == 'X') {
					colX++;
				}
				if (board[j][i] == 'O') {
					colO++;
				}
				if (board[j][i] == 'T') {
					colT ++;
				}
			}
			if ((colX == 4) || ((colX == 3) && (colT == 1))) {
				result = true;
				printf("X won\n");
				break;
			}
			if ((colO == 4) || ((colO == 3) && (colT == 1))) {
				result = true;
				printf("O won\n");
				break;
			}
		}
		if (result) {
			continue;
		}
		int lDiagX = 0;
		int lDiagO = 0;
		int lDiagT = 0;
		for (int i = 0; i < 4; i++) {
			int j = i;
			if (board[j][i] == 'X') {
				lDiagX++;
			}
			if (board[j][i] == 'O') {
				lDiagO++;
			}
			if (board[j][i] == 'T') {
				lDiagT ++;
			}
		}
		if ((lDiagX == 4) || ((lDiagX == 3) && (lDiagT == 1))) {
			result = true;
			printf("X won\n");
			continue;
		}
		if ((lDiagO == 4) || ((lDiagO == 3) && (lDiagT == 1))) {
			result = true;
			printf("O won\n");
			continue;
		}
		if (result) {
			continue;
		}
		int rDiagX = 0;
		int rDiagO = 0;
		int rDiagT = 0;
		for (int i = 0; i < 4; i++) {
			int j = 3 - i;
			if (board[i][j] == 'X') {
				rDiagX++;
			}
			if (board[i][j] == 'O') {
				rDiagO++;
			}
			if (board[i][j] == 'T') {
				rDiagT ++;
			}
		}
		if ((rDiagX == 4) || ((rDiagX == 3) && (rDiagT == 1))) {
			result = true;
			printf("X won\n");
			continue;
		}
		if ((rDiagO == 4) || ((rDiagO == 3) && (rDiagT == 1))) {
			result = true;
			printf("O won\n");
			continue;
		}
		if (result) {
			continue;
		}
		if (numDots > 0) {
			printf("Game has not completed\n");
		}
		else {
			printf("Draw\n");
		}

	}
}