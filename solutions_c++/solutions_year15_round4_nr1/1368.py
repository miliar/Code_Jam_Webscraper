#include <bits/stdc++.h>
using namespace std;
int main() {
	static int DI[256], DJ[256];
	DI['v'] = 1, DJ['v'] = 0;
	DI['>'] = 0, DJ['>'] = 1;
	DI['^'] = -1, DJ['^'] = 0;
	DI['<'] = 0, DJ['<'] = -1;
	const char *DIRS = "v>^<";

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";

		int R, C;
		char a[100][100];
		cin >> R >> C;
		for (int i = 0; i < R; ++i)
			for (int j = 0; j < C; ++j)
				cin >> a[i][j];
		int edge = 0;
		for (int i = 0; i < R; ++i)
			for (int j = 0; j < C; ++j) {
				if (a[i][j] == '.')
					continue;
				char succ[256];
				for (const char *dir = DIRS; *dir; ++dir) {
					const int di = DI[*dir], dj = DJ[*dir];
					for (int k = 1;; ++k) {
						const int i2 = i + k * di, j2 = j + k * dj;
						//cerr << "k=" << k << " " << i2 << ", " << j2 << " ";
						if (!(0 <= i2 && i2 < R && 0 <= j2 && j2 < C))
							succ[*dir] = 0;
						else if (a[i2][j2] != '.')
							succ[*dir] = a[i2][j2];
						else
							continue; // '.'
						break;
					}
					//cerr << i << ", " << j << ": " << *dir << " => " << succ[*dir] << endl;
				}
				if (succ[a[i][j]] == 0) { // arrow to edge
					for (const char *dir = DIRS; *dir; ++dir)
						if (*dir != a[i][j] && succ[*dir])
							goto found; // other arrow to change to
					// failed
					goto impossible;
found:
					++edge;
				}
			}
		cout << edge << endl;
		continue;
impossible:
		cout << "IMPOSSIBLE" << endl;
	}
}
