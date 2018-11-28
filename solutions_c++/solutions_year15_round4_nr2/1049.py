#include <iostream>
using namespace std;

double Ri[11];
double Ci[11];
double Vi[11];

int main()
{
	int T, t;
	int N;

	int i, j, k;
	double X, C;
	double ans0, ans1, ans;
	scanf("%d\n", &T);
	
	for (t = 1; t <= T; ++t) {
		ans = 0;
		scanf("%d %lf %lf\n", &N, &X, &C);

		for (i = 0; i < N; ++i) {
			scanf("%lf %lf\n", &Ri[i], &Ci[i]);
		}

		if (N == 1) {
			if (Ci[0] != C) {
				printf("Case #%d: IMPOSSIBLE\n", t);
			} else {
				printf("Case #%d: %.9lf\n", t, X/Ri[0]);
			}
		} else if (N == 2){
			if (Ci[0] == C && Ci[1] == C) {
				printf("Case #%d: %.9lf\n", t, X/(Ri[0]+Ri[1]));
				continue;
			}
			if (Ci[0] == C) {
				printf("Case #%d: %.9lf\n", t, X/Ri[0]);
				continue;
			}
			if (Ci[1] == C) {
				printf("Case #%d: %.9lf\n", t, X/Ri[1]);
				continue;
			}
			if ((Ci[0] > C && Ci[1] > C) || (Ci[0] < C && Ci[1] < C)) {
				printf("Case #%d: IMPOSSIBLE\n", t);
				continue;
			}

			ans1 = X * (C - Ci[0]) / (Ci[1] - Ci[0]);
			ans0 = X - ans1;

			ans0 = ans0 / Ri[0];
			ans1 = ans1 / Ri[1];

			ans = ans1;

			if (ans0 > ans1) {
				ans = ans0;
			}

			printf("Case #%d: %.9lf\n", t, ans);
		}
	}
}