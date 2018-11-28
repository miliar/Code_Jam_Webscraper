#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>

int N;
int order[12][3];

int rps(int a, int b) {
	switch (a + b) {
	case 1:
		return 0;
	case 2:
		return 2;
	case 3:
		return 1;
	default:
		exit(0);
	}
	return -1;
}

void gen(int n, char * p, char * a) {
	char t[4096], x, y;
	if (n) {
		gen(n - 1, p, t);
		for (int i = 0; i < (1 << (n - 1)); ++i) {
			switch (t[i]) {
			case 0:
				x = 0;
				y = 1;
				break;
			case 1:
				x = 1;
				y = 2;
				break;
			case 2:
				x = 2;
				y = 0;
				break;
			}
			if (order[N - n][x] > order[N - n][y]) {
				a[2 * i] = y;
				a[2 * i + 1] = x;
			} else {
				a[2 * i] = x;
				a[2 * i + 1] = y;
			}
		}
	} else {
		a[0] = p[0];
	}
}

int main() {
	FILE * fin = fopen("input.in", "r"), * fout = fopen("output.out", "w");
	int T, t, R, P, S, b;
	int temp[3] = {0, 1, 2}; //prs
	order[0][0] = 0;
	order[0][1] = 1;
	order[0][2] = 2;
	for (int i = 1; i < 12; ++i) {
		order[i][rps(temp[0], temp[1])] = 0;
		order[i][rps(temp[0], temp[2])] = 1;
		order[i][rps(temp[1], temp[2])] = 2;
		temp[order[i][0]] = 0;
		temp[order[i][1]] = 1;
		temp[order[i][2]] = 2;
	}
	fscanf(fin, "%d\n", &T);
	char a[4097], c, * p = &c;
	for (t = 1; t <= T; ++t) {
		fscanf(fin, "%d%d%d%d\n", &N, &R, &P, &S);
		b = 0;
		if (R == P && (S == R + 1 || S == R - 1)) {
			c = (N + 2) % 3;
		} else if (R == S && (P == R + 1 || P == R - 1)) {
			c = N % 3;
		} else if (P == S && (R == P + 1 || R == P - 1)) {
			c = (N + 1) % 3;
		} else {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", t);
			b = 1;
		}
		if (!b) {
			gen(N, p, a);
			for (int i = 0; i < (1 << N); ++i) {
				if (!a[i]) a[i] = 'P';
				else a[i] += 'Q';
			}
			a[1 << N] = '\0';
			fprintf(fout, "Case #%d: %s\n", t, a);
		}
	}
	return 0;
}
