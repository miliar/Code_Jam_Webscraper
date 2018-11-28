#include <algorithm>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

long long n, p, q, r, S;
long long a[1000000 + 2];
long long s[1000000 + 2];
long long get(int i, int j) {
	return max(s[j] - s[i - 1], s[i - 1]);
}
void solve() {
	cin >> n >> p >> q >> r >> S;
	for (long long i = 1; i <= n; i++) {
		a[i] = (((i - 1) * p + q) % r) + S;
		s[i] = s[i - 1] + a[i];
	}
	//1 ... i-1 i j j+1 ... n
	//min{max{s[j]-s[i-1],s[i-1],s[n]-s[j]}}
	long long ans = s[n];
	for (int j = 1; j <= n; j++) {
		long long c = s[n] - s[j];
		int l = 1, r = j;
		while (l < r) {
			int ml = (l * 2 + r) / 3, mr = (l + r * 2) / 3;
			if (get(ml, j) < get(mr, j)) {
				r = mr - 1;
			} else if (get(ml, j) > get(mr, j)) {
				l = ml + 1;
			} else {
				r = mr - 1;
				l = ml + 1;
			}
		}
		for (int i : vector<int> { l, r, (l + r) / 2 }) {
			long long a = s[j] - s[i - 1];
			long long b = s[i - 1];
			long long get = max(a, max(b, c));
			ans = min(ans, get);
		}
	}
	printf(" %.10f\n", 1 - double(ans) / s[n]);
}

int main() {
	freopen("src/out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		printf("Case #%d:", t);
		solve();
	}
}
