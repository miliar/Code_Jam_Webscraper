#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <fstream>

using namespace std;

typedef unsigned long long uint64;
typedef long long int64;

const int N = 4;
char board[N][N];

bool is_game_completed() {
	for (int x = 0; x < N; ++x) {
		for (int y = 0; y < N; ++y) {
			if (board[x][y] == '.') {
				return false;
			}
		}
	}
	return true;
}

bool checkset_win(int X, int O, int T, char &winner) {
	if (X == 4 || (X == 3 && T == 1)) {
		winner = 'X';
		return true;
	} 
	if (O == 4 || (O == 3 && T == 1)) {
		winner = 'O';
		return true;
	}
	return false;
}

void checkset_move(char move, int &X, int &O, int &T) {
	if (move == 'X') {
		X++;
	} else if (move == 'O') {
		O++;
	} else if (move == 'T') {
		T++;
	}
}

bool has_winner_in_forward_diagonal(char &winner) {
	int X, O, T;
	X = O = T = 0;
	for (int i = 0; i < N; ++i) {
		checkset_move(board[i][i], X, O, T);
	}
	return checkset_win(X, O, T, winner);
}

bool has_winner_in_backward_diagonal(char &winner) {
	int X, O, T;
	X = O = T = 0;
	for (int i = 0; i < N; ++i) {
		checkset_move(board[i][N - 1 - i], X, O, T);
	}
	return checkset_win(X, O, T, winner);
}

bool has_winning_row(char &winner) {
	int X;
	int O;
	int T;
	for (int x = 0; x < N; ++x) {
		X = O = T = 0;
		for (int y = 0; y < N; ++y) {
			checkset_move(board[x][y], X, O, T);
		}
		if (checkset_win(X, O, T, winner)) {
			return true;
		}
	}
	return false;
}

bool has_winning_column(char &winner) {
	int X;
	int O;
	int T;
	for (int y = 0; y < N; ++y) {
		X = O = T = 0;
		for (int x = 0; x < N; ++x) {
			checkset_move(board[x][y], X, O, T);
		}
		if (checkset_win(X, O, T, winner)) {
			return true;
		}
	}
	return false;
}

void read_board(istream &in) {
	for (int x = 0; x < N; ++x) {
		for (int y = 0; y < N; ++y) {
			in >> board[x][y];
		}
	}
}

void validate(int nth) {
	char winner = '_';
	cout << "Case #" << nth << ": ";
	if (has_winner_in_forward_diagonal(winner) ||
		has_winner_in_backward_diagonal(winner) ||
		has_winning_column(winner) ||
		has_winning_row(winner)) {
		cout << winner << " won\n";
	} else {
		if (is_game_completed()) {
			cout << "Draw\n";
		} else {
			cout << "Game has not completed\n";
		}
	}
}

void show_board() {
	for (int x = 0; x < N; ++x) {
		for (int y = 0; y < N; ++y) {
			cout << board[x][y];
		}
		cout << endl;
	}
	cout << endl << endl;
}
void google_tic_tac_toe(istream &in) {
	int test_cases;
	in >> test_cases;
	string empty_line;
	for (int i = 1; i <= test_cases; ++i) {
		read_board(in);
		getline(in, empty_line);
		validate(i);
	}
}

int main() {
	google_tic_tac_toe(cin);
	return 0;
}