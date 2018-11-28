#include <stdio.h>

int main(void)
{
	int T, t;
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &T);
	for (t=1;t<=T;++t){
		double C, F, X;
		int i;
		double res, tmp, a;
		fscanf(fin, "%lf %lf %lf", &C, &F, &X);
		a = 2.0;
		res = X / a;
		tmp = C / a;
		for (i=1;;++i){
			a = a + F;
			if (tmp + (X / a) < res){
				res = tmp + (X / a);
			} else break;
			tmp = tmp + (C / a);
		}
		fprintf(fout, "Case #%d: %.7lf\n", t, res);
	}
	fclose(fin);
	fclose(fout);
}
