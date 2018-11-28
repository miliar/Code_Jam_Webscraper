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

void solve(int tc) {
	int smax;
	string s;
	cin >> smax >> s;
	int cur = s[0] - '0', ans = 0;
	for (int i = 1; i <= smax; ++i) {
		int v = s[i] - '0';
		if (v == 0) continue;
		if (i > cur) {
			ans += i - cur;
			cur += i - cur;
		}
		cur += v;
	}
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

