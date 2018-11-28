/*
 * naomi.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: pxp943
 */

#include<stdio.h>
#include<algorithm>

using namespace std;
double naomiWeight[1000];
double kenWeight[1000];

FILE *f,*fin;

int main() {

	int testcase;
	int n, i, j, k;
	int naomifirst, naomilast, kenfirst, kenlast;
	int ken, naomiScore;
	int normalWar, decievWar;

	f = fopen("output.txt", "w");
	fin = fopen("input.txt", "r");

	fscanf(fin,"%d", &testcase);

	for (i = 1; i <= testcase; ++i) {
		fscanf(fin,"%d", &n);
		for (j = 0; j < n; ++j) {
			fscanf(fin,"%lf", &naomiWeight[j]);
		}
		for (j = 0; j < n; ++j) {
			fscanf(fin,"%lf", &kenWeight[j]);
		}

		sort(naomiWeight, naomiWeight + n);
		sort(kenWeight, kenWeight + n);
/*
		for (j = 0; j < n; ++j) {
			fprintf(f, "%f ", naomiWeight[j]);
		}
		fprintf(f,"\n");
		for (j = 0; j < n; ++j) {
			fprintf(f, "%f ", kenWeight[j]);
		}
		fprintf(f,"\n");
*/
		ken = 0;
		normalWar = 0;
		for (j = 0; j < n && ken < n; ++j) {

			while (kenWeight[ken] < naomiWeight[j] && ken < n)
				{
					ken++;
					normalWar++;
				}

			++ken;

		}
		//normalWar = n - j;

		naomifirst = 0;
		naomilast = n - 1;
		kenfirst = 0;
		kenlast = n - 1;

		naomiScore = 0;
		for (j = 0; j < n; ++j) {
			if (naomiWeight[j] < kenWeight[kenfirst])
				kenlast--;
			else {
				kenfirst++;
				naomiScore++;
			}
		}

		fprintf(f, "Case #%d: %d %d\n", i, naomiScore, normalWar);

	}

	fclose(f);
	fclose(fin);

	return 0;
}

