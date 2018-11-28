#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int i, j, k;
	int T;
	int D;
	int plates[2000];

	scanf("%d", &T);

	for (i = 0; i < T; ++i) {
		scanf("%d", &D);

		int maximum = 0;
		for (j = 0; j < D; ++j) {
			scanf("%d", &plates[j]);
			maximum = max(plates[j], maximum);
		}

		int min_minute = 10000;

		for (j = maximum; j >= 1; --j) {
			int morem = 0;
			for (k = 0; k < D; ++k) {
				if (plates[k] > j) {
					int d = plates[k] / j;
					if ((plates[k] + d - 1) / d <= j)
						morem += d - 1;
					else
						morem += d;
				}
			}

			min_minute = min(min_minute, morem + j);
			//printf("with %d dishes: %d minute\n", j, morem + j);
		}

		printf("Case #%d: %d\n", i + 1, min_minute);
	}
}