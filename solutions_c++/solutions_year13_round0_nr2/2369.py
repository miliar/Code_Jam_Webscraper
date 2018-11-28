#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

typedef vector<vector<int> > Board;

bool check(const Board &board, const vector<int> &maxColumn,
		const vector<int> &maxRow, size_t r, size_t c) {
	return board[r][c] == maxColumn[r] || board[r][c] == maxRow[c];
}

int maxElement(const Board &board, int c) {
	int a = 0;
	for (int r = 0; r < board.size(); ++r)
		a = max(a, board[r][c]);
	return a;
}

string calc(const Board &board) {
	vector<int> maxColumn(board.size()), maxRow(board[0].size());

	for (size_t i = 0; i < board.size(); ++i)
		maxColumn[i] = *max_element(board[i].begin(), board[i].end());

	for (size_t j = 0; j < board[0].size(); ++j)
		maxRow[j] = maxElement(board, j);

	for (size_t i = 0; i < board.size(); ++i)
		for (size_t j = 0; j < board[i].size(); ++j)
			if (!check(board, maxColumn, maxRow, i, j))
				return "NO";
	return "YES";
}

void solve(istream &in, ostream &out) {
	int T;
	in >> T;

	for (int t = 1; t <= T; ++t) {
		int N, M;
		in >> N >> M;
		Board board(N, vector<int>(M));
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				in >> board[i][j];

		out << "Case #" << t << ": " << calc(board) << endl;
	}
}

int main() {
	solve(cin, cout);
	return 0;
}
