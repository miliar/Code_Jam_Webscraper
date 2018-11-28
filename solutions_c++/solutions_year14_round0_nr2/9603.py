#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <math.h>
#include <sstream>
using namespace std;

double hasil(double C, double F, double X, double target, double CNow) {
	if (target == X) {
		return X/CNow;
	} else {
		double temp = C/CNow;
		if (X/CNow < temp + X/(CNow+F)) {
			return X/CNow;
		} else {
			double hasil1 = hasil(C,F,X,C,CNow+F);
			double hasil2 = hasil(C,F,X,X,CNow+F);
			if (hasil1 > hasil2) {
				return temp + hasil2;
			} else {
				return temp + hasil1;
			}
		}
	}
}

int main() {	
	int T = 0;
	scanf("%d\n",&T);	

	for (int i=0; i<T; i++) {
		double C = 0;
		double F = 0;
		double X = 0;
		scanf("%lf %lf %lf\n", &C, &F, &X);
		double hasil1 = hasil(C,F,X,C,2);
		double hasil2 = hasil(C,F,X,X,2);
		if ( hasil1 > hasil2) {
			printf("Case #%d: %.7lf\n", (i+1), hasil2);
		} else {
			printf("Case #%d: %.7lf\n", (i+1), hasil1);
		}
	}
	return 0;
}