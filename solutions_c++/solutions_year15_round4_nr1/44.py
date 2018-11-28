#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;


string arr[120];
int n, m;

vector<int> check(int x, int y) {
	vector<int> ans = {0, 0, 0, 0};
	for (int i = x + 1; i < n; ++i)
		if (arr[i][y] != '.')
			ans[2] = 1;
	for (int i = x - 1; i >= 0; --i)
		if (arr[i][y] != '.')
			ans[0] = 1;
	for (int i = y + 1; i < m; ++i)
		if (arr[x][i] != '.')
			ans[1] = 1;
	for (int i = y - 1; i >= 0; --i)
		if (arr[x][i] != '.')
			ans[3] = 1;
	return ans;
}


int solve() {
	int cnt = 0;
	cin >> n >> m;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (arr[i][j] != '.') {
				vector<int> now = check(i, j);
				if (now[0] == 0 && now[1] == 0 && now[2] == 0 && now[3] == 0)
					return -1;
				++cnt;
				if (arr[i][j] == '^' && now[0])
					--cnt;
				else if (arr[i][j] == '>' && now[1])
					--cnt;
				else if (arr[i][j] == 'v' && now[2])
					--cnt;
				else if (arr[i][j] == '<' && now[3])
					--cnt;
			}
		}
	}
	return cnt;
}


int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		int ans = solve();
		if (ans != -1)
			cout << "Case #" << i + 1 << ": " << ans << "\n";
		else
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << "\n";
	}
	return 0;
}


