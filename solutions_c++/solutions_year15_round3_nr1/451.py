#include <cstdio>
#include <cstring>

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas) {
		int r, c, w;
		scanf("%d%d%d", &r, &c, &w);
		int ret = c / w * r + w - 1;
		if (c % w > 0) ret += 1;
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}

