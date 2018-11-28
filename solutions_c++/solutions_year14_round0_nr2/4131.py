

#include <stdio.h>
#include <vector>
#include <algorithm>

#include <limits.h>

double getResSlow(double C, double F, double X);
double getResFast(double C, double F, double X);

int main() {
	int T;
	
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++) {
	
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);
		
		double res = getResSlow(C, F, X);
		
		printf("Case #%d: %lf\n", t, res);
	}

}

double getResSlow(double C, double F, double X) {

	double B = 2;

	double best = X/B;
	
	double timeForBuy = 0.0;
	
	for (int i = 1; timeForBuy < best; i++) {
		timeForBuy += C/B;
		double currentSol = timeForBuy + X/(B+F);
		
		if (currentSol < best) {
			best = currentSol;
		}
		
		B += F;
	}
	
	return best;
}

double getResFast(double C, double F, double X) {

	double B = 2;

	double best = X/B;
	
	double timeForBuy = 0.0;
	
	for (int i = 1; ; i++) {
		timeForBuy += C/B;
		double currentSol = timeForBuy + X/(B+F);
		
		if (currentSol < best) {
			best = currentSol;
		}
		else 
			break;
		
		B += F;
	}
	
	return best;
}


