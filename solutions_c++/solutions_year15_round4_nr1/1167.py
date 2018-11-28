#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	map <char, int> dx, dy;
	dx['^'] = -1;
	dx['v'] = 1;
	
	dy['>'] = 1;
	dy['<'] = -1;

	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		int n, m;
		cin >> n >> m;
		vector <string> arr(n);
		for (int i = 0; i < n; i++)
			cin >> arr[i];
		int ans = 0;
		bool can = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] == '.')
					continue;
				char c = arr[i][j];
				int nx = i + dx[c];
				int ny = j + dy[c];
				bool ok = false;
				while (1) {
					if (nx < 0 || nx >= n || ny < 0 || ny >= m)
						break;
					if (arr[nx][ny] != '.') {
						ok = true;
						break;
					}
					nx += dx[c];
					ny += dy[c];
				}
				if (!ok) {
					ans++;

					for (int x = 0; x < n; x++) {
						if (x != i && arr[x][j] != '.') {
							ok = true;
						}
					}

					for (int y = 0; y < m; y++) {
						if (y != j && arr[i][y] != '.') {
							ok = true;
						}
					}
					if (!ok) {
						can = false;
					}
				}
			}
		}

		if (!can) {
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << t + 1 << ": " << ans << endl;
		}
	}

	return 0;
}