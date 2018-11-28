#include <bits/stdc++.h>

using namespace std;

int counter[2600];

int main() {
	freopen("inper.txt", "r", stdin);
	freopen("outer.txt", "w", stdout);
	int t, d, cnt = 0;
	scanf("%d", &t);
	while (t--) {
		cnt++;
		memset(counter, 0, sizeof counter);
		int n;
		scanf("%d", &n);
		for (int p = 0; p < 2 * n - 1; p++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &d);
				counter[d]++;
			}
		}
		printf("Case #%d: ", cnt);
		for (int i = 0; i < 2600; i++) {
			if (counter[i] & 1) {
				printf("%d ", i);
			}
		}
		printf("\n");
	}
}
