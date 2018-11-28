#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <bitset>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");

void TicTacToe() {
	char Board[4][4];
	bool complete = true;
	for (int i=0; i<4; ++i) {
		for (int j=0; j<4; ++j) {
			fin >> Board[i][j];
			if (Board[i][j] == '.')
				complete = false;
		}
	}
	
	bool found;
	for (int i=0; i<4; ++i) {
		found = true;
		for (int j=0; j<4; ++j) {
			if (Board[i][j] != 'X' && Board[i][j] != 'T') {
				found = false;
				break;
			}
		}
		if (found) {
			fout << "X won" << endl;
			return;
		}

		found = true;
		for (int j=0; j<4; ++j) {
			if (Board[j][i] != 'X' && Board[j][i] != 'T') {
				found = false;
				break;
			}
		}
		if (found) {
			fout << "X won" << endl;
			return;
		}
	}
	found = true;
	for (int i=0; i<4; ++i) {
		if (Board[i][i] != 'X' && Board[i][i] != 'T') {
			found = false;
			break;
		}
	}
	if (found) {
		fout << "X won" << endl;
		return;
	}
	found = true;
	for (int i=0; i<4; ++i) {
		if (Board[i][3-i] != 'X' && Board[i][3-i] != 'T') {
			found = false;
			break;
		}
	}
	if (found) {
		fout << "X won" << endl;
		return;
	}

	for (int i=0; i<4; ++i) {
		bool found = true;
		for (int j=0; j<4; ++j) {
			if (Board[i][j] != 'O' && Board[i][j] != 'T') {
				found = false;
				break;
			}
		}
		if (found) {
			fout << "O won" << endl;
			return;
		}

		found = true;
		for (int j=0; j<4; ++j) {
			if (Board[j][i] != 'O' && Board[j][i] != 'T') {
				found = false;
				break;
			}
		}
		if (found) {
			fout << "O won" << endl;
			return;
		}
	}

	found = true;
	for (int i=0; i<4; ++i) {
		if (Board[i][i] != 'O' && Board[i][i] != 'T') {
			found = false;
			break;
		}
	}
	if (found) {
		fout << "O won" << endl;
		return;
	}
	found = true;
	for (int i=0; i<4; ++i) {
		if (Board[i][3-i] != 'O' && Board[i][3-i] != 'T') {
			found = false;
			break;
		}
	}
	if (found) {
		fout << "O won" << endl;
		return;
	}

	if (complete) {
		fout << "Draw" << endl;
	}
	else {
		fout << "Game has not completed" << endl;
	}
}

void Lawnmower() {
	int N, M;
	fin >> N >> M;

	int CurrentBoard[100][100];
	int AimBoard[100][100];
	bool QuickFail = false;
	for (int i=0; i<N; ++i) {
		for (int j=0; j<M; ++j) {
			fin >> AimBoard[i][j];
			if (AimBoard[i][j] > 100 || AimBoard[i][j] < 1)
				QuickFail = true;
			CurrentBoard[i][j] = 100;
		}
	}
	if (QuickFail) {
		fout << "NO" << endl;
		return;
	}


	for (int i=0; i<N; ++i) {
		int maximum = 0;
		for (int j=0; j<M; ++j)
			maximum = max<int>(maximum, AimBoard[i][j]);
		for (int j=0; j<M; ++j)
			CurrentBoard[i][j] = min<int>(CurrentBoard[i][j], maximum);
	}

	for (int i=0; i<M; ++i) {
		int maximum = 0;
		for (int j=0; j<N; ++j)
			maximum = max<int>(maximum, AimBoard[j][i]);
		for (int j=0; j<N; ++j)
			CurrentBoard[j][i] = min<int>(CurrentBoard[j][i], maximum);
	}

	bool success = true;
	for (int i=0; i<N; ++i) {
		for (int j=0; j<M; ++j) {
			if (CurrentBoard[i][j] != AimBoard[i][j]) {
				success = false;
				break;
			}
		}
		if (!success)
			break;
	}

	if (success)
		fout << "YES" << endl;
	else
		fout << "NO" << endl;
}

int main() {
	int N;
	fin >> N;
	for (int i=1; i<=N; ++i) {
		fout << "Case #" << i << ": ";
		//TicTacToe();
		Lawnmower();
	}
	return 0;
}