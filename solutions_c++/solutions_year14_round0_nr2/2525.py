#include <stdio.h>

int main(){
	FILE *fi = fopen("B-large.in", "r");
	FILE *fo = fopen("output.txt", "w");
	int T;
	
	fscanf(fi,"%d", &T);

	for (int k = 1; k <= T;k++){
		double C, F, X;
		double Time = 0;
		double now = 2;
		fscanf(fi,"%lf %lf %lf", &C, &F, &X);



		while (1){
			
			if (X / now > (C / now + X / (now + F))){
				Time += C / now;
				now += F;
				
			}
			else{
				Time += X / now;
				break;
			}
			}
		fprintf(fo, "Case #%d: %.7lf\n", k, Time);


	}

	return 0;
}