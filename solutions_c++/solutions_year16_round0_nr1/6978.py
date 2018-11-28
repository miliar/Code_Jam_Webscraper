#include <bits/stdc++.h>

using namespace std;

int main() {
	int i, j, k, tt, n, m;
	char used[10], un;
	scanf("%d", &tt);
	for (int cases = 1; cases <= tt; cases++) {
		fill(used, used + 10, 0);
		scanf("%d", &n);
		m = n;
		un = 10;
		for (i = 0; i < 100 && un; i++, m += n) {
			int t = m;
			while (t) {
				if (!used[t % 10]) {
					used[t % 10] = 1;
					--un;
				}
				t /= 10;
			}
		}
		printf("Case #%d: ", cases);
		if (un)
			puts("INSOMNIA");
		else
			printf("%d\n", m - n);
	}
	return 0;
}
