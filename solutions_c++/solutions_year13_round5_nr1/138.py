#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int MAXN = 1000;

int a[40];

int main() {
	int T;
	freopen("x.txt", "r", stdin); freopen("w.txt", "w", stdout); 
	scanf("%d", &T);
	for (int re = 1; re <= T; re++) {
		int B, N;
		scanf("%d%d", &B, &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", a + i);
		}
		sort(a, a + N);
		if (N == 37) {
			int k = 0;
			for (int i = N - 1; i >= 0; i--) {
				a[i] -= a[0];
				if (a[i] == 0) k++;
			}
			N -= k;
			for (int i = 0; i < N; i++) {
				a[i] = a[i + k];
			}
		}
		double ans = 0;
		// printf("N = %d\n", N);
		for (int i = 1; i <= MAXN; i++) {
			for (int j = 0; j <= N; j++) {
				int t = 0, k;
				double p = 0;
				for (k = 0; k < j; k++) {
					if (a[k] < i) {
						t += i - a[k];
						p += 36.0 * (i - a[k]) / (37 - N + j);
					}
				}
				for (; k < N; k++) {
					if (a[k] < i + 1) {
						t += i + 1 - a[k];
					}
				}
				t += i * (37 - N);
				if (t <= B) {
					p += (37 - N) * 1.0 / (37 - N + j) * i * 36 - t;
					if (p > ans) ans = p;
					// printf("i = %d j = %d t = %d p = %f\n", i, j, t, p);
				}
			}
		}
		printf("Case #%d: %.10f\n", re, ans);
	}
}
