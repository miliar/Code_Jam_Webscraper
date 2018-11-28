#include <iostream>

using namespace std;

int board[100][100];
int maxrow[100];
int maxcol[100];

void doit() {
	int N, M;
	cin >> N >> M;
	
	
	
	for (int i = 0; i < N; ++i) {
		maxrow[i] = 0;
		for (int j = 0; j < M; ++j) {
			cin >> board[i][j];
			if (i == 0) maxcol[j] = 0;
			maxcol[j] = max(maxcol[j], board[i][j]);
			maxrow[i] = max(maxrow[i], board[i][j]);
		}
	}
	
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (board[i][j] != maxcol[j] && board[i][j] != maxrow[i]) {
				cout << "NO" << endl;
				return;
			}
		}
	}
	
	cout << "YES" << endl;
}

int main() {
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		doit();
	}
}
