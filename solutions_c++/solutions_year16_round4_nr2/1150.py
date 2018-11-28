#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int itc;

void solve() {
	int n;
	cin >> n;
	int k;
	cin >> k;
	vector<long double> a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	long double ans = 0;
	int N = 1<<n;
	vector<vector<long double>> b(N);
	b[0].assign(1, 1);
	for (int M = 1; M < N; M++) {
		int m = __builtin_popcount(M);
		if (m > k) continue;
		int M1 = M & M-1;
		int lsb = __builtin_ctz(M);
		b[M].assign(m+1, 0);
		for (int j = 0; j < m; j++) {
			b[M][j] += (1-a[lsb])*b[M1][j];
			b[M][j+1] += (a[lsb])*b[M1][j];
		}
		if (m == k) {
			ans = max(ans, b[M][k/2]);
		}
	}
	printf("%Lf\n", ans);
}

int main() {
	cin.sync_with_stdio(false);
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d: ", itc);
		solve();
	}
}
