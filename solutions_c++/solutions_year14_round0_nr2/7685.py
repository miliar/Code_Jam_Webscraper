#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main(){
	int T;
	double C, F, X;
	scanf("%d", &T);
	int ttt = 0;
	while (T--){
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: ", ++ttt);
		double tmp = X/C - 2/F - 1;
		int M = tmp > 0 ? (int)ceil(tmp) : 0;
		double result = 0;
		for (int m = 0; m < M; m++)
			result += C/(m*F+2);
		result += X / (M*F + 2);
		printf("%.7lf\n", result);
	}

	return 0;
}