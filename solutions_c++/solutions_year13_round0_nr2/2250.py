#include <iostream>
#include <vector>
using namespace std;

bool solve() {
	int N, M;
	cin >> N >> M;
	vector<vector<int> > lawn(N, vector<int>(M)), lawn2 = lawn;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			cin >> lawn[i][j];
		}
	}

	for (int i = 0; i < N; ++i) {
		int m = 0;
		for (int j = 0; j < M; ++j) {
			m = max(m, lawn[i][j]);
		}
		for (int j = 0; j < M; ++j)
			lawn2[i][j] = m;
	}

	for (int j = 0; j < M; ++j) {
		int m = 0;
		for (int i = 0; i < N; ++i) {
			m = max(m, lawn[i][j]);
		}
		for (int i = 0; i < N; ++i)
			lawn2[i][j] = min(m, lawn2[i][j]);
	}

	return lawn == lawn2;
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		cout << "Case #" << i+1 << ": " << (solve() ? "YES" : "NO") << endl;
	}
	return 0;
}
