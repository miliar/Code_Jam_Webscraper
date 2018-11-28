#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN = 100 + 10;
int Test, N;
double V, X, R[MAXN], C[MAXN], T[MAXN];

int compare(double x, double y)
{
	if (x < y - 1e-17) return -1;
	if (x > y + 1e-17) return 1;
	return 0;
}

bool Check(double MAXT)
{
	for (int i = 0; i < N; i ++) {
		T[i] = MAXT * R[i];
	}
	double TEMP_V = V;
	for (int i = 0; i < N; i ++)
	if (compare(C[i], X) == 0) {
		TEMP_V -= T[i];
		T[i] = 0;
	}
	//printf("%.2lf %.2lf\n", MAXT, TEMP_V);
	if (compare(TEMP_V, 0.0) <= 0) {
		return true;
	}
	for (int i = 0; i < N; i ++)
	if (compare(C[i], X) == 1 && compare(T[i], 0.0) == 1) {
		for (int j = 0; j < N; j ++)
		if (compare(C[j], X) == -1 && compare(T[j], 0.0) == 1) {
			double Rate = (C[i] - X) / (X - C[j]);
			if (T[i] * Rate <= T[j]) {
				T[j] -= T[i] * Rate;
				TEMP_V -= T[i] * Rate + T[i];
				T[i] = 0;
				break;
			} else {
				T[i] -= T[j] / Rate;
				TEMP_V -= T[j] / Rate + T[j];
				T[j] = 0;
			}
		}
	}
	return compare(TEMP_V, 0.0) <= 0;
}

int main(int argc, char **argv)
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%d%lf%lf", &N, &V, &X);
		for (int i = 0; i < N; i ++) {
			scanf("%lf%lf", &R[i], &C[i]);
		}
		double Left = 0.0, Right = 1E10;
		for (int iter = 0; iter < 1000; iter ++) {
			double Mid = (Left + Right) / 2.0;
			if (Check(Mid)) {
				Right = Mid;
			} else {
				Left = Mid;
			}
		}
		if (Right > 5E9) {
			printf("Case #%d: IMPOSSIBLE\n", Case);
		} else {
			printf("Case #%d: %.12lf\n", Case, Right);
		}
	}
	return 0;
}
