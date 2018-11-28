/*
 * main.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: blding
 */

#include <cstdio>
#include <algorithm>

using namespace std;

int caseNum;
int num;
double w[2][1024];

int war()
{
	int ptr = num - 1;
	int cnt = 0;
	for (int i = num - 1; i >= 0; --i) {
		if (w[1][ptr] > w[0][i]) {
			--ptr;
		} else {
			++cnt;
		}
	}
	return cnt;
}

int dwar()
{
	int ptr = 0;
	int cnt = 0;
	for (int i = 0; i < num; ++i) {
		while (ptr < num && w[0][ptr] < w[1][i]) {
			++ptr;
		}
		if (ptr == num)
			break;
		++ptr;
//		fprintf(stdout, "(%lf %lf)", w[0][ptr], w[1][i]);
		++cnt;
	}
//	fprintf(stdout, "\n");
	return cnt;
}

void work(FILE * fout, int caseId)
{
	sort(w[0], w[0] + num);
	sort(w[1], w[1] + num);

	fprintf(fout, "Case #%d: %d %d\n", caseId, dwar(), war());
}

int main()
{
	FILE * fin = fopen("../input", "r");
	FILE * fout = fopen("../output", "w");

	fscanf(fin, "%d ", &caseNum);
	for (int caseId = 1; caseId <= caseNum; ++caseId) {
		fscanf(fin, "%d ", &num);
		for (int i = 0; i < 2; ++i) {
			for (int j = 0; j < num; ++j) {
				fscanf(fin, "%lf ", &w[i][j]);
			}
		}
		work(fout, caseId);
	}
	fclose(fin);
	fclose(fout);
}




