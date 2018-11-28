#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <climits>
using namespace std;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t;
	cin >> t;
	for (int l = 0; l < t; l++) {
		int n, m;
		cin >> n >> m;
		int graph[105][105], maxh[105], maxz[105];
		memset(maxh, -1, sizeof(maxh));
		memset(maxz, -1, sizeof(maxz));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> graph[i][j];
				if (graph[i][j] > maxh[i]) maxh[i] = graph[i][j];
				if (graph[i][j] > maxz[j]) maxz[j] = graph[i][j];
			}
		}
		bool can = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (maxh[i] > graph[i][j] && maxz[j] > graph[i][j]) can = false;
			}
		}
		if (can) cout << "Case #" << l + 1 << ": YES\n";
		else cout << "Case #" << l + 1 << ": NO\n";
	}
	return 0;
}

