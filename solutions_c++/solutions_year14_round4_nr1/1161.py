#include <bits/stdc++.h>
using namespace std;

const int N = 10005;

int n, x, a[N];

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; ++i) scanf("%d", a+i);
		sort(a, a+n);
		reverse(a, a+n);
		int k = n-1;
		for (int i = 0; i < k; ++i) {
			if (a[i] + a[k] <= x) --k;
		}
		printf("Case #%d: %d\n", cas, k+1);
	}
}
