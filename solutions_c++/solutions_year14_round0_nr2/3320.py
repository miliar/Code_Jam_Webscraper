#include<cstdio>
#include<iostream>
using namespace std;
FILE *in = fopen("large0.in", "r");
FILE *out = fopen("output.out", "w");
int main(){
	double product, C, F, X, time;
	int T, test;
	fscanf(in, "%d", &T);
	test = T;
	while (T--){
		time = 0.0;
		product = 2.0;
		fscanf(in, "%lf %lf %lf", &C, &F, &X);
		while ((X / product) > (C / product + X / (product + F))){
			time += C / product;
			product += F;
		}
		time += X / product;
		fprintf(out, "Case #%d: %.7lf\n", test - T, time);
	}
	fcloseall();
	return 0;
}