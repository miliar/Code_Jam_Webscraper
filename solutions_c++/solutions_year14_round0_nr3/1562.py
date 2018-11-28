//============================================================================
// Name        : a1.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C, Ansi-style
//============================================================================

#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<iostream>
#define N 100050
#define LL __int64
using namespace std;
char s[60][60];
int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int r, c, m, tt, ri = 0,i,j;
	scanf("%d", &tt);
	while (tt--) {
		ri++;
		scanf("%d%d%d", &r, &c, &m);
		printf("Case #%d:\n", ri);
		if (r * c - m == 1) {
			printf("c");
			for (i = 1; i < c; i++)
				printf("*");
			puts("");
			for (i = 1; i < r; i++) {
				for (j = 0; j < c; j++)
					printf("*");
				puts("");
			}
			continue;
		}

		if (r == 1) {
			printf("c");
			for (i = 1; i < c - m; i++)
				printf(".");
			for (i = 0; i < m; i++)
				printf("*");
			puts("");
			continue;
		}
		if (c == 1) {
			puts("c");
			for (i = 1; i < r - m; i++)
				printf(".\n");
			for (i = 0; i < m; i++)
				printf("*\n");
			continue;
		}
		if (r * c - m < 4) {
			printf("Impossible\n");
			continue;
		}
		if (r == 2) {
			if (m % 2 != 0) {
				printf("Impossible\n");
				continue;
			} else {
				for (i = 0; i < 2; i++)
					for (j = 0; j < c; j++) {
						if (j < (c - m / 2))
							s[i][j] = '.';
						else
							s[i][j] = '*';
					}
				s[0][0] = 'c';
				for (i = 0; i < r; i++) {
					for (j = 0; j < c; j++)
						printf("%c", s[i][j]);
					puts("");
				}
				continue;

			}
		}
		if (c == 2) {
			if (m % 2 != 0) {
				printf("Impossible\n");
				continue;
			} else {
				for (i = 0; i < r; i++) {
					for (j = 0; j < c; j++) {
						if (i < (r - m / 2))
							s[i][j] = '.';
						else
							s[i][j] = '*';
					}
				}
				s[0][0] = 'c';
				for (i = 0; i < r; i++) {
					for (j = 0; j < c; j++)
						printf("%c", s[i][j]);
					puts("");
				}
				continue;
			}
		}

		int res = r * c - m;
		if (res == 5 || res == 7) {
			printf("Impossible\n");
			continue;
		}
		int kc = res / c;
		if (kc < 2)
			kc = 2;
		for (i = 0; i < r; i++)
			for (j = 0; j < c; j++)
				s[i][j] = '*';
		if (res == 4) {
			s[0][1] = s[1][0] = s[1][1] = '.';
			s[0][0] = 'c';
			for (i = 0; i < r; i++) {
				for (j = 0; j < c; j++)
					printf("%c", s[i][j]);
				puts("");
			}
			continue;
		}
		if (kc > 2) {
			for (i = 0; i < kc; i++) {
				for (j = 0; j < c; j++)
					s[i][j] = '.';
			}

			int kr = c;
			int rr = res % kr;
			if (rr == 1) {
				s[kc - 1][c - 1] = '*';
				rr++;
			}
			//printf("%d %d %d\n",kc,kr,rr);
			for (i = 0; i < rr; i++)
				s[kc][i] = '.';
			s[0][0] = 'c';
			for (i = 0; i < r; i++) {
				for (j = 0; j < c; j++)
					printf("%c", s[i][j]);
				puts("");
			}
			continue;
		}
		int kr = res / kc;
		int rr = res % kr;
		for (i = 0; i < kc; i++)
			for (j = 0; j < kr; j++)
				s[i][j] = '.';
		if (rr == 1) {
			s[0][kr - 1] = '*';
			s[1][kr - 1] = '*';
			rr += 2;
		}
		for (i = 0; i < rr; i++)
			s[2][i] = '.';
		s[0][0] = 'c';
		for (i = 0; i < r; i++) {
			for (j = 0; j < c; j++)
				printf("%c", s[i][j]);
			puts("");
		}
	}
}
