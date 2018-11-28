#include <iostream> 
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <functional>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>
#include <unordered_map>

using namespace std;

using ld = long double;

ld dp[16][16];
ld b[16];

ld f(int i, int j) {
	if (i < 0 || j < 0) return 0;
	if (i + j == 0) return 1;
	ld p = b[i + j - 1];

	auto &res = dp[i][j];
	if (res >= 0) return res;

	return res = f(i - 1, j) * p + f(i, j - 1) * (1 - p);
}

ld solve() {
	int n, k;
	cin >> n >> k;
	vector<ld> a(n);
	for (int i = 0; i < n; ++i) cin >> a[i];

	ld ans = 0;
	for (int i = 0; i < (1 << n); ++i) {
		int cnt = 0;
		for (int j = 0; j < n; ++j) {
			if (i >> j & 1) {
				b[cnt++] = a[j];
			}
		}
		if (cnt != k) continue;
		for (int i = 0; i < 16; ++i)
			for (int j = 0; j < 16; ++j)
				dp[i][j] = -1;
		ans = max(ans, f(k / 2, k / 2));
	}
	return ans;
}

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);

	cout.setf(ios::fixed);
	cout.precision(9);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		cout << solve() << endl;
	}

}