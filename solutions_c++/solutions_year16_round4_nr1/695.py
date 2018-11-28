#include<cstdio>
#include<cstring>
#include<bits/stdc++.h>

char solv[3][13][5000];

int main() {
	int T; scanf("%d", &T);
	for (int j = 0; j < 3; ++j) {
		solv[j][0][0] = 'P'+((j>0)?(j+1):0);
	}
	for (int j = 1; j <= 12; ++j) {
		for (char k = 0; k < 3; ++k) {
			char op = (k+1)%3;
			if (strncmp(solv[k][j-1],solv[op][j-1],(1<<(j-1))) < 0) {
				memcpy(solv[k][j], solv[k][j-1], 1<<(j-1));
				memcpy(solv[k][j]+(1<<(j-1)), solv[op][j-1], 1<<(j-1));
			} else {
				memcpy(solv[k][j], solv[op][j-1], 1<<(j-1));
				memcpy(solv[k][j]+(1<<(j-1)), solv[k][j-1], 1<<(j-1));
			}
		}
	}
	for (int _ = 0; _ < T; ++_) {
		int N, R, P, S; scanf("%d%d%d%d", &N, &R, &P, &S);
		bool found = 0;
		for (int k = 0; k < 3 && !found; ++k) {
			int r = 0, p = 0, s = 0;
			for (int i = 0; i < (1<<N); ++i) {
				if(solv[k][N][i] == 'P') ++p;
				if(solv[k][N][i] == 'R') ++r;
				if(solv[k][N][i] == 'S') ++s;
			}
			if (r == R && p == P && s == S) {
				solv[k][N][1<<N] = 0;
				printf("Case #%d: %s\n", _+1, solv[k][N]);
				found = 1;
			}
		}
		if (!found)
			printf("Case #%d: IMPOSSIBLE\n", _+1);
	}
	return 0;
}
