#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

int main(int argc, char* argv[]) {
	int T;
	
	setbuf(stdout, NULL);
		

	scanf("%d\n", &T);
	for(int t=0; t<T; t++) {
		double C, F, X;

		scanf("%lf %lf %lf", &C, &F, &X);
		double oldTime = X / 2.0;
		int i = 0;
		while(true) {
		    double newTime = oldTime;
			newTime += C / (2 + i * F);
			newTime -= X / (2 + i * F);
			newTime += X / (2 + i * F + F);
			if (newTime > oldTime) {
			    printf("Case #%d: %.7f\n", t+1, oldTime);
				break;
			} else {
			    oldTime = newTime;
			}
		    i ++;
		}
	}
	
	return 0;
}
