#include <iostream>

using namespace std;

#define all(x) (x).begin(), (x).end()
#define forn(i, n) for(int i=0; i<(int)(n); i++)

enum Piece { Draw, InProgress, O, X, TT, Empty };
enum Check { Row, Column, Diagonal, ReverseDiagonal };

Piece getIthValue(const Piece (&board)[4][4], int index, int var, 
				  Check check) {
	switch (check) {
	case Row:
		return board[index][var];
	case Column:
		return board[var][index];
	case Diagonal:
		return board[var][var];
	case ReverseDiagonal:
		return board[3 - var][var];
	default:
		cout << "unexpected check \n";
		return Empty;
	}
}

Piece getWinner(const Piece (&board)[4][4], int fixed_index, 
				Check check) {
	Piece color = getIthValue(board, fixed_index, 0, check);
	if (color == Empty) return InProgress;
	if (color == TT)
		color = getIthValue(board, fixed_index, 1, check);
	for (int var = 1; var < 4; var++) {
		Piece c = getIthValue(board, fixed_index, var, check);
		if (c == TT) continue;
		if (c == Empty) return InProgress;
		if (color != c)
			return Draw;
	}
	return color;
}

Piece hasWon(const Piece (&board)[4][4]) {
	Piece winner = Draw;
	bool isInProgress = false;
	// Check rows and columns
	forn(i, 4) {
		winner = getWinner(board, i, Row);
		if (winner == O || winner == X) {
			return winner;
		} else if (winner == InProgress)
			isInProgress = true;

		winner = getWinner(board, i, Column);
		if (winner == O || winner == X) {
			return winner;
		} else if (winner == InProgress)
			isInProgress = true;
	}

	winner = getWinner(board, -1, Diagonal);
	if (winner == O || winner == X) {
		return winner;
	} else if (winner == InProgress)
		isInProgress = true;

	winner = getWinner(board, -1, ReverseDiagonal);
	if (winner == O || winner == X) {
		return winner;
	} else if (winner == InProgress)
		isInProgress = true;
	if (isInProgress) return InProgress;
	return Draw;
}

int main()
{
	int T;
	cin >> T;

	string s;
	getline(cin, s); // remove '\n'

	forn(i, T) {
		Piece board[4][4];
		forn(j, 4) {
			getline(cin, s);
			forn(k, 4) {
				switch (s[k]) {
				case '.':
					board[j][k] = Empty;
					break;
				case 'O':
					board[j][k] = O;
					break;
				case 'X':
					board[j][k] = X;
					break;
				case 'T':
					board[j][k] = TT;
					break;
				default:
					cout << "unexpected input" << endl;
				}
			}
		}
		Piece winner = hasWon(board);
		cout << "Case #" << i + 1 << ": ";
		switch (winner) {
		case X:
			cout << "X won\n";
			break;
		case O:
			cout << "O won\n";
			break;
		case Draw:
			cout << "Draw\n";
			break;
		case InProgress:
			cout << "Game has not completed\n";
			break;
		default:
			cout << "unexpected output" << endl;
		}
		getline(cin, s); // remove '\n'
	}

	return 0;
}
