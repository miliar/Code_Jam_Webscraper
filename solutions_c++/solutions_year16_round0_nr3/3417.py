#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long long base[11][17];
long long sumv[11];
int nowcount;
int N, J;
FILE *fo;
void makebase(){
	for (int i = 2; i < 11; i++) {
		base[i][0] = 1;
		for (int j = 1; j < 17; j++) {
			base[i][j] = base[i][j - 1] * i;
		}
	}
}


void generate(bool visited[17], int nowindex) {
	if (nowcount == J)
		return;

	if (nowindex == N-1) {
		long long tris[11];
		for (int b = 2; b < 11; b++) {
			long long sum = sumv[b];
			for (int i = 1; i < N-1; i++) {
				if (visited[i])
					sum += base[b][i];
			}
			tris[b] = -1;
			long double x = 0.5*(sum / 1 + 1);
			for (int i = 0; i < 30; i++) {
				x = 0.5 * (x + (sum / x));
			}
			for (long long j = 2, max = x + 1; j < max; j++) {
				if (sum % j == 0) {
					tris[b] = j;
					j = max;
				}
			}
		}
		for (int b = 2; b < 11; b++) {
			if (tris[b] < 0)
				return;
		}
		for (int i = N - 1; i >= 0; i--) {
			if (visited[i])
				fprintf(fo, "1");
			else
				fprintf(fo, "0");
		}
		for (int b = 2; b < 11; b++) {
			fprintf(fo, " %d", tris[b]);
		}
		fprintf(fo, "\n");
		nowcount++;
		return;
	}

	visited[nowindex] = false;
	generate(visited, nowindex+1);
	visited[nowindex] = true;
	generate(visited, nowindex+1);
	return;
}

void main() {
	int testnum;
	bool visited[17];
	FILE *f = fopen("C-small-attempt1.in", "r");
	fo = fopen("out_C1.txt", "w");
	makebase();

	fscanf(f, "%d", &testnum);
	for (int t = 1; t <= testnum; t++) {
		fscanf(f, "%d %d", &N, &J);
		for (int i = 0; i < 17; i++)
			visited[i] = false;
		visited[0] = true;
		visited[N-1] = true;
		nowcount = 0;

		for (int i = 2; i < 11; i++) {
			sumv[i] = base[i][N-1] + 1;
		}
		fprintf(fo, "Case #%d:\n", t);
		generate(visited, 1);
	}
}