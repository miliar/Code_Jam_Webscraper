#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define dump(x) (cout << #x << " = " << x << endl)

double INF = 1e10;

int T;
double C, F, X;

/*
double rec(double ct, double ub, double cps)
{
	if (ct > ub) return INF;
	double ctime = C/cps;
	double ntime = ct+ctime;
	double ncps = cps+F;
	double nub = min(ub, ntime+(X/ncps));
	return min(ub, rec(ntime, nub, ncps));
}
*/

double rec(double ct, double ub, double cps)
{
	double ans = ub;
	for (;;) {
		if (ct > ub) return ans;
		double ctime = C/cps;
		double ntime = ct+ctime;
		double ncps = cps+F;
		double nub = min(ub, ntime+(X/ncps));

		if (ntime > nub)
			return ans;
		ans = min(ans, nub);
		ct = ntime, ub = nub, cps = ncps;
	}
	return -1;
}

int main()
{
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> C >> F >> X;
		printf("Case #%d: %.10lf\n", t+1, rec(0, X/2.0, 2.0));
	}
	return 0;
}

