#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <math.h>
#include <sstream>
using namespace std;

int cekBoard(string tData[]) {
	int result = 0;
	
	char hor = ' ';
	int countHor = 0;
	bool horSukses = false;

	char ver = ' ';
	int countVer = 0;
	bool VerSukses = false;

	char mir1 = ' ';
	bool mir1Sukses = false;

	char mir2 = ' ';
	bool mir2Sukses = false;

	int countData = 0;

	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			if (tData[i][j] != '.') {
				countData++;
			}

			if (!horSukses) {
				if (j == 0) {
					hor = tData[i][j];
					countHor = 1;
				} else {
					if (hor == 'T') {
						hor = tData[i][j];
					} else {
						if ((hor != '.') && (tData[i][j] != '.') && ((hor == tData[i][j]) || (tData[i][j] == 'T'))) {
							countHor++;
						}
					}
				}
			}
			if (!VerSukses) {
				if (j == 0) {
					ver = tData[j][i];
					countVer = 1;
				} else {
					if (ver == 'T') {
						ver = tData[j][i];
					} else {
						if ((ver != '.') && (tData[j][i] != '.') && ((ver == tData[j][i]) || (tData[j][i] == 'T'))) {
							countVer++;
						}
					}
				}
			}
		}
		if (countHor == 4) {
			horSukses = true;
		}
		if (countVer == 4) {
			VerSukses = true;
		}
	}

	if ((!horSukses) && (!VerSukses)) {
		if (tData[0][0] != 'T') {
			if ((tData[0][0] != '.') && ((tData[0][0] == tData[1][1]) || (tData[1][1] == 'T')) && ((tData[0][0] == tData[2][2]) || (tData[2][2] == 'T')) && ((tData[0][0] == tData[3][3]) || (tData[3][3] == 'T'))) {
				mir1Sukses = true;
				mir1 = tData[0][0];
			}
		} else {
			if ((tData[1][1] != '.') && (tData[1][1] == tData[2][2]) && (tData[1][1] == tData[3][3])) {
				mir1Sukses = true;
				mir1 = tData[1][1];
			}		
		}
		
		if (!mir1Sukses) {
			if (tData[3][0] != 'T') {
				if ((tData[3][0] != '.') && ((tData[3][0] == tData[2][1]) || (tData[2][1] == 'T')) && ((tData[3][0] == tData[1][2]) || (tData[1][2] == 'T')) && ((tData[3][0] == tData[0][3]) || (tData[0][3] == 'T'))) {
					mir2Sukses = true;
					mir2 = tData[3][0];
				}
			} else {
				if ((tData[2][1] != '.') && (tData[2][1] == tData[1][2]) && (tData[2][1] == tData[0][3])) {
					mir2Sukses = true;
					mir2 = tData[2][1];
				}		
			}
		}
	}

	if (horSukses) {
		if (hor == 'X') {
			result = 1;
		} else if (hor == 'O') {
			result = 2;
		}
	} else if (VerSukses) {
		if (ver == 'X') {
			result = 1;
		} else if (ver == 'O') {
			result = 2;
		}
	} else if (mir1Sukses) {
		if (mir1 == 'X') {
			result = 1;
		} else if (mir1 == 'O') {
			result = 2;
		}
	} else if (mir2Sukses) {
		if (mir2 == 'X') {
			result = 1;
		} else if (mir2 == 'O') {
			result = 2;
		}
	} else {
		if (countData == 16) {
			result = 3;
		} else {
			result = 4;
		}
	}


	return result;
}
int main() {	
	int T = 0;
	scanf("%d\n",&T);
	for (int i=0; i<T; i++) {
		string data[4];
		for (int j=0; j<4; j++) {
			getline(cin,data[j]);
		}
		if (i != T-1) {
			scanf("\n");
		}
		int hasil = cekBoard(data);
		printf("Case #%d: ",i+1);
		if (hasil == 1) {
			cout << "X won\n";
		} else if (hasil == 2) {
			cout << "O won\n";
		} else if (hasil == 3) {
			cout << "Draw\n";
		} else if (hasil == 4) {
			cout << "Game has not completed\n";
		}
	}
	//while (scanf("%d %d %d\n",&d1,&d2,&d3) != EOF) {
		//jawaban
		//printf("Case #%d: %d\n",d1,d2);
	//}
	//getch(); 
	return 0;
}