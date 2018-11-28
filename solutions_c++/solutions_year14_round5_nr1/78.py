#include <bits/stdc++.h>
using namespace std;

const int N = (int) 1e6;
int a[N], n, p, q, r, s;
long long sum[N + 1];

long long get(int x, int y) {
	return sum[y] - sum[x];
}

int main() {
	int testCount; cin >> testCount;
	for(int testID = 0; testID < testCount; ++testID) {
		cin >> n >> p >> q >> r >> s;
		for(int i = 0; i < n; ++i) a[i] = (1LL * i * p + q) % r + s;
		for(int i = 0; i < n; ++i) sum[i + 1] = sum[i] + a[i];
		long long res = sum[n];
		for(int x = 0; x < n; ++x) {
			int low = x + 1, high = n;
			while(low < high) {
				int mid = (low + high) / 2;
				if(max(get(x, mid), get(mid, n)) <= max(get(x, mid + 1), get(mid + 1, n)))
					high = mid;
				else
					low = mid + 1;
			}
			res = min(res, max(get(0, x), max(get(x, low), get(low, n))));
		}
		printf("Case #%d: %.12lf\n", testID + 1, 1 - (double) res / sum[n]);
	}
	return 0;
}
