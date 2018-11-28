#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int N, M, K;
double P[300], A[300], F[300][300];

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int test, nCase = 0;
	scanf("%d", &test);
	while (test --) {
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; i ++) {
			scanf("%lf", &P[i]);
		}
		sort(P, P + N);
		double ret = 0.0;
		for (int k = 0; k <= K; k ++) {
			M = 0;
			for (int i = 0; i < k; i ++) {
				A[M ++] = P[i];
			}
			for (int i = 0; i < K - k; i ++) {
				A[M ++] = P[N - i - 1];
			}
			memset(F, 0, sizeof(F));
			F[0][0] = 1.0;
			for (int i = 0; i < M; i ++) {
				for (int j = 0; j <= i; j ++) {
					F[i + 1][j] += F[i][j] * (1 - A[i]);
					F[i + 1][j + 1] += F[i][j] * A[i];
				}
			}
			ret = max(ret, F[M][K / 2]);
		}
		printf("Case #%d: %.8lf\n", ++ nCase, ret);
	}
	return 0;
}
