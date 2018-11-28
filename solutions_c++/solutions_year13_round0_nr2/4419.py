#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std;

int lawn[100][100];
bool mark[100][100];
int row_max[100];
int col_max[100];
int steps;
int N, M;

inline void Input()
{
	scanf("%d %d\n", &N, &M);
	steps = 0;
	//memset(mark, false,sizeof (mark));
	memset(row_max, 0,sizeof (row_max));
	memset(col_max, 0,sizeof (col_max));
	for (int i = 0; i< N; i++) {
		row_max[i] = 0;
	}
	for (int i = 0; i< M; i++) {
		col_max[i] = 0;
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			mark[i][j] = false;
			scanf("%d", &lawn[i][j]);
			if (lawn[i][j] > row_max[i]) {
				row_max[i] = lawn[i][j];
			}
			if (lawn[i][j] > col_max[j]) {
				col_max[j] = lawn[i][j];
			}
		}
	}
}

bool Execute()
{
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (lawn[i][j] == row_max[i] && !mark[i][j]) {
				mark[i][j] = true;
				steps++;
			}
		}
	}
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (lawn[j][i] == col_max[i] && !mark[j][i]) {
				mark[j][i] = true;
				steps++;
			}
		}
	}
	if (steps != N*M) {
		return false;
	} else {
		return true;
	}
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for (int i = 1; i <= T; i++) {
		Input();
		if (Execute()) {
			printf("Case #%d: YES\n", i);
		} else {
			printf("Case #%d: NO\n", i);
		}
	}
	return 0;
}	
