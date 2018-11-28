#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		double a[1000], b[1000];
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%lf", &a[i]);
		for (int i = 0; i < N; i++)
			scanf("%lf", &b[i]);

		sort(a, a + N);
		sort(b, b + N);

		int ans1 = 0, ans2 = 0;
		int ap = 0, bp = 0;

		for (int i = 0; i < N; i++)
			if (b[i] > a[ap]) {
				ap++;
				ans1++;
			}

		bp = 0;
		for (int i = 0; i < N; i++)
			if (a[i] > b[bp]) {
				bp++;
				ans2++;
			}

		printf("Case #%d: %d %d\n", ca, ans2, N - ans1);
	}
	return 0;
}