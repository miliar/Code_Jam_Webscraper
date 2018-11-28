#include <cstdio>
#include <stdlib.h>
#include <memory.h>

FILE *fin = fopen("B.in", "r");
FILE *fout = fopen("B.out", "w");

const int MAXN = 111;

#define ROW 0
#define COL 1

int a[MAXN][MAXN];
int b[MAXN][MAXN];

int mark[MAXN][MAXN];

bool canMow(int n, int m){
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (mark[i][j] != 2) return false;
		}
	}
	return true;
}

bool canMow(int idx, int type, int n, int m){
	if (type == ROW){
		for (int i = 0; i < m; i++){
			if (mark[idx][i] == 2) return false;
		}
		return true;
	}
	else if (type == COL){
		for (int i = 0; i < n; i++){
			if (mark[i][idx] == 2) return false;
		}
		return true;
	}
}

void mow(int idx, int type, int n, int m){
	if (type == ROW){
		for (int i = 0; i < m; i++){
			mark[idx][i] = 1;
		}
	}
	else if (type == COL){
		for (int i = 0; i < n; i++){
			mark[i][idx] = 1;
		}
	}
}

void tryToMow(int n, int m){
	for (int i = 0; i < n; i++){
		if (canMow(i, ROW, n, m)){
			mow(i, ROW, n, m);
		}
	}

	for (int i = 0; i < m; i++){
		if (canMow(i, COL, n, m)){
			mow(i, COL, n, m);
		}
	}
}

void markMowed(int k, int n, int m){
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (a[i][j] == k && mark[i][j] == 1) mark[i][j] = 2;
			else if (mark[i][j] == 1) mark[i][j] = 0;
		}
	}
}

int main(){
	int t;
	fscanf(fin, "%d", &t);

	for (int test = 1; test <= t; test++){
		int n, m;
		fscanf(fin, "%d%d", &n, &m);

		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				fscanf(fin, "%d", &a[i][j]);
			}
		}

		memset(mark, 0, sizeof(mark));
		for (int k = 100; k >= 1; k--){
			tryToMow(n, m);
			markMowed(k, n, m);
		}

		fprintf(fout, "Case #%d: ", test);

		bool tt = canMow(n ,m);

		if (tt){
			fprintf(fout, "YES\n");
		}
		else {
			fprintf(fout, "NO\n");
		}
	}

	fclose(fin);
	fclose(fout);
//	system("pause");
	return 0;
}