//============================================================================
// Name        : Tic-Tac-Toe-Tomek.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

bool terminado(char tab[][4]) {
	for (unsigned int i=0; i<4; i++) {
		for (unsigned int j=0; j<4; j++) {
			if (tab[j][i] == '.')
				return false;
		}
	}
	return true;
}

char win(char A[]) {

	if (A[0] == 'T') {
		for (unsigned int i=2; i<4; i++) {
			if (A[i] == '.' || A[1] != A[i])
				return -1;
		}
		return A[1];
	} else {
		for (unsigned int i=1; i<4; i++) {
			if (A[i] != 'T') {
				if (A[i] == '.' || A[0] != A[i])
					return -1;
			}
		}
		return A[0];
	}
}

int main() {
	ifstream fin("C:\\Users\\Daniel\\Downloads\\Firefox\\A-large.in");
	ofstream fout("C:\\Users\\Daniel\\Downloads\\Firefox\\A-large.out");
	unsigned int T;

	fin >> T;

	for (unsigned int k=1; k<=T; k++) {
		char tablero[4][4];
		char gana = -1;
		for (unsigned int i=0; i<4; i++) {
			for (unsigned int j=0; j<4; j++) {
				fin >> tablero[j][i];
			}
		}
		for (unsigned int i=0; i<4 && gana == -1; i++) {
			char a[4] = {tablero[i][0], tablero[i][1], tablero[i][2], tablero[i][3]};
			gana = win(a);
		}
		for (unsigned int i=0; i<4 && gana == -1; i++) {
			char a[4] = {tablero[0][i], tablero[1][i], tablero[2][i], tablero[3][i]};
			gana = win(a);
		}
		if (gana == -1) {
			char a[4] = {tablero[0][0], tablero[1][1], tablero[2][2], tablero[3][3]};
			gana = win(a);
			if (gana == -1) {
				char a[4] = {tablero[0][3], tablero[1][2], tablero[2][1], tablero[3][0]};
				gana = win(a);
			}
		}

		if (gana == -1) {
			if (terminado(tablero))
				fout << "Case #" << k << ": Draw\n";
			else
				fout << "Case #" << k << ": Game has not completed\n";
		} else {
			fout << "Case #" << k << ": " << gana << " won\n";
		}

	}


	return 0;
}
