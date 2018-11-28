#include <iostream>
#include <vector>
using namespace std;
bool f() {
	int N, M;
	cin >> N >> M;
	vector<vector<int> > a(N, vector<int>(M));
	for (int i = 0; i < N; ++ i) {
		for (int j = 0; j < M; ++ j) {
			cin >> a[i][j];
		}
	}
	vector<int> b(N), c(M);
	for (int i = 0; i < N; ++ i) {
		for (int j = 0; j < M; ++ j) {
			b[i] = max(b[i], a[i][j]);
			c[j] = max(c[j], a[i][j]);
		}
	}
	vector<vector<int> > d(N, vector<int>(M, 1<<30));
	for (int i = 0; i < N; ++ i) {
		for (int j = 0; j < M; ++ j) {
			d[i][j] = min(b[i], c[j]);
		}
	}
	return a == d;
}
int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++ tt) {
		cout << "Case #" << tt << ": " << (f() ? "YES" : "NO") << endl;
	}
}
