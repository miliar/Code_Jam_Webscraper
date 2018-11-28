#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

const double EPS = 0.0000000001;

double solve(int N, double V, double X, double *R, double *C) {
	if (N == 1) {
		if (abs(X-C[0]) > EPS) {
			return -1.0;
		} else {
			return V / R[0];
		}
	} else {
		if (abs(C[0]-X) < EPS && abs(C[1]-X) < EPS) {
			return V / (R[0] + R[1]);
		} else if (abs(C[0]-X) < EPS) {
			return V / R[0];
		} else if (abs(C[1]-X) < EPS) {
			return V / R[1];
		} else {
			/*
			if (C[0] > C[1]) {
				swap(C[0], C[1]);
				swap(R[0], R[1]);
			}
			*/
			if ((C[0] < X && C[1] < X) || (X < C[0] && X < C[1])) {
				return -1.0;
			}
			double v0 = (X-C[1])/(C[0]-C[1]);
			double v1 = (C[0]-X)/(C[0]-C[1]);
			return max(V * v0 / R[0], V * v1 / R[1]);
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		double V, X;
		double R[110], C[110];
		cin >> N >> V >> X;
		for (int j = 0; j < N; j++)
			cin >> R[j] >> C[j];
		/*
		printf("%d %.9f %.9f\n", N, V, X);
		for (int j = 0; j < N; j++)
			printf("%.9f %.9f\n", R[j], C[j]);
		*/
		double ans = solve(N, V, X, R, C);
		printf("Case #%d: ", i+1);
		if (ans < -0.5) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%.12f\n", ans);
		}
	}
}
