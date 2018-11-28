#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cfloat>

using namespace std;

double C, F ,X;


double findMinWithDP() {
	int MAX_FACTORIES = (int)(X / C);
	if (MAX_FACTORIES * C >= X) {
		MAX_FACTORIES--;
	}
	
	double *dp = new double[MAX_FACTORIES+1];
	dp[0] = 0.0;
	double min_time = X / 2.0;
	for (int i = 1; i < MAX_FACTORIES+1; ++i) {
		dp[i] = dp[i-1] + C / (2.0 + (i-1) * F);
		min_time = min(min_time, dp[i] + X / (2.0 + i * F));
	}

	delete[] dp;

	return min_time;	
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; ++i) {
		scanf("%lf %lf %lf\n", &C, &F, &X);
		printf("Case #%d: %.7lf\n",i+1, findMinWithDP());
	}
}
