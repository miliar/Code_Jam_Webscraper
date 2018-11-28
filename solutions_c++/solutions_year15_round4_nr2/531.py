#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <math.h>


using namespace std;


int T, N;
double V, X;
vector<double> R;
vector<double> C;

double EPS = 1e-9;

double solve()
{
	if (N == 2 && fabs(C[0]-C[1]) < EPS) {
		N = 1, R[0] += R[1];
	}

	for (int i = 0; i < N; i++) {
		if (fabs(X-C[i]) < EPS) {
			return V/R[i];
		}
	}

	if (N == 2) {
		if (C[0] < X && C[1] < X)return -1.0;
		if (C[0] > X && C[1] > X)return -1.0;

		double VA = (X-C[1])*V/(C[0]-C[1]);
		double VB = V - VA;

		return max(VA/R[0], VB/R[1]);
	}

	return -1.0;
}


int main()
{
	scanf(" %d", &T);

	for (int cas = 1; cas <= T; cas++) {
		scanf(" %d %lf %lf", &N, &V, &X);
		R.resize(N);
		C.resize(N);
		for (int i = 0; i < N; i++)
			scanf(" %lf %lf", &R[i], &C[i]);

		double res = solve();
		if (res < 0.0)
			printf("Case #%d: IMPOSSIBLE\n", cas);
		else
			printf("Case #%d: %.7lf\n", cas, res);
	}

	return 0;
}