#include <cstdio>
#include <algorithm>

//double C, F, X;

int N;
double a[1010], b[1010];

int main() {
	int T;
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			scanf("%lf", &a[i]);
		for (int i = 0; i < N; ++i)
			scanf("%lf", &b[i]);
		std::sort(a, a + N);
		std::sort(b, b + N);
		int l = 0, r = N - 1;
		int ans1 = 0, ans2 = N;
		for (int i = 0; i < N; ++i) {
			if (a[i] < b[l]) --r;
			else {
				++l;
				ans1++;
			}
		}
		for (int i = 0, j = 0; i < N; ++i) {
			while (j < N && b[j] < a[i]) ++j;
			if (j < N) {
				--ans2;
				++j;
			}
		} 
		printf("Case #%d: %d %d\n", t, ans1, ans2);
	}
}