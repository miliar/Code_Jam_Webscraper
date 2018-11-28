/*
 * QA.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: BarbaraW
 */
#include <cstdio>
#include <stdio.h>
#include <string>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;

#define MAX_D 100

int rows_remaining;
int cols_remaining;

bool check(int lawn[MAX_D + 2][MAX_D + 2], bool map[MAX_D][MAX_D], int n,
		int m) {
	for (int r = 0; r < n; r++) {
		for (int i = 0; i < m; i++) {
			if (lawn[r][i] == lawn[r][MAX_D] && (!map[r][i])) {
				map[r][i] = true;
				lawn[r][MAX_D + 1]--;
				lawn[MAX_D + 1][i]--;
			//	printf("(%d, %d)\n",r,i);
			//	printf("row %d remain %d\n",r,lawn[r][MAX_D + 1]);
			//	printf("col %d remain %d\n",i,lawn[MAX_D + 1][i]);

				if (lawn[r][MAX_D + 1] == 0) {
					rows_remaining--;
				//	printf("total row remain %d\n",rows_remaining);

				}
				if (lawn[MAX_D + 1][i] == 0) {
					cols_remaining--;
				//	printf("total cols remain %d\n",cols_remaining);

				}
			}
		}
	}
	for (int c = 0; c < m; c++) {
		for (int i = 0; i < n; i++) {
			if (lawn[i][c] == lawn[MAX_D][c] && (!map[i][c])) {
				map[i][c] = true;
				lawn[MAX_D + 1][c]--;
				lawn[i][MAX_D + 1]--;
				if (lawn[i][MAX_D + 1] == 0) {
					rows_remaining--;
				}
				if (lawn[MAX_D + 1][c] == 0) {
					cols_remaining--;
				}
			}
		}
	}
	return (cols_remaining == 0) && (rows_remaining == 0);
}

int main() {
	int total2, total;
	FILE * fl = fopen("B-large.in", "r");
	FILE* fo = fopen("outB", "w");
	fscanf(fl, "%d", &total2);
	total = total2;
	int lawn[MAX_D + 2][MAX_D + 2];
	bool map[MAX_D][MAX_D];
	for (int i = 0; i < total; i++) {
		memset(map, false, sizeof(map));
		memset(lawn, 0, sizeof(lawn));
		int N, M;
		fscanf(fl, "%d %d", &N, &M);
		rows_remaining = N;
		cols_remaining = M;
		for (int j = 0; j < N; j++) {
			lawn[j][MAX_D + 1] = M;
			for (int k = 0; k < M; k++) {
				if (j == 0) {
					lawn[MAX_D + 1][k] = N;
				}
				fscanf(fl, " %d", (&lawn[j][k]));
				lawn[j][MAX_D] = max(lawn[j][MAX_D], lawn[j][k]);
				lawn[MAX_D][k] = max(lawn[MAX_D][k], lawn[j][k]);
			}
		}
		bool passed = check(lawn, map, N, M);
		if (passed)
			fprintf(fo, "Case #%d: YES\n", i + 1);
		else {
			fprintf(fo, "Case #%d: NO\n", i + 1);
		}
	}
	return 0;
}

