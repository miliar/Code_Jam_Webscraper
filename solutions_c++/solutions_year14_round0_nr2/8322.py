// Requires C++ 0x // C++11 support in compiler
#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

double solve(double C, double F, double X) {
	double currentProductionRate = 2.0;
	double now = 0.0;
	
	if(C > X) {
		return now + X/currentProductionRate;
	}

	double timeToFini, timeToF, timeToFiniAfterF;
	do {
		timeToFini = X/currentProductionRate;
		timeToF = C/currentProductionRate;
		timeToFiniAfterF = timeToF + X/(currentProductionRate + F);
		if(timeToFini <= timeToFiniAfterF) {
			now += timeToFini;
		} else {
			now += timeToF;
			currentProductionRate += F;
		}
	} while(timeToFini > timeToFiniAfterF);
	return now;
}

int main(void) {
	int T;
	cin >> T;

	for(int t=1; t<=T; ++t) {
		double C, F, X;
		cin >> C >> F >> X;
		printf("Case #%d: %.7f\n", t, solve(C, F, X));
	}
}
