#include <stdio.h>
#include <algorithm>

using namespace std;

const int MSIZE = 100;

int t;
int n, m;
int mas[MSIZE][MSIZE];

int row[MSIZE];
int col[MSIZE];

void foo(int it){
	int n, m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &mas[i][j]);
	for (int i = 0; i < n; i++){
		int lm = -1;
		for (int j = 0; j < m; j++)
			lm = max(lm, mas[i][j]);
		row[i] = lm;
	}
	for (int i = 0; i < m; i++){
		int lm = -1;
		for (int j = 0; j < n; j++)
			lm = max(lm, mas[j][i]);
		col[i] = lm; 
	}
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (mas[i][j] < row[i] && mas[i][j] < col[j]){
				printf("Case #%d: NO\n", it);
				return;
			}
		}
	}
	printf("Case #%d: YES\n", it);
	return;
}

int main(){
	freopen("input.txt", "r", stdin);


	scanf("%d", &t);
	for (int i = 0; i < t; i++)
		foo(i + 1);


	return 0;
}