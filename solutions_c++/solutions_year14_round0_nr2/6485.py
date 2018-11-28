#include <stdio.h>

int main(void) {
	
	int num;
	fscanf(stdin, "%d", &num);
	//printf("num = %d\n", num);
	
	for (int i = 0; i < num; ++i) {
		double C, F, X;
		fscanf(stdin, "%lf %lf %lf", &C, &F, &X);
		//printf("C=%lf F=%lf X=%lf\n", C, F, X);
		
		double f = 2.0;
		if (X <= C) {
			printf("Case #%d: %lf\n", i + 1,  (X / f));
		}
		else {
			double r = 0.0;
			double c = 0.0;
			//printf("X / f                  = %lf\n", X / f);
			//printf("X / (f + F) + (C / f)  = %lf\n", X / (f + F) + (C / f));
			while (X / f > X / (f + F) + (C / f)) {
				r += C / f;
				f += F;
				//printf("X / f                  = %lf\n", X / f);
				//printf("X / (f + F) + (C / f)  = %lf\n", X / (f + F) + (C / f));
			}
			//printf("r = %lf\n", r);
			//printf("f = %lf\n", f);
			//printf("r + X / f = %lf\n", r + X / f);
			printf("Case #%d: %lf\n", i + 1, r + X / f);
		}
		
		
	}
}
