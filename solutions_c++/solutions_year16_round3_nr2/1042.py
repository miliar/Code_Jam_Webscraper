#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <bitset>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <set>
#include <list>
#include <deque>
#include <functional>
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <assert.h>
#include <iomanip>
#include <unordered_map>

using namespace std;

int f[10][10], n, m, dp[10];
bool solved;

void go(int cur) {
	if (cur >= n)
		return;
	if (dp[n - 1] == m) {
		cout << "POSSIBLE" << endl;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)
				cout << f[i][j];
			cout << endl;
		}
		solved = true;
	}
	for (int i = 0; i < cur; i++) {
		if (!f[i][cur]) {
			f[i][cur] = 1;
			dp[cur] += dp[i];
			if (!solved) {
				go(cur);
				go(cur + 1);
			}
			f[i][cur] = 0;
			dp[cur] -= dp[i];
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("B-small-attempt0 (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				f[i][j] = dp[j] = 0;
		dp[0] = 1;
		solved = false;
		go(1);
		if (!solved)
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}