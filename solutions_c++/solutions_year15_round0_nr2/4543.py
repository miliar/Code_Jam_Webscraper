#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

map< vector<int>, int > dp;

int back(vector<int> P) {
	sort(P.begin(), P.end(), greater<int>());
	if (dp.count(P))
		return dp[P];
	int ret = P[0];
	for (int i = 0; i < P.size(); ++i) {
		for (int j = 1; j < P[i]; ++j) {
			vector<int> cur = P;
			cur.push_back(j);
			cur.push_back(cur[i] - j);
			cur.erase(cur.begin() + i);
			ret = min(ret, 1 + back(cur));
		}
	}
	return dp[P] = ret;
}

void solve(int tc) {
	int D;
	cin >> D;
	vector<int> P;
	for (int i = 0, x; i < D; ++i) {
		cin >> x;
		P.push_back(x);
	}
	dp.clear();
	int ans = back(P);
	cout << "Case #" << tc << ": " << ans << '\n';
}

int main() {
	ios_base::sync_with_stdio(0);
	#ifdef ACMTUYO
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
		clock_t start = clock();
	#endif
	
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc)
		solve(tc);
	
	#ifdef ACMTUYO
		fprintf(stderr, "\ntime=%.3lfsec\n", 1. * (clock() - start) / CLOCKS_PER_SEC);
	#endif
	return 0;
}

