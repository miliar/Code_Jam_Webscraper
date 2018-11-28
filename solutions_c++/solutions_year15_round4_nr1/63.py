#include <iostream>
using namespace std;

char grid[100][100];

inline bool isarrow(int i, int j) {
	char c = grid[i][j];
	return c == '^' || c == 'v' || c == '<' || c == '>';
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int R, C;
		cin >> R >> C;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				cin >> grid[i][j];
			}
		}

		int bad = 0;
		bool impossible = false;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (!isarrow(i, j)) continue;

				int rowarrows = 0;
				int colarrows = 0;
				for (int k = 0; k < C; k++) if (isarrow(i, k)) rowarrows++;
				for (int k = 0; k < R; k++) if (isarrow(k, j)) colarrows++;

				if (isarrow(i, j) && rowarrows == 1 && colarrows == 1) impossible = true;

				bool good = false;
				switch (grid[i][j]) {
					case '^':
						for (int k = 0; k < i; k++) good = good || isarrow(k, j);
						break;
					case 'v':
						for (int k = i+1; k < R; k++) good = good || isarrow(k, j);
						break;
					case '<':
						for (int k = 0; k < j; k++) good = good || isarrow(i, k);
						break;
					case '>':
						for (int k = j+1; k < C; k++) good = good || isarrow(i, k);
						break;
				}
				if (!good) bad++;
			}
		}

		cout << "Case #" << t << ": ";
		if (impossible) cout << "IMPOSSIBLE\n";
		else cout << bad << '\n';
	}

	return 0;
}
