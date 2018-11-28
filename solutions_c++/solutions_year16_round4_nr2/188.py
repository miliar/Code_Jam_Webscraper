#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <numeric>
#include <memory.h>
#define mp make_pair
#define pii pair <int, int>
#define ll long long
#define ui unsigned int
#define ld double
#define pll pair <ll, ll> 
 
using namespace std;

const int maxn = 210;

ld v[maxn];
ld dp[maxn][2 * maxn];
bool st[maxn][2 * maxn];

int n, k;

vector <ld> r;

ld get_dp(int pos, int x) {
	if (!st[pos][x]) {
		st[pos][x] = true;

		if (pos == (int)r.size()) {
			if (x == 200) {
				dp[pos][x] = 1.0;
			} else {
				dp[pos][x] = 0.0;
			}
		} else {
			dp[pos][x] = r[pos] * get_dp(pos + 1, x + 1) + (1 - r[pos]) * get_dp(pos + 1, x - 1);
		}
	}

	return dp[pos][x];
}

ld go(int a) {
	r.clear();

	for (int i = 0; i < a; i++) {
		r.push_back(v[i]);
	}

	a = k - a;

	for (int i = n - 1; i >= n - a; i--) {
		r.push_back(v[i]);
	}

	memset(st, 0, sizeof st);

	return get_dp(0, 200);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	int ts = 0;

	while (t--) {
		ts++;

		scanf("%d %d", &n, &k);

		for (int i = 0; i < n; i++) {
			scanf("%lf", &v[i]);
		}

		sort(v, v + n);

		printf("Case #%d: ", ts);

		ld ver = 0.0;

		for (int i = 0; i <= k; i++) {
			ver = max(ver, go(i));
		}

		printf("%.10lf\n", ver);
	}

	return 0;
}
