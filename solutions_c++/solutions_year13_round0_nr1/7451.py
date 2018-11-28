/*
 * =====================================================================================
 *
 *       Filename:  problemA.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/13/13 11:06:59
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  PascalMore (), yq.mao.it@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 5
#define MAXM 5
#define X_WON "X won"
#define O_WON "O won"
#define DRAW "Draw"
#define NOT_COMPLETE "Game has not completed"

int board[MAXN][MAXN];

void judgeStatus(int x) {
	int sumCol[4];
	int left=0, right=0;
	bool existPoint = false;
	memset(sumCol, 0, sizeof sumCol);
	for (int i=0; i<4; ++i) {
		int sumRow = 0;
		for (int j=0; j<4; ++j) {
			//printf ("%d ", board[i][j]);
			sumCol[j] += board[i][j];
			if (i==j) left += board[i][j];
			if ((3-i) == j) right += board[i][j];
			if (board[i][j] == -1) existPoint = true;
			sumRow += board[i][j];
		}
		if (sumRow == 20 || sumRow == 15) {
			printf("Case #%d: %s\n", x, O_WON);
			return;
		}
		else if (sumRow == -20 || sumRow == -15) {
			printf("Case #%d: %s\n", x, X_WON);
			return;
		}
	}
	
	for (int i=0; i<4; ++i) {
		if (sumCol[i] == 20 || sumCol[i] == 15) {
			printf("Case #%d: %s\n", x, O_WON);
			return;
		}
		else if (sumCol[i] == -20 || sumCol[i] == -15) {
			printf("Case #%d: %s\n", x, X_WON);
			return;
		}
	}
	if (left == 20 || left == 15) {
		printf("Case #%d: %s\n", x, O_WON);
		return;
	}
	else if (left == -20 || left == -15) {
		printf("Case #%d: %s\n", x, X_WON);
		return;
	}
	if (right == 20 || right == 15) {
		printf("Case #%d: %s\n", x, O_WON);
		return;
	}
	else if (right == -20 || right == -15) {
		printf("Case #%d: %s\n", x, X_WON);
		return;
	}

	if (!existPoint) {
		printf("Case #%d: %s\n", x, DRAW);
		return;
	}
	else {
		printf("Case #%d: %s\n", x, NOT_COMPLETE);
		return;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	char c;
	scanf("%d", &T);
	//printf("%d\n", T);
	for (int k=1; k<=T; ++k) {
		scanf ("%c", &c);
		for (int i=0; i<4; ++i) {
			for (int j=0; j<4; ++j) {
				scanf("%c", &c);
				//printf("(%d %d) = %c\n", i, j, c);
				switch (c) {
					case 'X':
						board[i][j] = -5;
						break;
					case 'O':
						board[i][j] = 5;
						break;
					case 'T':
						board[i][j] = 0;
						break;
					case '.':
						board[i][j] = -1;
						break;
					case '\n':
						continue;
						break;
				}
			}
			scanf("%c", &c);
		}
		judgeStatus(k);
	}
	return 0;	
}
