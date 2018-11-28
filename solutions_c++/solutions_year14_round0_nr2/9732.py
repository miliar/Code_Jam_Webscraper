#include <stdio.h>

using namespace std;

double find_nemo(double C, double F, double X, double rate) {
	//printf("rate : %lf\n", rate);
	double a = X/(rate);
	double b = (C/rate) + (X)/(rate + F);
	//printf("a: %lf and b: %lf \n", a, b);
	if(b<a) {
		//buy
		//printf("%lf\n", (C/rate));
		return (C/rate) + find_nemo(C, F, X, (rate+F));
	}
	else {
		//don't buy
		return X/rate;
	}
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	double C, F, X;
	scanf("%d", &T);
	for(int i=1; i<=T; i++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		//printf("%.7lf %.7lf %.7lf\n", C, F, X);
		double k = find_nemo(C, F, X, 2);
		
		printf("Case #%d: %.7lf\n", i, k);
	}
	return 0;
}

