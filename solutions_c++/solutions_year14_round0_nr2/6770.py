#include <stdio.h>

int n;

int main() {
	scanf("%d",&n);

	for(int c = 0; c < n;c++) {
		double time = 0;
		double C;
		double F;
		double X;
		
		scanf("%lf %lf %lf",&C,&F,&X);
		
		double cspeed = 2;
		
		while(C/cspeed + X/(F+cspeed) < X/cspeed) {
			time+=C/cspeed;
			cspeed += F;
		}
		
		time+=X/cspeed;
		
		printf("Case #%d: %.7f\n",c+1,time);
	}

}
