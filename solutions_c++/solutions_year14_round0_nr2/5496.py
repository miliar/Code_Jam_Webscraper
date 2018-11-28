#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

double C, F, X;

double solve(double s)
{
	double ret;
	
	double x = X;
	double a = 0.0;
	double f = F;
	double c = C;
	
	ret = a + x / s;
	while (a + x / (s + f) + c / s < ret) {
		a += c / s;
		s += f;
		ret = a + x / s;
	}
	
	return ret;
}

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; ++t) {
		double ret;
		cin >> C >> F >> X;
		ret = solve(2.0f);
		printf("Case #%d: %.7f\n", t, ret);
	}
	
	return 0;
}
