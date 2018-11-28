#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define EPS 1e-8
#define MAXN 100005
#define MAXE 1005

typedef pair<int, int> pii;
typedef long long ll;

inline int sgn(double x) {
	return (x > EPS) - (x < -EPS);
}

int T;
double C, F, X;

int main() {
	scanf("%d", &T);
	for (int nCase = 1; nCase <= T; ++nCase) {
		scanf("%lf %lf %lf", &C, &F, &X);

		double S = 2.0;
		double ret = 0;
		do {
			if (sgn(X / S - (X / (S + F) + C / S)) >= 0) {
				ret += C / S;
				S += F;
			} else {
				ret += X / S;
				break;
			}
		} while (1);
		printf("Case #%d: %.7f\n", nCase, ret);
	}
	return 0;
}


