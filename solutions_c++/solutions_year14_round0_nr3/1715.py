#include <stdio.h>

int cases, kejs;
int R, C, M, i, j, k, m;
char b[52][52];
char c[52][52];

void fill(int i, int j) {
	if (c[i][j] != 0) return;
	c[i][j] = 10;
	fill(i-1,j-1); fill(i-1,j); fill(i-1,j+1);
	fill(i,j-1); fill(i,j+1);
	fill(i+1,j-1); fill(i+1,j); fill(i+1,j+1);
}

bool can(int rr, int cc) {
	fill(rr, cc);
	int i, j;
	for (i = 1; i <= R; i++) {
		for (j = 1; j <= C; j++) {
			if (c[i][j] == 10) c[i][j] = 0;
			else if (c[i][j] == 0) return false;
		}
	}
	return true;
}

int main() {
    scanf("%d", &cases);
    for (kejs = 1; kejs <= cases; kejs++) {
        printf("Case #%d:\n", kejs);
        scanf("%d%d%d", &R, &C, &M);
				for (i = 0; i <= R + 1; i++) {b[i][C+1] = '\0'; c[i][C+1] = c[i][0] = 9;}
				for (i = 0; i <= C + 1; i++) {b[R+1][i] = '\0'; c[R+1][i] = c[0][i] = 9;}
				int lim = (1 << (R*C));
				for (k = 0; k < lim; k++) {
					if (__builtin_popcount(k) != M) continue;
					m = 0;
					for (i = 1; i <= R; i++) {
						for (j = 1; j <= C; j++) {
							if ((1 << m) & k) b[i][j] = '*';
							else b[i][j] = '.';
							m++;
						}
					}
					if (R*C-1 == M) break;
					for (i = 1; i <= R; i++) {
						for (j = 1; j <= C; j++) {
							if (b[i][j] == '*') c[i][j] = 9;
							else c[i][j] = 
								(b[i-1][j-1] == '*') + (b[i-1][j] == '*') + (b[i-1][j+1] == '*') +
								(b[i][j-1] == '*') + (b[i][j+1] == '*') +
								(b[i+1][j-1] == '*') + (b[i+1][j] == '*') + (b[i+1][j+1] == '*');
						}
					}
					for (i = 1; i <= R; i++) {
						for (j = 1; j <= C; j++) {
							if (c[i][j] > 0 && c[i][j] < 9) {
								if (
									(c[i-1][j-1] == 0) + (c[i-1][j] == 0) + (c[i-1][j+1] == 0) +
									(c[i][j-1] == 0) + (c[i][j+1] == 0) +
									(c[i+1][j-1] == 0) + (c[i+1][j] == 0) + (c[i+1][j+1] == 0)
									== 0
								) goto bad;
							}
						}
					}
					for (i = 1; i <= R; i++) {
						for (j = 1; j <= C; j++) {
							if (c[i][j] == 0 && !can(i, j)) goto bad; 
						}
					}
					break;
bad:;
				}
				if (k < lim) {
					k = 0;
					for (i = 1; i <= R; i++) {
						for (j = 1; j <= C; j++) {
							if (b[i][j] == '.' && k == 0) {
								if (R*C==M+1 || c[i][j] == 0) {
									k = 1;
									printf("c");
									continue;
								}	
							}
							printf("%c", b[i][j]);
						}
						printf("\n");
					}
				} else {
	        printf("Impossible\n");
				}
			}
    return 0;
}

