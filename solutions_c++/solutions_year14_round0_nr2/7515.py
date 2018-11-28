#include<stdio.h>
#include<stdlib.h>

void mainfunction(FILE *fi,FILE *fo){
	double C, F, X;
	double cp = 2,res=0;
	fscanf(fi,"%lf %lf %lf", &C, &F, &X);
	while (1){
		if ((X / cp) < ((X / (cp + F)) + (C / cp))){
			res += X / cp;
			break;
		}
		else{
			res += C / cp;
			cp += F;
		}
	}
	fprintf(fo, "%.7lf\n", res);
}

int main(void){
	FILE *fi = fopen("B-large.in", "r");
	FILE *fo = fopen("result.out", "w");
	int T;
	fscanf(fi,"%d", &T);
	for (int i = 0; i < T; i++){
		fprintf(fo,"Case #%d: ", i + 1);
		mainfunction(fi, fo);
	}
}