#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	int T;
	int naomi[1500], ken[1500];
	scanf("%d", &T);
	for (int times = 1; times <= T; times++) {
		int N;
		double tmp;
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%lf", &tmp);
			naomi[i] = round(tmp * 100000);
		}
		for (int i = 0; i < N; i++) {
			scanf("%lf", &tmp);
			ken[i] = round(tmp * 100000);
		}
		sort(naomi, naomi + N);
		sort(ken, ken + N);
		int p, q, r, score;
		p = 0; q = N - 1;
		r = N - 1;
		score = N;
		while (p <= q) {
			if (ken[r] >= naomi[q]) {
				score--;
				p++;
				r--;
			} else {
				q--;
				r--;
			}
		}
		printf("Case #%d: %d ", times, score);
		p = 0; q = 0;
		score = N;
		while (q < N) {
			if (naomi[p] >= ken[q]) {
				q++;
			} else {
				q++;
				p++;
				score--;
			}
		}
		printf("%d\n", score);
	return 0;
}