#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

int p[1100000];

int main() {
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t) {
		int d;
		scanf("%d", &d);

		int maxp = 0;
		for (int i = 0; i < d; ++i) {
			scanf("%d", &p[i]);
			maxp = max(p[i], maxp);
		}

		int sol = maxp;

		for (int i = 1; i <= maxp; ++i) {
			int minutes = 0;
			for (int j = 0; j < d; ++j) {
				minutes += p[j] / i + (p[j] % i ? 1 : 0) - 1;
				if (minutes > sol)
					break;
			}
			minutes += i;
			sol = min(sol, minutes);
		}

		printf("Case #%d: %d\n", t, sol);
	}

	return 0;
}