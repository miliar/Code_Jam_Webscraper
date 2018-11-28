#include <iostream>
#include <cassert>

using namespace std;

int N, M;
int a[100][100];
int row[100];
int col[100];

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> N >> M;
		assert(N > 0 && N <= 100);
		assert(M > 0 && M <= 100);
		for (int i = 0; i < N; i++) row[i] = 0;
		for (int j = 0; j < M; j++) col[j] = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cin >> a[i][j];
				row[i] = max(row[i], a[i][j]);
				col[j] = max(col[j], a[i][j]);
			}
		}
		bool success = true;
		for (int i = 0; i < N && success; i++) {
			for (int j = 0; j < M && success; j++) {
				if (a[i][j] < row[i] && a[i][j] < col[j])
					success = false;
			}
		}
		cout << "Case #" << (t + 1) << ": " << (success ? "YES" : "NO") << endl;
	}
	return 0;
}
