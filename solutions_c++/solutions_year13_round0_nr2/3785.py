#include <iostream>
using namespace std;

int M,N;
int board[100][100];
int maxRow[100]; // N
int maxCol[100]; // M

void read_input() {
	cin >> N >> M;
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			cin >> board[i][j];
}

void print_board() {
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			cout << board[i][j] << " ";
		}
		cout << "\n";
	}
}

bool posible() {
	int max;

	/// Find max on each row
	for (int i = 0; i < N; ++i) {
		max = -1;
		for (int j = 0; j < M; ++j)
			if (board[i][j] > max) max = board[i][j];
		maxRow[i] = max;
	}

	/// Find max on each column
	for (int i = 0; i < M; ++i) {
		max = -1;
		for (int j = 0; j < N; ++j)
			if (board[j][i] > max) max = board[j][i];
		maxCol[i] = max;
	}

	/// If have one break constrain return false
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if ((board[i][j]<maxRow[i]) && (board[i][j]<maxCol[j]))
				return false;
		}
	}
	return true;
}

int main(int argc, char const *argv[])
{
	int t, T;

	cin >> T;

	for (t = 1; t <= T; ++t) {
		read_input();
		//print_board();

		cout << "Case #" << t << ": ";
		cout << (posible()? "YES" : "NO") << "\n";
	}

	return 0;
}