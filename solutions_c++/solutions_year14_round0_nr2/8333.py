#include <cstdio>
#include <iostream>

using namespace std;

double solve (double C, double F, double X)
{
	if (X <= C)
		return X/2;
	double prevT = X/2;
	double t=C/2;
	double currR = 2+F;
	while (true) {
		double cT = t + X/currR;
		if (cT >= prevT)
			break;
		t += C/currR;
		currR += F;
		prevT = cT;
	}
	return prevT;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int tc=0; tc<T; tc++) {
		double C, F, X;
		cin >> C >> F >> X;
		printf("Case #%d: %.7f\n", tc+1, solve(C, F, X));
	}

	return 0;
}