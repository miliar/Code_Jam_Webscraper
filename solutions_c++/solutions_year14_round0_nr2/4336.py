/*
 * main.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: blding
 */

#include <cstdio>
#include <cmath>

int caseNum;

double c;
double f;
double x;

double getTime(int k)
{
	double s = 0.0;
	for (int i = 0; i < k; ++i) {
		s += 1 / (2 + f * i);
	}
	return c * s + x / (2 + f * k);
}

void work(FILE * fout, int caseId)
{
	int k = floor((x * f - 2 * c) / c / f);
	if (k < 0)
		k = 0;
	double t = getTime(k);
	fprintf(fout, "Case #%d: %.7lf\n", caseId, t);
}

int main()
{
	FILE * fin = fopen("../input", "r");
	FILE * fout = fopen("../output", "w");
	fscanf(fin, "%d ", &caseNum);
	for (int caseId = 1; caseId <= caseNum; ++caseId) {
		fscanf(fin, "%lf %lf %lf ", &c, &f, &x);
		work(fout, caseId);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}



