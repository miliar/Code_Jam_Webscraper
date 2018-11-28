#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int main(){
	int T, i;
	double c, f, x, p[2], tw, tf, total[2];
	FILE *in, *out;
	in = fopen("B-large.in", "r");
	out = fopen("B-large.out", "w");
	fscanf(in, "%d", &T);
	for (i = 1; i <= T; ++i){
		p[0] = 2; p[1] = total[0] = total[1] = 0;
		tf = tw = 0;
		fscanf(in, "%lf%lf%lf", &c, &f, &x);
		total[1] = x / p[0];
		do{
			total[0] = total[1];
			tf += c / p[0];
			p[1] = p[0] + f;
			tw = x / p[1];
			total[1] = tw + tf;
			p[0] = p[1];
		} while (total[1] < total[0]);
		fprintf(out, "Case #%d: %.7lf\n", i, total[0]);
	}

	fclose(in);
	fclose(out);
	return 0;
}