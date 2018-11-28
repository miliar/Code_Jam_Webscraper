#include <cstdio>
#include <memory>

int casei, cases;
int n;
bool seen[10];

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", casei);
			continue;
		}
		memset(seen, false, sizeof seen);
		int cnt = 0;
		int m = n;
		while (true) {
			for (int tmp = m; tmp > 0; tmp /= 10) {
				int di = tmp % 10;
				if (!seen[di]) {
					seen[di] = true;
					++cnt;
				}
			}
			if (cnt == 10) break;
			m += n;
		}
		printf("Case #%d: %d\n", casei, m);
	}
	return 0;
}
