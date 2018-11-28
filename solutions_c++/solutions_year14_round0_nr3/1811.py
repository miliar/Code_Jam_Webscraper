#include <bits/stdc++.h>
using namespace std;
void func() {
	int R, C, M;
	cin >> R >> C >> M;
	for (int p = 0; p < 1<<(R*C); ++ p) if (__builtin_popcount(p) == M) {
		vector<string> a(R, string(C, '#'));
		int pp = p;
		for (int i = 0; i < R; ++ i) for (int j = 0; j < C; ++ j) {
			a[i][j] = (pp&1) ? '*' : '#'; pp >>= 1;
		}
		
		for (int i = 0; i < R; ++ i) {
			for (int j = 0; j < C; ++ j) {
				if (a[i][j] == '#') {
					auto b = a;
					b[i][j] = 'c';
					queue<pair<int,int>> Q;
					Q.push(make_pair(i,j));
					while (!Q.empty()) {
						auto k = Q.front(); Q.pop();
						int c = 0;
						for (int di = -1; di <= 1; ++ di) for (int dj = -1; dj <= 1; ++ dj) {
							int ii = k.first + di, jj = k.second + dj;
							if (0 <= ii && ii < R && 0 <= jj && jj < C && a[ii][jj] == '*') ++ c;
						}
						if (c > 0) continue;
						for (int di = -1; di <= 1; ++ di) for (int dj = -1; dj <= 1; ++ dj) {
							int ii = k.first + di, jj = k.second + dj;
							if (0 <= ii && ii < R && 0 <= jj && jj < C && b[ii][jj] == '#') {
								Q.push(make_pair(ii,jj));
								b[ii][jj] = '.';
							}
						}
					}
					bool f = true;
					for (int i = 0; i < R; ++ i) for (int j = 0; j < C; ++ j) if (b[i][j] == '#') f = false;
					if (f) {
						for (int i = 0; i < R; ++ i) cout << b[i] << endl;
						return;
					}
				}
			}
		}
	}
	cout << "Impossible" << endl;
}
int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++ tt) {
		cout << "Case #" << tt << ": " << endl;
		func();
	}
}
