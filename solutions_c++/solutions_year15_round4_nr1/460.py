#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

char M[101][101];
int cntr[101], cntc[101];
int main (void) {
	int t, cc, i, j;
	scanf ("%d", &t);
	for (cc = 1; cc<= t; cc++) {
		memset(cntr, 0, sizeof cntr);
		memset(cntc, 0, sizeof cntc);
		int r, c;
		char last;
		int ans = 0;
		scanf ("%d%d", &r, &c);
		for (i = 0; i < r; i++) {
			scanf ("%s", M[i]);
		}
		for (i = 0; i < r; i++) { //checa o primeiro e o ultimo da linha
			bool first = true;
			last = '.';
			for (j = 0; j < c; j++) {
				if (M[i][j] != '.' && first) {
					if (M[i][j] == '<')	ans++;
					first = false;
				}
				if (M[i][j] != '.')	{
					last = M[i][j];
					cntr[i]++;
					cntc[j]++;
				}
			}
			if (last == '>')	ans++;
		}
		for (j = 0; j < c; j++) { //primeiro e ultimo da coluna
			bool first = true;
			last = '.';
			for (i = 0; i < r; i++) {
				if (M[i][j] != '.' && first) {
					if (M[i][j] == '^')	ans++;
					first = false;
				}
				if (M[i][j] != '.') {
					last = M[i][j];
				}
			}
			if (last == 'v')	ans++;
		}
		bool ok = true;
		for (i = 0; i < r && ok; i++) {
			for (j = 0; j < c && ok; j++) {
				if(M[i][j] != '.' && cntr[i] == 1 && cntc[j] == 1) {
					ok = false;
				}
			}
		}
		if (ok)	printf ("Case #%d: %d\n", cc, ans);
		else	printf ("Case #%d: IMPOSSIBLE\n", cc);
	}

}