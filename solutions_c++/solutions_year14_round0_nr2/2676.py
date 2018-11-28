#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double solve() {
	double c, f, x;
	cin >> c >> f >> x;

	double speed = 2.0;

	if (x <= c) {
		return x/speed;
	}

	double tt = 0.0;
	while ( x/speed  > (c/speed + x/(speed+f)) ) {
		tt += (c/speed);
		speed += f;
	}
	tt += (x/speed);

	return tt;
}

int main()
{
	int caseNum;
	cin >> caseNum;

	for (int caseNo=1; caseNo <= caseNum; ++caseNo) {
		double res = solve();
		printf("Case #%d: %.7f\n", caseNo, res);
	}

	return 0;
}
