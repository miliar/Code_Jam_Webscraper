#include <bits/stdc++.h>

using namespace std;

int ar[1009];
int main() {
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++) {
		int n, mx = 0, mn = 99999;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &ar[i]), mx = max(ar[i], mx);
		while (mx) {
			int tot = 0;
			for (int i = 0; i < n; i++)
				if (ar[i] > mx) {
					tot += (ar[i] - mx) / mx + (ar[i] % mx != 0);
				}
			mn = min(mn, tot + mx);
			mx--;
		}
		printf("Case #%d: %d\n", T, mn);
	}

	return 0;
}
