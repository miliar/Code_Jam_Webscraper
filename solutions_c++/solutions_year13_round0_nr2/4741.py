#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

bool valid(int n, int m, bool grid[][100]) {
	bool mark[100][100] = {{false}};

	for (int i = 0; i < n; i++) {
		int cnt = 0;
		for (int j = 0; j < m; j++)
			cnt += grid[i][j];
		if (cnt == m)
			for (int j = 0; j < m; j++)
				mark[i][j] = true;
	}

	for (int i = 0; i < m; i++) {
		int cnt = 0;
		for (int j = 0; j < n; j++)
			cnt += grid[j][i];
		if (cnt == n)
			for (int j = 0; j < n; j++)
				mark[j][i] = true;
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (grid[i][j] && !mark[i][j])
				return false;
	return true;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int num_tests;
	cin >> num_tests;

	for (int test_id = 1; test_id <= num_tests; test_id++) {
		int n, m, a[100][100];
		vector< int > v;

		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				cin >> a[i][j];
				v.push_back(a[i][j]);
			}

		sort(v.begin(), v.end());
		v.resize(unique(v.begin(), v.end()) - v.begin());

		bool good = true, grid[100][100] = {{false}};
		for (int i = 0; i < v.size(); i++) {
			for (int x = 0; x < n; x++)
				for (int y = 0; y < m; y++)
					grid[x][y] = (a[x][y] <= v[i]);
			if (!valid(n, m, grid)) {
				good = false;
				break;
			}
		}

		cout << "Case #" << test_id << ": " << ((good)? "YES": "NO") << endl;
	}
	return 0;
}
