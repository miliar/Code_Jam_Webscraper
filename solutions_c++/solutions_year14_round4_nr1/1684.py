#include <bits/stdc++.h>

using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)

int n, m;
int a[10000];

bool able(int discs) {
	// X * 2 + (n - 2 * X)
	// discs = X + (n - 2 * X) = n - X
	// discs = n - X, X = n - discs
	int x = n - discs;
	int i = 0, j = 2 * x - 1;

//	printf("\tdiscs = %d, x = %d\n", discs, x);
	if(n - 2 * x < 0) return false;

	while(i <= j) {
		if(a[i] + a[j] <= m);
		else return false;
		i ++; j --;
	}
//	printf("? discs = %d, [0, %d) %d %d\n", discs, x, i, j);
	return true;
}

int go() {
	sort(a, a + n);

	int l = 1, r = n;
	int ans = n;
	while(l <= r) {
		int mid = (l + r) / 2;
		if(able(mid)) {
			ans = mid;
			r = mid - 1;
		}
		else {
			l = mid + 1;
		}
	}
	return ans;
}

int main() {
	int T;
	cin.sync_with_stdio(false);

	cin >> T;
	for(int t = 1; t <= T; ++ t) {
		cin >> n >> m;
		REP(i, n) cin >> a[i];
		printf("Case #%d: %d\n", t, go());
	}
	return 0;
}
