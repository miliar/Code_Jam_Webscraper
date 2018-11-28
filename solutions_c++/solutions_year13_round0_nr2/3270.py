#include <iostream>

using namespace std;

int h[105][105];
int n, m;

bool exist(int r, int c) {
	int i;
	for (i = 0; i < m; i++) {
		if (h[r][i] > h[r][c])
			break;
	}
	if (i == m) return true;

	for (i = 0; i < n; i++) {
		if (h[i][c] > h[r][c])
			break;
	}
	if (i == n) return true;

	return false;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int  cas = 1; cas <= T; cas++) {
		cin >> n >> m;
		for (int i = 0; i < n; i++) for (int j = 0; j < m; j++)
			cin >> h[i][j];

		bool can = true;
		for (int i = 0; can && i < n; i++) for (int j = 0; j < m; j++) {
			if(!exist(i, j)) {
				can = false;
				break;
			}
		}

		if (can) cout << "Case #" << cas << ": YES\n";
		else cout << "Case #" << cas << ": NO\n";

	}

	// system("pause");
	return 0;
}