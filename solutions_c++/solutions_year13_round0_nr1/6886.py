#include <iostream>
#include <cstdio>

using namespace std;

char board[4][4];

char diagonalP() {
	//verifica a diagonal principal
	int O = 0;
	int X = 0;
	int T = 0;
	int dot = 0;
	for (int i = 0; i < 4; i++) {

		if (board[i][i] == 'O') {
			O++;
		} else if (board[i][i] == 'X') {
			X++;
		} else if (board[i][i] == 'T'){
			T++;
		} else {
			dot++;
		}
	}
	if (dot == 0 && O == 0) {
		return 'x';
	} else if (dot == 0 && X == 0) {
		return 'o';
	} else {
		return 'n';
	}
}

char diagonalS() {
	//verifica a diagonal secundária
	int O = 0;
	int X = 0;
	int T = 0;
	int dot = 0;
	for (int i = 0, j = 3; i < 4; i++, j--) {
		
		if (board[i][j] == 'O') {
			O++;
		} else if (board[i][j] == 'X') {
			X++;
		} else if (board[i][j] == 'T'){
			T++;
		} else {
			dot++;
		}
	}
	if (dot == 0 && O == 0) {
		return 'x';
	} else if (dot == 0 && X == 0) {
		return 'o';
	} else {
		return 'n';
	}
}

char linhas() {
	for (int i = 0; i < 4; i++) {
		
		int O = 0;
		int X = 0;
		int T = 0;
		int dot = 0;
		for (int j = 0; j < 4; j++) {

			if (board[i][j] == 'O') {
				O++;
			} else if (board[i][j] == 'X') {
				X++;
			} else if (board[i][j] == 'T'){
				T++;
			} else {
				dot++;
			}
		}

		if (dot == 0 && O == 0) {
			return 'x';
		} else if (dot == 0 && X == 0) {
			return 'o';
		} 
	}
	return 'n';
}

char colunas() {
	for (int i = 0; i < 4; i++) {
		
		int O = 0;
		int X = 0;
		int T = 0;
		int dot = 0;

		for (int j = 0; j < 4; j++) {

			if (board[j][i] == 'O') {
				O++;
			} else if (board[j][i] == 'X') {
				X++;
			} else if (board[j][i] == 'T'){
				T++;
			} else {
				dot++;
			}
		}
		if (dot == 0 && O == 0) {
			return 'x';
		} else if (dot == 0 && X == 0) {
			return 'o';
		} 
	}
	return 'n';
}

bool isFull() {
	for (int j = 0; j < 4; j++) {
		for (int k = 0; k < 4; k++) {
			if (board[j][k] == '.') {
				return false;
			}
		}
	}
	return true;
}

bool empate() {
	if (diagonalP() != 'x' && diagonalS() != 'x' && linhas() != 'x' && colunas() != 'x' 
		&& diagonalP() != 'o' && diagonalS() != 'o' && linhas() != 'o' && colunas() != 'o' 
		&& isFull()) {
		return true;
	}
	return false;
}

bool incompleto() {
	if (diagonalP() != 'x' && diagonalS() != 'x' && linhas() != 'x' && colunas() != 'x' 
		&& diagonalP() != 'o' && diagonalS() != 'o' && linhas() != 'o' && colunas() != 'o' 
		&& !isFull()) {
		return true;
	}
	return false;
}

int main() {
	int n;
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> board[j][k];
			}
		}
		
		if (diagonalP() == 'x' || diagonalS() == 'x' || linhas() == 'x' || colunas() == 'x') {
			printf("Case #%d: X won\n", i+1);
		} else if (diagonalP() == 'o' || diagonalS() == 'o' || linhas() == 'o' || colunas() == 'o') {
			printf("Case #%d: O won\n", i+1);
		} else if (empate()) {
			printf("Case #%d: Draw\n", i+1);
		} else if (incompleto()) {
			printf("Case #%d: Game has not completed\n", i+1);
		}
	}

	return 0;
}
