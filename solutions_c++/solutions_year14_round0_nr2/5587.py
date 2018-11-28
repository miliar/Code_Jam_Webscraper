#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc,char **argv)
{
	int t,T;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		double C,F,X;
		double total_time=0.0;
		double rate=2.0;
		scanf("%lf %lf %lf\n",&C,&F,&X);
		while (1){
			double t0;// time to goal without buying a new farm
			double t1a,t1b; // a: time to buy a new farm, b: time to goal with a farm
			t0 = X/rate;
			t1a = C/rate;
			t1b = X/(rate+F);
			if (t0<(t1a+t1b)){
				total_time+=t0;
				break;
			}
			rate+=F;
			total_time+=t1a;
		}
		printf("Case #%d: %.8lf\n",t,total_time);
	}
	return 0;
}
