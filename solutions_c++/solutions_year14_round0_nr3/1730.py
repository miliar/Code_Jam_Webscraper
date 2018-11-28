#include <iostream>
#include <vector>
#include <stdio.h>
#include <queue>
using namespace std;

int r, c, m;
int found = 0;

int a[64][64];

FILE* fin = NULL;
FILE* fout = NULL;

void print(int startr, int startc) {
	for(int i = 0; i < r; i++) {
		for(int j = 0; j < c; j++) {
			if (i == startr && j == startc) {
				fprintf(fout, "%c", 'c');
			} else if (a[i][j] == 0) {
				fprintf(fout, "%c", '.');
			} else {
				fprintf(fout, "%c", '*');
			}
		}
		fprintf(fout, "\n");
	}
}


int visit[64][64];
int wy[8][2] = {
	{-1,-1},
	{-1, 0},
	{-1, 1},
	{0, -1},
	{0, 1},
	{1, -1},
	{1, 0},
	{1, 1}
};



int judge(int sr, int sc) {
	int num = 0;
	
	for(int i = 0; i < r; ++i) {
		for(int j = 0; j < c; ++j) {
			visit[i][j] = 0;
		}
	}
	visit[sr][sc] = 1;

	queue<int> q;
	q.push(sr * c + sc);

	while (!q.empty()) {
		int temp = q.front();
		q.pop();
		int nowr = temp / c;
		int nowc = temp % c;

		bool hasmine = 0;
		for(int i = 0; i < 8; i++) {
			int tempr = nowr + wy[i][0];
			int tempc = nowc + wy[i][1];

			if (tempr >= 0 && tempr <= r && tempc  >= 0 && tempc <= c) {
				if (a[tempr][tempc] != 0) {
					hasmine = true;
					break;
				}
			}
		}

		if (!hasmine) {
			for(int i = 0; i < 8; i++) {
				int tempr = nowr + wy[i][0];
				int tempc = nowc + wy[i][1];

				if (tempr >= 0 && tempr <= r && tempc  >= 0 && tempc <= c) {
					if (!visit[tempr][tempc]) {
						visit[tempr][tempc] = 1;
						q.push(tempr * c + tempc);
					}
				}
			}
		}
	}

	
	for(int i = 0; i < r; ++i) {
		for(int j = 0; j < c; ++j) {
			num += visit[i][j];
		}
	}


	return num == r * c - m;
}

void solve(int nowr, int nowc, int nowm) {
	if (found) {
		return;
	}
	if (nowr >= r) {
		if (nowm != m) {
			return;
		}

		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				if (a[i][j] == 0) {
					if (judge(i, j)) {
						print(i, j);
						found = true;
						return;
					}
				}
			}
		}
		return;
	}

	int nextr = 0;
	int nextc = 0;

	if (nowc == c - 1) {
		nextr = nowr + 1;
		nextc = 0;
	} else {
		nextr = nowr;
		nextc = nowc + 1;
	}

	a[nowr][nowc] = 0;
	solve(nextr, nextc, nowm);

	a[nowr][nowc] = 1;
	solve(nextr, nextc, nowm + 1);
}

int main() {
	int n;
	
	fin = fopen("C-small-attempt0.in", "r");
	fout = fopen("output.txt" ,"w");

	fscanf(fin, "%d", &n);

	for(int t = 1; t <= n; ++t) {
		printf("case#%d\n", t);

		fscanf(fin, "%d%d%d", &r, &c, &m);
		found = 0;
		memset(a, 0, sizeof(a));

		fprintf(fout, "Case #%d:\n", t);
		solve(0, 0, 0);
		if (!found) {
			fprintf(fout, "Impossible\n");
		}
	}
	fclose(fin);
	fclose(fout);
}