/******************************************************************************************
*           .--.																		  *
* ::\`--._,'.::.`._.--'/::			@author Ana M. Mihut	@course GCJ					  *
* ::::. `  __::__ ' .:::::			@alias  LT-Kerrigan		@date   12.04.2014			  *
* ::::::-:.`'..`'.:-::::::			@link   https://code.google.com/codejam/		      *
* ::::::::\ `--' /::::::::			@detail	Deceitful War								  *
*																						  *
*******************************************************************************************/

#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int Check(const void *a, const void *b){
	double tmpA = *(double*)a;
	double tmpB = *(double*)b;
	
	return ((tmpA > tmpB) ? -1 : ((tmpA < tmpB) ? 1 : 0));
}

int main(){
	FILE *in = freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int T, N, k = 1, i, j, m;
	double naomi[1000] = { 0 }, ken[1000] = { 0 };

	scanf("%d", &T);
	while (T--){
		int war = 0, dwar = 0;
		scanf("%d", &N);
		
		for (i = 0; i<N; i++)
			scanf("%lf", &naomi[i]);
		for (i = 0; i<N; i++)
			scanf("%lf", &ken[i]);

		qsort(naomi, N, sizeof(double), Check);
		qsort(ken, N, sizeof(double), Check);

		double *temp = new double[N];
		
		for (i = 0; i<N; i++)
			temp[i] = ken[i];

		for (i = 0; i < N; i++){
			for (j = 0; j < N; j++){
				if (naomi[i] > ken[j]){
					ken[j] = 10;
					dwar++;
					break;
				}
			}
		}

		for (i = 0; i<N; i++){
			for (j = N - 1; j >= 0; j--){
				if (temp[j] >= naomi[i]){
					temp[j] = -1;
					break;
				}
			}
			if (j == -1)
				war++;
		}
		printf("Case #%d: %d %d\n", k, dwar, war);
		k++;
	}
	return 0;
}

