#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b_large.out", "w", stdout);
	int TextN, TT = 0;
	double C, F, X, Time, V;
	scanf("%d", &TextN);
	while (TextN--) {
		scanf("%lf%lf%lf", &C, &F, &X);
		Time = 0, V = 2.0;
		while (X / V > C / V + X / (V + F)) {
			Time += C / V;
			V += F;
		}
		Time += X / V;
		printf("Case #%d: %.7lf\n", ++TT, Time);
	}

	return 0;
}