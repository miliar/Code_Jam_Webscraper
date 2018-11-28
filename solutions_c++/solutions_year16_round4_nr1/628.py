#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <math.h>
#include <string.h>
#include <algorithm>

#define si()        (scanf("%d", &TEMP), TEMP)
#define pii         pair<int, int>
#define fi          first
#define se          second
#define pin(X)      printf("%d\n", (X))
#define pis(X)      printf("%d ", (X))
#define pil()       printf("\n");
#define pb          push_back
#define sz(X)       ((int)(X).size())
#define loop(X, Y)  for (int X = 0 ; X < (Y) ; X++)
#define loopi(X, Y) for (int X = 1 ; X <= (Y) ; X++)

using namespace std;

int TEMP;

int li[3000];
int len;


void solve() {
	int n = si();
	int r = 0, p = 0, c = 0;

	int entry[20000] = {0};
	int nentry[20000] = {};

	loop(i, n) {
  		for (int j = 0; j < (1 << i); j++) {
			int c = entry[j];
			nentry[j << 1] = c;
			nentry[(j << 1) + 1] = (c + 1) % 3;
		}
		for (int j = 0; j < (1 << (i + 1)); j++) {
			entry[j] = nentry[j];
		}
	}

	loop(i, 1 << n) {
		switch (entry[i]) {
		case 0: r++; break;
		case 1: c++; break;
		case 2: p++; break;
		}
	}

	int rR = si(), rP = si(), rC = si();

	int pos;
	char li[3];

	if (r == rR && c == rC) {
		pos = 1;
		li[0] = 'R';
		li[1] = 'S';
		li[2] = 'P';
	}else if (r == rC && c == rP) {
		pos = 1;
		li[0] = 'S';
		li[1] = 'P';
		li[2] = 'R';
	}
	else if (r == rP && c == rR) {
		pos = 1;
		li[0] = 'P';
		li[1] = 'R';
		li[2] = 'S';
	}
	else pos = 0;

	if (pos) {
		for (int i = 1; i < (1 << n); i <<= 1) {
			int ln = (1 << n) / i;

			for (int j = 0; j < (ln << 1); j++) {
				int cmp = 0;
				for (int k = j * 2 * i; k < (j * 2 + 1) * i; k++) {
					if (li[entry[k]] < li[entry[k + i]]) {
						cmp = 1;
					}
					else if (li[entry[k]] > li[entry[k + i]]) {
						cmp = -1;
					}
					if (cmp) break;
				}
				if (cmp == -1) {
					for (int k = j * 2 * i; k < (j * 2 + 1) * i; k++) {
						entry[k] ^= entry[k + i] ^= entry[k] ^= entry[k + i];
					}
				}
			}
		}


		loop(i, (1 << n)) {
			printf("%c", li[entry[i]]);
		}
		printf("\n");
	}
	else {
		printf("IMPOSSIBLE\n");
	}
}

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t = si();
	loopi(i, t) {
		printf("Case #%d: ", i); solve();
	}
}