#include <stdio.h>
#include <algorithm>
double sol[100000][2] = { 0 };
int main(){
	FILE* fp = fopen("practice.in", "r");
	FILE* fp2 = fopen("practice.out", "w");

	int t;
	fscanf(fp, "%d", &t);
	int i, j, k;
	for (i = 1; i <= t; i++){
		double c, f, x;
		fscanf(fp,"%lf%lf%lf", &c, &f, &x);
		sol[0][1] = x / 2.0;
		for (j=1;;j++){
			sol[j][0] = sol[j - 1][0] + c / (2 + (j - 1) * f);
			sol[j][1] = sol[j][0] + x / (2 + j*f);
			if (sol[j][1] > sol[j - 1][1])
				break;
		}
			fprintf(fp2, "Case #%d: %.7f\n", i,sol[j-1][1]);
	}

}