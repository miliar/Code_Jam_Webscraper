#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)
#define N 1001010

int T, n, a[N];

int calc(int x) {
    int ans = 0;
    rep(i, n) ans += (a[i] - 1) / x;
    return ans;
}

void solve() {
	scanf("%d ", &n);
	int maxn = 0;
	rep(i, n) {
	    scanf("%d", a+i);
	    maxn = max(a[i], maxn);
	}
	int ans = maxn;
	for (int i = 1; i <= maxn; ++i) {
        ans = min(calc(i) + i, ans);
	}
	cout << ans << endl;
}

int main() {
	freopen("B-large.in", "r", stdin );
	freopen("b.ou", "w", stdout);
	ios::sync_with_stdio(false);
	scanf("%d", &T);
	kep(_, T) {
		cout << "Case #" << _ << ": ";
		solve();
	}
}
