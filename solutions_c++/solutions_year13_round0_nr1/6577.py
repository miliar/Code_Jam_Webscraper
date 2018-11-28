#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector<char> vc;
typedef vector< vc > MatC;


void printBoard (const MatC &board) {
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cout << board[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

struct Step {
	int i,j, di, dj;
	char player;
};

void printStep (const Step &s) {
	cout << "Step i:" << s.i <<", j:"<<s.j<<" di:"<<s.di<<", dj:"<<s.dj<<" player:"<<s.player<<endl;
}

void performStep(const MatC &board, Step &s, bool &solved, char &winner) {
	if (s.i > 3 || s.j > 3) {
		solved = true;
		winner = s.player;
		//cout << "Winner step:" << endl;
		//printStep(s);
		return;
	}
	const char cell = board[s.i][s.j];
	//cout << "current cell: " << cell << endl;
	if (cell == '.' || (cell != 'T' && s.player != '.' && cell != s.player)) return;
	if (s.player == '.' && cell != 'T') {
		//cout << "Setting player" << endl;
		s.player = cell;
	}
	//printStep(s);
	s.i += s.di;
	s.j += s.dj;
	if (!solved) performStep(board, s, solved, winner);
}

int evaluateBoard(const MatC &board) {
	bool solved = false;
	char winner = '.';

	for (int j = 0; j < 4; ++j) {
		Step s;
		s.i = 0;
		s.j = j;
		s.di = 1;
		s.dj = 0;
		s.player = '.';
		performStep(board, s, solved, winner);
	}

	for (int i = 0; i < 4; ++i) {
		Step s;
		s.i = i;
		s.j = 0;
		s.di = 0;
		s.dj = 1;
		s.player = '.';
		performStep(board, s, solved, winner);
	}

	Step s;
	s.i = 0;
	s.j = 0;
	s.di = 1;
	s.dj = 1;
	s.player = '.';
	performStep(board, s, solved, winner);

	s.i = 0;
	s.j = 3;
	s.di = 1;
	s.dj = -1;
	s.player = '.';
	performStep(board, s, solved, winner);


	//cout << "solved: " << solved << endl;
	//cout << "winner: " << winner << endl;
	//printBoard(board); cout << endl;

	if (solved) {
		if (winner == 'X') return 0;
		return 1;
	} else {
		bool found = false;
		for (int i = 0; i < 4; ++i) {
			if (found) break;
			for (int j = 0; j < 4; ++j) {
				if (board[i][j] == '.') {
					found = true;
					break;
				}
			}
		}
		if (found) return 2;
		return 3;
	}


}

int main () {

	int T;
	cin >> T;

	string row;
	getline(cin, row);
	int bcase = 0;

	while (bcase < T) {
		MatC board (4, vc(4));
		for (int i = 0; i < 4; ++i){
			getline(cin, row);
			for (int j = 0; j < 4; ++j) {
				board[i][j] = row[j];
			}
		}
		getline(cin, row);
		switch (evaluateBoard(board)) {
			case 0: cout << "Case #" << (bcase+1) << ": X won" << endl;
			break;
			case 1: cout << "Case #" << (bcase+1) << ": O won" << endl;
			break;
			case 2: cout << "Case #" << (bcase+1) << ": Game has not completed" << endl;
			break;
			case 3: cout << "Case #" << (bcase+1) << ": Draw" << endl;
			break;
		}
		++bcase;
	}

}