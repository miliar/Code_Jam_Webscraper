#include <cstdio>

int findK(double C, double F, double X) {
	return (int)((X*F - 2.0*C - C*F)/(C*F));
}

double term(double x, double F, int k) {
	double kk = (double)k;
	return x/(2.0 + kk*F);
}

double cal_sum(double C, double F, double X, int k) {
	double sum = 0.0;
	if (k > 0) {
		for (int i = 0; i < k; i++) {
			sum += term(C, F, i);
			//printf ("%f\n", term(C,F,i));
		}
			//printf("%f\n", term(X,F,k));
			sum += term(X, F, k);
	}
	else {
		sum = term(X, F, 0);
	}
	return sum;

}


int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		double C, F, X, sum1, sum2, min;
		scanf("%lf%lf%lf", &C, &F, &X);
		int k = findK(C,F,X);
		//printf("%d\n", k);
		// if (k > 0) {
		// 	for (int z = 0; z < 2*k; z++) {
		// 		printf("Case #%d: %lf\n", z, cal_sum(C,F,X,z));
		// 	}
		// }
		sum1 = cal_sum(C,F,X, k);
		sum2 = cal_sum(C,F,X, k+1);
		min = sum1 < sum2 ? sum1 : sum2;
		printf("Case #%d: %lf\n", t+1, min);
		//if (min == sum1) printf("Hey\n");
	}
	return 0;
}