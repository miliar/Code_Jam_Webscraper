/*
 * TTT.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Jason Wu
 */

#include "TTT.h"

void QR2013::TTT::solve() {
	int T;
	char board[5][6];
	int score[6][4];
	int dot, status;
	const char *msg;

	scanf("%d", &T);

	for (int c = 1; c <= T; c++) {
		REP(i, 4) scanf("%s", board[i]);
		REP(i, 6) REP(j, 4) score[i][j] = 0;
		dot = status = 0;

		REP(i, 4) REP(j, 4) {
			//0 - X row
			//1 - X col
			//2 - O row
			//3 - O col
			//4 - X diag 0, 1
			//5 - O diag 0, 1
			switch(board[i][j]) {
			case 'X':
				++score[0][i];
				++score[1][j];
				if (i == j) ++score[4][0];
				if (i+j == 3) ++score[4][1];
				break;
			case 'O':
				++score[2][i];
				++score[3][j];
				if (i == j) ++score[5][0];
				if (i+j == 3) ++score[5][1];
				break;
			case 'T':
				++score[0][i];
				++score[1][j];
				++score[2][i];
				++score[3][j];
				if (i == j) {
					++score[4][0];
					++score[5][0];
				}
				if (i+j == 3) {
					++score[4][1];
					++score[5][1];
				}
				break;
			case '.':
				++dot;
				break;
			}
		}

		REP(i, 4) REP(j, 4) {
			if (score[i][j] == 4 && i < 2) ++status;
			if (score[i][j] == 4 && i >= 2) --status;
		}
		if (score[4][0] == 4 || score[4][1] == 4) ++status;
		if (score[5][0] == 4 || score[5][1] == 4) --status;

		if (status > 0)
			msg = "X won";
		else if (status < 0)
			msg = "O won";
		else if (status == 0) {
			msg = (dot == 0) ? "Draw" : "Game has not completed";
		}

		printf("Case #%d: %s\n", c, msg);
	}
}
/* namespace QR2013 */
