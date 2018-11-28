#include <stdio.h>

FILE * pw = stdout;
FILE * pr = stdin;

double project(double cept, double grad, double target){
	return cept + target/grad;
}

int main(){
	pw = fopen("out.txt", "w");
	pr = fopen("in.txt", "r");
	int tc, ti;
	double c, f, x;
	
	fscanf(pr, "%d", &tc);
	for(ti = 1; ti <= tc; ti++){
		fprintf(pw, "Case #%d: ", ti);
		
		fscanf(pr, "%lf %lf %lf", &c, &f, &x);
		
		double grad = 2;
		double cept = 0;
		double best = project(cept, grad, x);
		//printf("Cept at %lf, try grad %lf, proj %lf\n", cept, grad, project(cept, grad, x));
		while(project(cept, grad, x) <= best){
			best = project(cept, grad, x);
			cept = project(cept, grad, c);
			grad += f;	
		//printf("Cept at %lf, try grad %lf, proj %lf\n", cept, grad, project(cept, grad, x));
		}
		
		fprintf(pw, "%.7lf\n", best);
	}
	return 0;
}
