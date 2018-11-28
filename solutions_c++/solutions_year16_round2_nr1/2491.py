#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>

int solvation(FILE* f1, FILE* f2, int *ans) {
	int i, nz = 0, nw = 0, nx = 0, nu = 0, ns = 0, nh = 0, nv = 0, ni = 0, nn = 0, ng = 0;
	int a[10];
	char c = 0;
	while (true) {
		fscanf_s(f1, "%c", &c);
		if (c == 'Z')
			nz++;
		if (c == 'W')
			nw++;
		if (c == 'X')
			nx++;
		if (c == 'G')
			ng++;
		if (c == 'U')
			nu++;
		if (c == 'S')
			ns++;
		if (c == 'H')
			nh++;
		if (c == 'V')
			nv++;
		if (c == 'I')
			ni++;
		if (c == 'N')
			nn++;
		if (c == 10) {
			break;
		}
	}
	for (i = 0; i < 10; i++)
		a[i] = 0;
	a[0] = nz;
	a[2] = nw;
	a[6] = nx;
	a[8] = ng;
	a[7] = ns - a[6];
	a[3] = nh - a[8];
	a[4] = nu;
	a[5] = nv - a[7];
	a[9] = ni - a[5] - a[6] - a[8];
	a[1] = nn - 2 * a[9] - a[7];
	int num = 0;
	for (i = 0; i < 10; i++) {
		for (int j = 0; j < a[i]; j++) {
			ans[num] = i;
			num++;
		}
	}
	return num;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int tnum;
	int ans[2000];
	int num;
	char c;
	FILE* f1;
	FILE* f2;
	fopen_s(&f1, "in.txt", "r");
	fopen_s(&f2, "out.txt", "w");
	fscanf_s(f1, "%d", &tnum);
	fscanf_s(f1, "%c", &c);
	for (int inum = 0; inum < tnum; inum++) {
		num = solvation(f1, f2, ans);
		fprintf_s(f2, "Case #%d: ", inum + 1);
		for (int i = 0; i < num; i++) {
			fprintf_s(f2, "%d", ans[i]);
		}
		fprintf_s(f2, "\n");
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
