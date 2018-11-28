#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
//#include <set>
//using namespace std;

int max(int x, int y){return x<y ? y : x;}
int min(int x, int y){return x>y ? y : x;}
int cmp_double(const void *d1, const void *d2){
	if(*(double*)d1<*(double*)d2)return -1;
	if(*(double*)d1>*(double*)d2)return 1;
	return 0;
}
void solve(int n, double *N, double *K, int &wr, int &dwr){
	qsort(N, n, sizeof(double), cmp_double);
	qsort(K, n, sizeof(double), cmp_double);
	int i, j, twr=0, tdwr=0;
	for(i=j=n-1; i>=0&&j>=0; j--, i--){
		while(N[i]>K[j] && i>=0)
			i--, twr++;
		if(i<0)break;
	}
	wr = twr;
	for(i=j=n-1; i>=0&&j>=0; j--, i--, tdwr++){
		while(K[i]>N[j] && i>=0)
			i--;
		if(i<0)break;
	}
	dwr = tdwr;
}

int main(){
	FILE *fin = fopen("input.txt","r"), *fout;
	if(!fin){printf("no input\n"); return 0;}
	fout = fopen("output.txt","w");
	int i, j, T=0, n, dwr=0, wr=0;
	if(fscanf(fin,"%d",&T)!=1)return 0;
	char *str=0;
	double *K, *N;
	for(i=1; i<=T; i++){
		fscanf(fin, "%d", &n);
		K = new double[n]; N = new double[n];
		for(j=0; j<n; j++)
			fscanf(fin, "%lf", N+j);
		for(j=0; j<n; j++)
			fscanf(fin, "%lf", K+j);
		solve(n, N, K, wr, dwr);
		fprintf(fout, "case #%d: %d %d\n", i, dwr, wr);
		delete[]K; delete[]N;
	}
	fclose(fin); fclose(fout);
	return 0;
}