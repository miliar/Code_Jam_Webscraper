#include <stdio.h>

double solve(double C, double F, double X, double rate){
	double best = X/rate;
	double time = 0.0;
	while(1){
		time += C/rate;
		rate += F;
		time += X/rate;
		if(time < best)
			best = time;
		else break;
		
		time -= X/rate;
	}
	return best;
}

int main(){
	double C,F,X;
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		
		scanf("%lf %lf %lf",&C,&F,&X);
		double time = solve(C,F,X,2.0);
		printf("Case #%d: %.7lf\n",i,time);
	}
	return 0;
}