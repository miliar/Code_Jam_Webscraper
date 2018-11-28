#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <string>

using namespace std;

typedef long long i64;

bool check(vector <string> arr) {
	int n = arr.size();

	for (int i = 0; i < n; i++) {
		bool ok = false;
		for (int j = 0; j < n; j++)
			if (arr[i][j] == '1')
				ok = true;
		if (!ok)
			return false;
	}

	bool ok = true;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (arr[i][j] == '0') {
				ok = false;
				break;
			}
	if (ok)
		return true;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (arr[i][j] == '1') {
				int cnt = 0;
				for (int k = 0; k < n; k++) {
					if (arr[i][k] == '1')
						cnt++;
					if (arr[k][j] == '1')
						cnt++;
				}
				if (cnt == 2)
					arr[i][j] = '0';
			}
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			bool triple = true;
			for (int x = 0; x < n; x++)
				for (int y = 0; y < n; y++) {
					if (x != i && y != j && arr[x][y] == '0') {
						triple = false;
						break;
					}
					if ((x == i || y == j) && arr[x][y] == '1') {
						triple = false;
						break;
					}
				}
			if (triple)
			return true;
		}

	for (int i = 0; i < n; i++) {
		int cnt = 0;
		for (int j = 0; j < n; j++)
			if (arr[i][j] == '1')
				cnt++;
		if (cnt > 2)
			return false;
	}

	for (int i = 0; i < n; i++) {
		int cnt = 0;
		for (int j = 0; j < n; j++)
			if (arr[j][i] == '1')
				cnt++;
		if (cnt > 2)
			return false;
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			for (int x = 0; x < n; x++)
				for (int y = 0; y < n; y++)
					if (i != x && j != y) {
						if (arr[i][j] == '1' && arr[i][y] == '1' && arr[x][j] == '1' && arr[x][y] == '1') {
							arr[i][j] = arr[i][y] = arr[x][j] = arr[x][y] = '0';
						}
					}
		}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (arr[i][j] != '0')
				return false;
	return true;
}

int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		int n;
		int ans = 1e9;
		cin >> n;
		vector <string> arr(n);
		for (int i = 0; i < n; i++)
			cin >> arr[i];
		for (int mask = 0; mask < (1 << (n * n)); mask++) {
			vector <string> cur = arr;
			int cost = 0;
			bool ok = true;
			for (int j = 0; j < n * n; j++) {
				int x = j / n;
				int y = j % n;
				bool initv = (arr[x][y] == '1');
				bool nowv = (mask & (1 << j));
				if (initv && !nowv) {
					ok = false;
					break;
				}
				if (nowv && !initv) {
					cur[x][y] = '1';
					cost++;
				}
			}
			if (!ok)
				continue;
			if (check(cur))
				ans = min(ans, cost);
		}
		printf("Case #%d: %d\n", t, ans);
	}
}
