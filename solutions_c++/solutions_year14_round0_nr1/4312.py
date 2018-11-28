/*
 * main.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: blding
 */

#include <algorithm>
#include <cstdio>

using namespace std;

int caseNum;
int cards[2][4][4];
int ans[2];
int hit[17];

void work(int caseId, FILE * fout)
{
	for (int i = 1; i < 17; ++i) {
		hit[i] = 0;
	}
	for (int i = 0; i < 2; ++i) {
		for (int j = 0; j < 4; ++j) {
			++hit[cards[i][ans[i] - 1][j]];
		}
	}
	int cnt = 0;
	int id = 0;
	for (int i = 1; i < 17; ++i) {
		//fprintf(fout, "(%d %d) ", i, hit[i]);
		if (hit[i] == 2) {
			++cnt;
			id = i;
		}
	}
	if (cnt == 0) {
		fprintf(fout, "Case #%d: Volunteer cheated!\n", caseId);
	} else if (cnt == 1) {
		fprintf(fout, "Case #%d: %d\n", caseId, id);
	} else {
		fprintf(fout, "Case #%d: Bad magician!\n", caseId);
	}
}

int main()
{
	FILE * fin;
	FILE * fout;

	fin = fopen("../input", "r");
	fout = fopen("../output", "w");

	fscanf(fin, "%d ", &caseNum);
	for (int i = 0; i < caseNum; ++i) {
		for (int j = 0; j < 2; ++j) {
			fscanf(fin, "%d ", &ans[j]);
			for (int row = 0; row < 4; ++row) {
				for (int col = 0; col < 4; ++col) {
					fscanf(fin, "%d ", &cards[j][row][col]);
				}
			}
		}
		work(i + 1, fout);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}


