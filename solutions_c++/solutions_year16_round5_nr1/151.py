#include <functional>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>


using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long ll;

const int MAXK = -1;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;

int fastsolve(string s) {
	vector<char> v;
	int n = s.length();
	int ans = 0;
	for (int i = 0; i < n; i++) {
		if (!v.empty() && v.back() == s[i]) {
			ans += 10;
			v.pop_back();
		}
		else {
			v.push_back(s[i]);
		}
	}
	ans += 5 * (v.size() / 2);
	return ans;
}

int slowsolve(string s) {
	int n = s.length();
	vector<vector<int> > dp(n, vector<int>(n));
	for (int len = 2; len <= n; len += 2) {
		for (int i = 0; i + len <= n; i++) {
			int j = i + len - 1;
			dp[i][j] = 0;
			if (len == 2) {
				dp[i][j] = s[i] == s[j] ? 10 : 5;
			}
			else {
				for (int k = 1; k < len; k += 2) {
					int l1 = i + 1, r1 = i + k - 1;
					int dp1 = 0;
					if (l1 <= r1) dp1 = dp[l1][r1];
					int l2 = i + k + 1, r2 = j;
					int dp2 = 0;
					if (l2 <= r2) dp2 = dp[l2][r2];
					dp[i][j] = max(dp[i][j], (s[i] == s[i + k] ? 10 : 5) + dp1 + dp2);
				}
			}
		}
	}
	return dp[0][n - 1];
}

void stress() {
	for (int it = 0;; it++) {
		cerr << it << endl;
		int n = rand() % 30 * 2 + 2;
		string s = "";
		for (int i = 0; i < n; i++) s += (char)('a' + rand() % 2);
		int ans1 = fastsolve(s);
		int ans2 = slowsolve(s);
		if (ans1 != ans2) {
			cout << "EROOR" << endl;
			exit(0);
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	//stress();

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";
		
		string s;
		cin >> s;

		int ans = fastsolve(s);
		cout << ans << endl;
		cerr << ans << endl;
	}

	return 0;
}