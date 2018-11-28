#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

double solve( double C, double F, double X, double rate, double total) {
	double res = 0;
	double A = total + (X/rate);
	double B = total + (C/rate) + (X/(rate+F));
	if ( A > B ) {
		res = solve(C,F,X,rate+F,total+(C/rate));
	} else {
		res = A;
	}
	return res;
}

int main () {
	int T;
	double C,F,X;
	scanf("%d",&T);
	for ( int w = 1; w <= T; w++) {
		scanf("%lf %lf %lf",&C,&F,&X);
		printf("Case #%d: %.7lf\n",w,solve(C,F,X,2,0));
	}
	return 0;
}
