/*
 * main.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: vincent
 */
#include <iostream>

using namespace std;

char getWinner(int cpt) {
	char winner = '.';

	if (cpt == 'O'*4 || cpt == 'O'*3 + 'T') {
		return 'O';
	}
	if (cpt == 'X'*4 || cpt == 'X'*3 + 'T') {
		return 'X';
	}

	return winner;
}

int main () {

	int nbGame;
	int cptLine, cptDiag1, cptDiag2, cptCol1, cptCol2, cptCol3, cptCol4, cptDot;
	bool haveDot;
	char winner;
	int line[4];
	char l[4];
	string str;

	scanf("%d\n",&nbGame);

	for (int i=0; i< nbGame; i++) {

		cptDiag1 = cptDiag2 = cptCol1 = cptCol2 = cptCol3 = cptCol4 = cptDot = 0;
		haveDot = false;
		winner ='.';

		for (int j=0; j<4; j++) {

			scanf("%s",&l);

			line[0] = (int) l[0];
			line[1] = (int) l[1];
			line[2] = (int) l[2];
			line[3] = (int) l[3];

			cptLine = line[0]+line[1]+line[2]+line[3];
			cptDiag1 += line[j];
			cptDiag2 += line[3-j];
			cptCol1 += line[0];
			cptCol2 += line[1];
			cptCol3 += line[2];
			cptCol4 += line[3];

			if (cptLine < 'O'*4) {
				haveDot = true;
			}

			if (cptLine == 'O'*4 || cptLine == 'O'*3 + 'T') {
				winner = 'O';
				//continue;
			}
			if (cptLine == 'X'*4 || cptLine == 'X'*3 + 'T') {
				winner = 'X';
				//continue;
			}
		}

		cout << "Case #" << (i+1) << ": ";
		if (winner == '.') {
			winner = getWinner(cptCol1);
			if (winner == '.') {
				winner = getWinner(cptCol2);
				if (winner == '.') {
					winner = getWinner(cptCol3);
					if (winner == '.') {
						winner = getWinner(cptCol4);
						if (winner == '.') {
							winner = getWinner(cptDiag1);
							if (winner == '.') {
								winner = getWinner(cptDiag2);
							}
						}
					}
				}
			}
		}

		if (winner != '.') {
			cout << ( (char) winner) << " won" << endl;
		} else {
			if (haveDot) {
				cout << "Game has not completed" << endl;
			} else {
				cout << "Draw" << endl;
			}
		}
		scanf("%c",&l);
	}

}




