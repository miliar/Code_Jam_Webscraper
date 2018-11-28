#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>

int solvation(FILE* f1, FILE* f2, int inum) {
	int ans = 0;
	char c, c1;
	fscanf_s(f1, "%c", &c);
	if (c == '-') {
		ans++;
	}
	c1 = c;
	while (c != 10) {
		fscanf_s(f1, "%c", &c);
		if (c == '-' && c1 == '+') {
			ans += 2;
		}
		c1 = c;
	}
	return ans;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int tnum;
	int ans = 0;
	FILE* f1;
	FILE* f2;
	char c;
	fopen_s(&f1, "in.txt", "r");
	fopen_s(&f2, "out.txt", "w");
	fscanf_s(f1, "%d", &tnum);
	fscanf_s(f1, "%c", &c);
	for (int inum = 0; inum < tnum; inum++) {
		ans = solvation(f1, f2, inum);
		fprintf_s(f2, "Case #%d: %d\n", inum + 1, ans);
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
