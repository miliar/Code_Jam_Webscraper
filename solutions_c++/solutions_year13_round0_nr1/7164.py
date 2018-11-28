/*
 * tic-tac-toe.cpp
 *
 *  Created on: Apr 14, 2013
 *      Author: saha
 */




#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <queue>

using namespace std;

int main()
{
	int T, N;
	char P[5][5];

	int isDot = 0;
	int xWon = 0;
	int oWon = 0;

	scanf("%d", &T);
	scanf("\n");
	for(int t=1; t<=T ; t++, scanf("\n")) {
		memset(P, 0, sizeof(P));
		isDot = 0;
		xWon = 0;
		oWon = 0;

		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				scanf("%c", &P[i][j]);
				if(P[i][j] == '.')
					isDot = 1;
			}
			scanf("\n");
		}

//		for(int i=0;i<4;i++) {
//			for(int j=0;j<4;j++) {
//				printf("%c",P[i][j]);
//			}
//			printf("\n");
//		}
//		printf("\n");

		xWon = 1;
		for(int i=0;i<4;i++) {
			if(P[i][i] != 'X' && P[i][i] != 'T'){
				xWon = 0; break;
			}
		}
		if(xWon == 1) {
			printf("Case #%d: X won\n",t);
			continue;
		}

		xWon = 1;
		for(int i=0;i<4;i++) {
			if(P[3-i][i] != 'X' && P[3-i][i] != 'T'){
				xWon = 0; break;
			}
		}
		if(xWon == 1) {
			printf("Case #%d: X won\n",t);
			continue;
		}

		oWon = 1;
		for(int i=0;i<4;i++) {
			if(P[i][i] != 'O' && P[i][i] != 'T'){
				oWon = 0; break;
			}
		}
		if(oWon == 1) {
			printf("Case #%d: O won\n",t);
			continue;
		}

		oWon = 1;
		for(int i=0;i<4;i++) {
			if(P[3-i][i] != 'O' && P[3-i][i] != 'T'){
				oWon = 0; break;
			}
		}
		if(oWon == 1) {
			printf("Case #%d: O won\n",t);
			continue;
		}

		for(int i=0;i<4;i++) {
			xWon = 1;
			for(int j=0;j<4;j++) {
				if(P[i][j] != 'X' && P[i][j] != 'T'){
					xWon = 0; break;
				}
			}
			if(xWon == 1)
				break;
			xWon = 1;
			for(int j=0;j<4;j++) {
				if(P[j][i] != 'X' && P[j][i] != 'T'){
					xWon = 0; break;
				}
			}
			if(xWon == 1)
				break;
		}
		if(xWon == 1) {
			printf("Case #%d: X won\n",t);
			continue;
		}

		for(int i=0;i<4;i++) {
			oWon = 1;
			for(int j=0;j<4;j++) {
				if(P[i][j] != 'O' && P[i][j] != 'T'){
					oWon = 0; break;
				}
			}
			if(oWon == 1)
				break;
			oWon = 1;
			for(int j=0;j<4;j++) {
				if(P[j][i] != 'O' && P[j][i] != 'T'){
					oWon = 0; break;
				}
			}
			if(oWon == 1)
				break;
		}
		if(oWon == 1) {
			printf("Case #%d: O won\n",t);
			continue;
		}

		if(isDot == 1)
			printf("Case #%d: Game has not completed\n",t);
		else
			printf("Case #%d: Draw\n",t);
	}
}
