#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>

using namespace std;

#define LIMN 100
#define LIMS 1000001

int v[LIMN];
int N;
int pd[LIMN][LIMS];

int cmp (const void *a, const void *b) {
	return *(int*)a-*(int*)b;
}

int solve (int curr, int size) {
	if (curr == N)	return 0;
	if (pd[curr][size] == -1) {
		if (size > v[curr])	pd[curr][size] = solve(curr+1, (int)min(LIMS-1LL, size+(long long)v[curr]));
		else {
			int tmp = 1000000;
			if (size > 1)	tmp = solve(curr, (int)min(LIMS-1LL, 2LL*size-1));
			pd[curr][size] = 1+min(solve(curr+1, size),tmp);
		}
	}
	return pd[curr][size];
}

int main (void) {
	int T, c, i, A;
	long long currs;
	scanf ("%d", &T);
	
	for (c = 1; c <= T; c++) {
		printf ("Case #%d: ", c);
		scanf ("%d%d", &A, &N);
		memset (pd, -1, sizeof pd);
		for (i = 0; i < N; i++)	scanf ("%d", &v[i]);
		qsort(v, N, sizeof(int), cmp);
		printf ("%d\n", solve (0, A));
	}
	return 0;
}
