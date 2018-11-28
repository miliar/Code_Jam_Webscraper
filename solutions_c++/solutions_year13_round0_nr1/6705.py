#include <string>
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <numeric>
#include <vector>

#define INT(i) int i; { string line; getline(std::cin, line); stringstream stream(line); stream >> i; } 
#define LINE(l) string l; getline(std::cin, l);

#define INT_LINE_SINGLE(i) int i; { string line; getline(std::cin, line); stringstream stream(line); stream >> i; } 
#define INT_LINE_LIST(v, s) vector<int> v; { string line; getline(std::cin, line); stringstream stream(line); int n; while(stream >> n) { v.push_back(n); } }
#define INT_LINE_LIST_N(v, s, n) vector<int> v; { string line; getline(std::cin, line); stringstream stream(line); int i, x = 0; while(x++ < n && stream >> i) { v.push_back(i); } }

using namespace std;

bool hasWon(char c, vector<vector<char>> board);
void process(int c, vector<vector<char>> board);

int main(void) {
	INT_LINE_SINGLE(cases);

	for(int c = 0; c < cases; c++){
		vector<vector<char>> board;
		board.resize(4);

		for(int y = 0; y < 4; y++) {
			LINE(l);
			board[y].resize(4);
			for(int x = 0; x < 4; x++) {
				board[y][x] = l.at(x);
			}
		}

		LINE(x);

		process(c + 1, board);
	}

	return 0;
}

void process(int c, vector<vector<char>> board)
{
	string r;

	bool hasXWon = hasWon('X', board);
	bool hasOWon = hasWon('O', board);

	if(hasXWon && hasOWon) {
		r = "Draw";
	} else if(hasXWon == hasOWon) {
		if(all_of(board.begin(), board.end(), [](vector<char> row) { return all_of(row.begin(), row.end(), [](char c) { return c != '.'; }); })) {
			r = "Draw";
		} else{
			r = "Game has not completed";
		}
	} else if (hasXWon) {
		r = "X won";
	} else {
		r = "O won";
	}

	printf("Case #%i: %s\n", c, r.c_str());
}

bool hasWon(char player, vector<vector<char>> board)
{
	// check rows
	if(any_of(board.begin(), board.end(), [player](vector<char> row) { return all_of(row.begin(), row.end(), [player](char c) { return c == 'T' || c == player; }); })) {
		return true;
	}

	// check cols
	for(int x = 0; x < 4; x++) {
		if(all_of(board.begin(), board.end(), [player, x](vector<char> row) { char c = row[x]; return c == 'T' || c == player; })) {
			return true;
		}
	}

	// check diags
	bool diag1Valid = true;
	bool diag2Valid = true;
	for(int i = 0; i < 4; i++) {
		int j = 3 - i;

		char x1 = board[i][i];
		char x2 = board[i][j];

		if(board[i][i] != 'T' && board[i][i] != player) {
			diag1Valid = false;
		}
		if(board[i][j] != 'T' && board[i][j] != player) {
			diag2Valid = false;
		}
	}

	return diag1Valid || diag2Valid;
}