#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <algorithm>
#include <assert.h>
#include <math.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
const int N = 1e6 + 10;
int z[N];

map<string, int> dp;

string oper(string s, int r) {
	for (int i = 0; i <= r; i++) {
		int j = r - i;
		if (i < j)
			swap(s[i], s[j]);

		if (s[i] == '-')
			s[i] = '+';
		else
			s[i] = '-';
	}
	return s;
}
int calc(string s) {
	if (dp.count(s)) {
		return dp[s];
	}
	if (s == string(s.length(), '+')) {
		return dp[s] = 0;
	}

	dp[s] = 15555555;
	int j = s.length() - 1;
	while (s[j] == '+') j--;
	

	for (int i = 0; i < j; i++) {
		if (s[i] == '+') {
			string ns = oper(s, i);
			assert(ns[0] == '-');
			ns = oper(ns, j);
			assert(ns[j] == '+');
			dp[s] = min(dp[s], 2 + calc(ns));
		}
	}

	if (s[0] == '-') {
		string ns = oper(s, j);
		assert(ns[j] == '+');
		dp[s] = min(dp[s], 1 + calc(ns));
	}
	return dp[s];
}


int calc2(string s) {
	int j = s.length() - 1;
	int ans = 0;
	while (true) {
		while (j >= 0 && s[j] == '+') j--;
		if (j < 0) break;
		int ii = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				ii = i;
				break;
			}
		}
		assert(s[j] == '-');

		if (ii) {
			ans++;
			s = oper(s, ii - 1);
		}
		assert(s[0] == '-');
		ans++;
		s = oper(s, j);
		assert(s[j] == '+');
	}

	return ans;
}

int main() {
#ifdef _DEBUG
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _DEBUG
	
	cout.sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		string s;
		cin >> s;
		cout << "Case #" << i + 1 << ": ";
		cout << calc2(s) << '\n';
	}
	return 0;
}