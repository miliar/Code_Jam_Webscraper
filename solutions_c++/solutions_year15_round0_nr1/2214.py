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

int T;
int n, a[N];

void solve() {
	scanf("%d ", &n);
	char c = getchar();
	int j = 0;
	while (c >= '0' && c <= '9') {
		a[j++] = c - '0';
		c = getchar();
	}
	int ans = 0, cur = 0;
	for (int i = 0; i <=n; ++i) {
		if (cur < i) ans += i-cur;
		cur = max(cur, i);
		cur += a[i];
	}

	cout << ans << endl;
}

int main() {
	freopen("A-large.in", "r", stdin );
	freopen("a.ou", "w", stdout);
	ios::sync_with_stdio(false);
	scanf("%d", &T);
	kep(_, T) {
		cout << "Case #" << _ << ": ";
		solve();
	}
}
