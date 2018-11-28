#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>

int solvation(FILE* f1, FILE* f2, int inum, int *a) {
	int ans = 0;
	int k, c, s;
	fscanf_s(f1, "%d %d %d", &k, &c, &s);
	if (c*s < k) {
		return 0;
	}
	if (s == k) {
		for (int i = 0; i < s; i++) {
			a[i] = i + 1;
		}
		return s;
	}
	ans = (k - 1) / c + 1;
	int ind;
	for (int i = 0; i < ans; i++) {
		ind = c*i;
		for (int j = 1; j < c; j++) {
			ind *= k;
			ind += (i * c + j);
		}
		ind++;
		a[i] = ind;
	}
	return ans;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int tnum;
	int ans = 0;
	int a[100];
	FILE* f1;
	FILE* f2;
	char c;
	fopen_s(&f1, "in.txt", "r");
	fopen_s(&f2, "out.txt", "w");
	fscanf_s(f1, "%d", &tnum);
	for (int inum = 0; inum < tnum; inum++) {
		ans = solvation(f1, f2, inum, a);
		if (!ans) {
			fprintf_s(f2, "Case #%d: IMPOSSIBLE\n", inum + 1);
		}
		else {
			fprintf_s(f2, "Case #%d:", inum + 1);
			for (int i = 0; i < ans; i++) {
				fprintf_s(f2, " %d", a[i]);
			}
			fprintf_s(f2, "\n");
		}
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
