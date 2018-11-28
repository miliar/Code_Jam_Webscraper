#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <set>

using namespace std;

int a[1100];
int b[1100];
int pos[1100];
int f[1100];
int g[1100];
int h[1100][1100];
int n;

int dp(int l, int r) {
	if (h[l][r] != -1)
		return h[l][r];
	int& ret = h[l][r];
	if (l == r)
		return 0;
	int p = pos[n - r + l];
	return ret = min(dp(l + 1, r) + f[p], dp(l, r - 1) + g[p]);
}

void work() {
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	for (int i = 0; i < n; i++)
		b[i] = a[i];
	sort(b, b + n);
	for (int i = 0; i < n; i++)
		a[i] = lower_bound(b, b + n, a[i]) - b;
	for (int i = 0; i < n; i++)
		pos[a[i]] = i;

	memset(f, 0, sizeof(f));
	memset(g, 0, sizeof(g));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++)
			if (a[j] > a[i])
				f[i]++;
	}
	for (int i = n - 1; i >= 0; i--) {
		for (int j = i + 1; j < n; j++)
			if (a[j] > a[i])
				g[i]++;
	}
	memset(h, -1, sizeof(h));
	cout << dp(0, n) << endl;
}


int main() {
	freopen("G:/1.in", "r", stdin);
	freopen("G:/1.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		work();
	}

	return 0;
}
