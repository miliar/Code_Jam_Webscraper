#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>

#define INFILE fp_in
#define OUTFILE fp_out

using namespace std;

FILE *fp_in, *fp_out;

bool comp(double a, double b){
	return a > b;
}


void solve(int T){
	double naomi[1024], ken[1024];
	int n;
	double tmp;
	fscanf(INFILE,"%d", &n);

	for (int i = 0; i < n; i++){
		fscanf(INFILE, "%lf", &tmp);
		naomi[i] = tmp;
	}
	for (int i = 0; i < n; i++){
		fscanf(INFILE, "%lf", &tmp);
		ken[i] = tmp;
	}

	sort(naomi, naomi+n, comp);
	sort(ken, ken+n, comp);

	int nn = 0, kn = 0;

	int wina=0, winb=0;

	while (nn<n&&kn<n){
		if (naomi[nn] > ken[kn]){
			nn++;
		}
		else{
			wina++;
			kn++;
			nn++;
		}
	}
	nn = 0; kn = 0;


	while (nn < n&&kn<n){
		if (naomi[nn]<ken[kn]){
			kn++;
		}
		else{
			winb++;
			kn++;
			nn++;
		}
	}

	fprintf(OUTFILE, "Case #%d: %d %d\n",T+1, winb, n - wina);
}

int main(){


	int T, line;

	fp_in = fopen("D-large.in", "r");
	fp_out = fopen("D-large.out", "w");
	fscanf(INFILE, "%d", &T);

	for (int i = 0; i < T; i++){
		solve(i);
	}

}