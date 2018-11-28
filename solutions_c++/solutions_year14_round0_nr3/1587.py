#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <queue>

using namespace std;

const char EMPTY = '.';
const char MINE  = '*';

typedef bool bolle;

void print_board(vector<vector<char> > board) {
	int Y = board.size();
	if (Y == 0) return;

	int X = board[0].size();

	for (int i=0; i<Y; i++) {
		for (int j=0; j<X; j++) {
			cout << board[i][j];
		}
		cout << endl;
	}
}

bolle is_mine(vector<vector<char> > board, int i, int j) {
	if (i < 0 || i>=board.size())
		return false;
	else if (j < 0 || j>=board[i].size())
		return false;

	if (board[i][j] == MINE)
		return true;

	return false;
}

bolle surrounded_by_mine(vector<vector<char> > board, int i, int j) {
	bolle surrounded=false;
	surrounded = surrounded || is_mine(board, i+1, j);   // NICE
	surrounded = surrounded || is_mine(board, i-1, j);   // NICE
	surrounded = surrounded || is_mine(board, i,   j+1); // NICE
	surrounded = surrounded || is_mine(board, i,   j-1); // NICE
	surrounded = surrounded || is_mine(board, i+1, j+1); // NICE
	surrounded = surrounded || is_mine(board, i-1, j-1); // NICE
	surrounded = surrounded || is_mine(board, i+1, j-1); // NICE
	surrounded = surrounded || is_mine(board, i-1, j+1); // NICE
	return surrounded;
}

int reachable(vector<vector<char> > board, int row, int col) {
	if (row < 0 || row>=board.size() || col < 0 || col>=board[0].size())
		return 0;

	if (board[row][col] != EMPTY)
		return 0;

	else {
		if (surrounded_by_mine(board, row, col))
			return 1;

		bool visited[board.size()][board[0].size()];
		for (int R=0; R<board.size(); R++) {
			for (int C=0; C<board[0].size(); C++) {
				visited[R][C] = false;
			}
		}

		queue<int> row_q;
		queue<int> col_q;

		row_q.push(row);
		col_q.push(col);		

		int reach=0;

		while (!row_q.empty()) {
			int R = row_q.front(); row_q.pop();
			int C = col_q.front(); col_q.pop();

			if (R < 0 || R >= board.size() || visited[R][C]) continue;
			if (C < 0 || C >= board[0].size()) continue;

			visited[R][C] = true;

			if (board[R][C] == EMPTY)
				reach++;

			if (!surrounded_by_mine(board, R, C)) {
				row_q.push(R+1); col_q.push(C);  
				row_q.push(R-1); col_q.push(C);  
				row_q.push(R  ); col_q.push(C+1);
				row_q.push(R  ); col_q.push(C-1);
				row_q.push(R+1); col_q.push(C+1);
				row_q.push(R-1); col_q.push(C-1);
				row_q.push(R+1); col_q.push(C-1);
				row_q.push(R-1); col_q.push(C+1);
			}
		}
		return reach;
	}
}

vector<vector<char> > solve(vector<vector<char> > board, int R, int C, int next_R, int next_C, int mines, int should_be_empty) {

	if (next_R >= R && next_C >= C) {
		goto empty;
	}

	if (mines==0) {
		for (int row=0; row<R; row++) {
			for (int col=0; col<C; col++) {
				if (board[row][col] == EMPTY) {
					if (reachable(board, row, col) == should_be_empty) {
						board[row][col] = 'c';
						return board;
					}
				}
			}
		}

		goto empty;
	}

	for (int row=next_R; row<R; row++) {
		for (int col=next_C; col<C; col++) {
			if (board[row][col] == MINE) continue;
			board[row][col] = MINE;
			vector<vector<char> > solution = solve(board, R, C, row, col+1, mines-1, should_be_empty);
			if (solution.size() > 0) { return solution; } // found a solution
			else { board[row][col] = EMPTY; } // no solution, remove mine and go on
		}
		next_C = 0;
	}

	empty:
	vector<vector<char> > empty_board;
	return empty_board;
}

int main(void) {
	int cases; cin >> cases;
	int case_number=0;

	while (cases-->0) {
		case_number++;
		int R,C,M; cin >> R >> C >> M;

		cout << "Case #" << case_number << ": " << endl;

		if (R*C <= M) {
			cout << "Impossible" << endl;
			continue;
		}

		vector<vector<char> > board;
		for (int i=0; i<R; i++) {
			vector<char> tmp(C, EMPTY);
			board.push_back(tmp);
		}

		vector<vector<char> > solution = solve(board, R, C, 0, 0, M, R*C-M);

		if (solution.size() > 0) {
			print_board(solution);
		}
		else {
			cout << "Impossible" << endl;
		}
	}
}