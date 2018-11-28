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

int T, n, a[1005];

void solve() {
	cin >> n;
	REP(i, n) cin >> a[i];
	sort(a, a + n);
	int ans = (int)1e9;
	REP(i, 1001) if (i) {
		int cnt = 0;
		REP(j, n) cnt += (a[j] + i - 1) / i - 1;
		ans = min(ans, cnt + i);
	}
	static int z = 0;
	printf("Case #%d: %d\n", ++z, ans);
}

int main() {
	cin >> T;
	while (T--) solve();
	return 0;
}

