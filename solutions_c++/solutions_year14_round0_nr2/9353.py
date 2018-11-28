#include<stdio.h>
int main() {
	int T, t;
	double C, F, X, bound;
	double estTime = 0;
	double farmTime[10000];
	int i,j,k;
	FILE *in, *ou;
	in = fopen("input.txt","r");
	ou = fopen("output.txt","w");
	fscanf(in,"%d",&T);
	for(t =0 ; t < T ; t ++) {
		fscanf(in,"%lf%lf%lf",&C,&F,&X);
		bound = X / 2;
		farmTime[0] = 0;
		for(i=1;i<10000;i++) {
			farmTime[i] = farmTime[i-1] + C / ((i-1) * F + 2);
			estTime = farmTime[i] + X / ((i) * F + 2);
			if(estTime > bound)
				break;
			bound = estTime;
		}
		fprintf(ou,"Case #%d: %.7lf\n",t+1,bound);
	}
	
	return 1;
}
