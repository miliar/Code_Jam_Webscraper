#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>

int solvation(FILE* f1, FILE* f2, int inum) {
	int ans = 0;
	int sum = 0, sum1;
	int n, k = 10;
	int a[10];
	for (int i = 0; i < k; i++) {
		a[i] = 0;
	}
	fscanf_s(f1, "%d", &n);
	if (n == 0) {
		return 0;
	}
	while (!ans) {
		sum = sum + n;
		sum1 = sum;
		while (sum1 > 0) {
			int p = sum1 % 10;
			if (a[p] == 0) {
				a[p] = 1;
				k--;
			}
			sum1 = sum1 / 10;
		}
		if (k <= 0) {
			ans = sum;
		}
	}
	return ans;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int tnum;
	int ans = 0;
	FILE* f1;
	FILE* f2;
	fopen_s(&f1, "in.txt", "r");
	fopen_s(&f2, "out.txt", "w");
	fscanf_s(f1, "%d", &tnum);
	for (int inum = 0; inum < tnum; inum++) {
		ans = solvation(f1, f2, inum);
		if (ans == 0) {
			fprintf_s(f2, "Case #%d: INSOMNIA\n", inum + 1);
		}
		else {
			fprintf_s(f2, "Case #%d: %d\n", inum + 1, ans);
		}
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
