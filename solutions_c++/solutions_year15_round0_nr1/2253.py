#include <iostream>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define REP(i, n) for(int i(0); (i)<(int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= int(b); i++)

int T, n;
string s;

void solve() {
	cin >> n >> s;
	int ans = 0;
	int now = s[0] - '0';
	REP(i, n) {
		int y = s[i + 1] - '0';
		if (y) {
			ans = max(ans, i + 1 - now);
		}
		now += y;
	}
	static int z = 0;
	printf("Case #%d: %d\n", ++z, ans);
}

int main() {
	cin >> T;
	while (T--) solve();
	return 0;
}

