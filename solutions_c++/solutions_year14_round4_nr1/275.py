#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

const int MAX_N = 101010;
int a[MAX_N], n, X;

int main() {
	int n_case = 0;
	scanf("%d", &n_case);
	for (int ca = 1; ca <= n_case; ca++) {
		int ans = 0;
		scanf("%d%d", &n, &X);
		for (int i = 0; i < n; i++) {
			scanf("%d", a + i);
		}
		sort(a, a + n);
		int b = 0, e = n - 1;
		while (b <= e) {
			if (a[e] + a[b] <= X) {
				b++, e--, ans++;
			} else {
				e--, ans++;
			}
		}
		printf("Case #%d: %d\n", ca, ans);
	}
	return 0;
}
