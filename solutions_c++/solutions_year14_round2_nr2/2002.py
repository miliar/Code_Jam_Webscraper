#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests, a, b, k;
	scanf("%d", &tests);

	for (int t = 1; t <= tests; t++) {
		scanf("%d %d %d", &a, &b, &k);

		long long count = 0;
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				count += ((i & j) < k);
			}
		}

		printf("Case #%d: %I64d\n", t, count);
	}

	return 0;
}