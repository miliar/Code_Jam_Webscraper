#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

#define INFILE fp_in
#define OUTFILE fp_out

FILE *fp_in, *fp_out;


void solve(int T){
	double c, f, x, min;
	

	fscanf(INFILE, "%lf %lf %lf", &c, &f, &x);

	min = x / 2;

	int num = (int)x / c;
	double cur = 0;
	for (int i = 1; i < num+1; i++){
		cur = x/(2+i*f);
		for (int j = 0; j < i; j++){
			cur += c / (2 + j*f);
		}
		if (cur < min){
			min = cur;
		}
	}

	fprintf(OUTFILE, "Case #%d: %.7lf\n",T+1, min);

}

int main(){


	int T, line;

	fp_in = fopen("B-large.in", "r");
	fp_out = fopen("B-large.out", "w");
	fscanf(INFILE, "%d", &T);

	for (int i = 0; i < T; i++){
		solve(i);
	}

}