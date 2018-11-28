#include <stdio.h>
#include <memory.h>
#include <math.h>

double solve(double c, double f, double x){
	double sum = 0, tc = 2;
	int i, N = int(ceil((x*f-c*2.)/(c*f)))-1;
	for(i=0; i<N; i++){
		sum += c/tc;
		tc += f;
	}
	return sum + x/tc;
}

int main(){
	FILE *fin = fopen("input.txt","r"), *fout;
	if(!fin){printf("no input\n"); return 0;}
	fout = fopen("output.txt","w");
	int i, T=0;
	double c,f,x;
	if(fscanf(fin,"%d",&T)!=1)return 0;
	int *str=0;
	for(i=1; i<=T; i++){
		fscanf(fin, "%lf%lf%lf", &c, &f, &x);
		fprintf(fout, "case #%d: %.7lf\n", i, solve(c,f,x));
	}
	fclose(fin); fclose(fout);
	return 0;
}