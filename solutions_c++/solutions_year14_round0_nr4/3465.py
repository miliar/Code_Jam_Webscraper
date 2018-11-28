#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T;
	int i;
	scanf("%d", &T);
	double naomi[1001];
	double ken[1001];

	for (i = 0; i < T; ++i) {
		int N;
		scanf("%d", &N);
		int j;

		for (j = 0; j < N; ++j) {
			scanf("%lf", &naomi[j]);
		}
		for (j = 0; j < N; ++j) {
			scanf("%lf", &ken[j]);
		}

		sort(naomi, &naomi[N]);
		sort(ken, &ken[N]);

		int now = 0;
		int k;
		int res1 = 0;
		for (j = 0; j < N; ++j) {
			for (k = now; k < N; ++k) {
				if (naomi[k] > ken[j]) {
					++res1;
					break;
				}
			}
			now = k + 1;
		}

		now = 0;
		int res2 = 0;
		for (j = 0; j < N; ++j) {
			++res2;
			for (k = now; k < N; ++k) {
				if (naomi[j] < ken[k]) {
					--res2;
					break;
				}
			}
			now = k + 1;
		}

		printf("Case #%d: %d %d\n", i + 1, res1, res2);
	}

	return 0;
}