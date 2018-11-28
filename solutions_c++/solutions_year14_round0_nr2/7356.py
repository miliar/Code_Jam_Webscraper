#include <stdio.h>

double cookieWin;
double farmRate;
double farmCost;

double cookieTime(double bestYet, double cookieRate, double aux) {
	__RECURSE:
	double naive = cookieWin/cookieRate + aux;
	if (bestYet < aux) {
		return bestYet;
	}
	if (bestYet > naive) {
		bestYet = naive;
	}
	double nextFarm = farmCost/cookieRate;
	double nextRate = cookieRate + farmRate;

	cookieRate = nextRate;
	aux += nextFarm;
	goto __RECURSE;
	/*
	double compete = cookieTime(maxTime - nextFarm, nextRate) + nextFarm;
	if (compete < naive) {
		return compete;
	}
	return naive;*/
}

void doCase(int i) {
	scanf("%lf %lf %lf", &farmCost, &farmRate, &cookieWin);
	double res = cookieTime(cookieWin/2.0, 2.0, 0);
	printf("Case #%i: %.7lf\n", i+1, res);
}
int main() {
	int nCases;
	scanf("%i", &nCases);
	for (int i = 0; i < nCases; i++) {
		doCase(i);
	}
	return 0;
}
