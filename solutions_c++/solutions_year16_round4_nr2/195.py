#include <bits/stdc++.h>

using namespace std;

double Pr[222];
double F[222][222];

int main(void)
{
    int T = 0;
    int TK = 0;
    scanf("%d", &T);
    while (T--) {
		printf("Case #%d: ", ++TK);

		int N, K;
		scanf("%d %d", &N, &K);

		for (int i = 0;i < N;i++) scanf("%lf", &Pr[i]);

		sort(Pr, Pr + N);

		double ans = 0;
		for (int i = 0;i <= K;i++) {
			memset(F, 0, sizeof(F));
			F[0][0] = 1.;
			int t = 0;
			for (int j = 0;j < i;j++) {
				for (int k = 0;k < N;k++) {
					F[t+1][k+1] += F[t][k] * Pr[j];
					F[t+1][k] += F[t][k] * (1. - Pr[j]);
				}
				t++;
			}
			for (int j = N-(K-i);j < N;j++) {
				for (int k = 0;k < N;k++) {
					F[t+1][k+1] += F[t][k] * Pr[j];
					F[t+1][k] += F[t][k] * (1. - Pr[j]);
				}
				t++;
			}
			ans = max(ans, F[K][K/2]);
		}
		printf("%.9f\n", ans);
	}
	return 0;
}
