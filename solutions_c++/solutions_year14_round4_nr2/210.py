#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdio>
using namespace std;

const int N = 1000;
int a[N], f[N + 1][N + 1], b[N], n;

int main() {
	int nTest; cin >> nTest;
	for(int test = 0; test < nTest; ++test) {
		int n; cin >> n;
		for(int i = 0; i < n; ++i) cin >> a[i];
		copy(a, a + n, b);
		sort(b, b + n);
		fill_n(f[n], n + 1, 0);
		for(int i = n - 1; i >= 0; --i) {
			int pos = find(a, a + n, b[i]) - a;
			for(int j = pos - 1; j >= 0; --j) if(a[j] < b[i]) --pos;
			for(int left = 0; left <= i; ++left)
				f[i][left] = min(f[i + 1][left + 1] + pos, f[i + 1][left] + n - i - 1 - pos);
		}
		printf("Case #%d: %d\n", test + 1, f[0][0]);
	}
	return 0;
}
