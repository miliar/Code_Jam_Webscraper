#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fp, *fw;

double imax(double a, double b) {
	return a > b ? a : b;
}

int main() {
	fp = fopen("D:\\GCJ\\B-small-attempt0.in", "r");
	fw = fopen("D:\\GCJ\\outBs.txt", "w");
	int cse, n, g = 1, i, ok;
	double V, X, r[110], c[110], res, t1, t2;
	fscanf(fp, "%d", &cse);
	while(cse--) {
		fscanf(fp, "%d %lf %lf", &n, &V, &X);
		ok = 1;
		for(i = 0; i < n; ++i) {
			fscanf(fp, "%lf %lf", &r[i], &c[i]);
		}
		if(n == 1) {
			if(X == c[0]) res = V / r[0];
			else
				ok = 0;
		}
		else {
			if(c[0] == c[1]) {
				if(c[0] == X) res = V / (r[0] + r[1]);
				else
					ok = 0;
			}
			else if(c[0] == X){
				res = V / r[0];
			}
			else if(c[1] == X) {
				res = V / r[1];
			}
			else {
				t1 = V * (c[0] - X) / (r[1] * (c[0] - c[1]));
				t2 = V * (X - c[1]) / (r[0] * (c[0] - c[1]));
				if(t1 > 0 && t2 > 0) res = imax(t1, t2);
				else
					ok = 0;
			}
		}
		if(!ok) fprintf(fw, "Case #%d: IMPOSSIBLE\n", g++);
		else
			fprintf(fw, "Case #%d: %.7lf\n", g++, res);
	}
	system("PAUSE");
	return 0;
}