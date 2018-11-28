#include <cstdio>

using namespace std;

int main() {
	freopen("tiles.in", "r", stdin);
	freopen("tiles.out", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; ++i) {
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);

		printf("Case #%d: ", i);
		for (int j = 1; j <= s; ++j)
			printf("%d ", j);
		printf("\n");
	}

	return 0;
}
