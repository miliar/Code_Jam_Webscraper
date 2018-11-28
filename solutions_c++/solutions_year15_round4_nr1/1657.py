#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

int solve() {
	int r, c;
	cin >> r >> c;
	vector<vector<char>> map(r, vector<char>(c));
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			cin >> map[i][j];
	int ans = 0;
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j) {
			if (map[i][j] == '.')
				continue;
			bool to_some = false;
			bool any = false;
			for (int k = j + 1; k < c; ++k) {
				any |= map[i][k] != '.';
				to_some |= (map[i][j] == '>') && (map[i][k] != '.');
			}
			for (int k = j - 1; k >= 0; --k) {
				any |= map[i][k] != '.';
				to_some |= (map[i][j] == '<') && (map[i][k] != '.');
			}
			for (int k = i + 1; k < r; ++k) {
				any |= map[k][j] != '.';
				to_some |= (map[i][j] == 'v') && (map[k][j] != '.');
			}
			for (int k = i - 1; k >= 0; --k) {
				any |= map[k][j] != '.';
				to_some |= (map[i][j] == '^') && (map[k][j] != '.');
			}
			if (!any)
				return -1;
			if (!to_some)
				++ans;
		}
	return ans;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int ans = solve();
		cout << "Case #" << i + 1 << ": ";
		if (ans < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}