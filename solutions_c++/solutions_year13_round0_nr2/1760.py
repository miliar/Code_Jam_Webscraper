#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string>
using namespace std;
#define N 105

int test, precnt, k;
int n, m, g[N][N], cnt, check[N][N], temp, num, minv;
bool good;
FILE *fo = fopen("output.txt","w");
/*
bool process()
{
	cnt = n*m;
	while(cnt > 0) {
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++)
				printf("%d ", check[i][j]);
			printf("\n");
		}
		
		precnt = 0;
		minv = 999999999;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				if(check[i][j] == 0)
					minv = min(minv, g[i][j]);
		
		//printf("%d\n", minv);

		// left -> right
		for(int i = 0; i < n; i++) {
			k = -1;
			for(int j = 0; j < m; j++) {
				if(check[i][j] == 0) {
					num = g[i][j];
					k = j;
					break;
				}
			}
			if(k == -1) continue;
			//num = g[i][0];
			//if(num != minv || check[i][0] == 1) continue;
			if(num != minv) continue;
			good = true;
			//printf("%d %d\n", i, k);
			for(int j = k+1; j < m; j++) {
				if(check[i][j] == 1) continue;
				if(g[i][j] != num) {
					good = false;
					break;
				}
				//printf("%d\n", j);
			}
			if(good) {
				for(int j = 0; j < m; j++) {
					if(check[i][j] == 0) precnt++;
					check[i][j] = 1;
				}
				//break;
			}
		}

		// right -> left
		for(int i = 0; i < n; i++) {
			k = -1;
			for(int j = m-1; j >= 0; j--) {
				if(check[i][j] == 0) {
					num = g[i][j];
					k = j;
					break;
				}
			}
			if(k == -1) continue;
			//num = g[i][m-1];
			//if(num != minv || check[i][m-1] == 1) continue;
			if(num != minv) continue;
			good = true;
			for(int j = k-1; j >= 0; j--) {
				if(check[i][j] == 1) continue;
				if(g[i][j] != num) {
					good = false;
					break;
				}
			}
			if(good) {
				for(int j = m-1; j >= 0; j--) {
					if(check[i][j] == 0) precnt++;
					check[i][j] = 1;
				}
				//break;
			}
		}
		
		// top -> bottom
		for(int j = 0; j < m; j++) {
			k = -1;
			for(int i = 0; i < n; i++) {
				if(check[i][j] == 0) {
					num = g[i][j];
					k = i;
					break;
				}
			}
			if(k == -1) continue;
			//num = g[0][j];
			//if(num != minv || check[0][j] == 1) continue;
			if(num != minv) continue;
			good = true;
			for(int i = k+1; i < n; i++) {
				if(check[i][j] == 1) continue;
				if(g[i][j] != num) {
					good = false;
					break;
				}
			}
			if(good) {
				for(int i = 0; i < n; i++) {
					if(check[i][j] == 0) precnt++;
					check[i][j] = 1;
				}
				//break;
			}
		}

		// bottom -> top
		for(int j = 0; j < m; j++) {
			k = -1;
			for(int i = m-1; i >= 0; i--) {
				if(check[i][j] == 0) {
					num = g[i][j];
					k = i;
					break;
				}
			}
			if(k == -1) continue;
			//num = g[n-1][j];
			//if(num != minv || check[n-1][j] == 1) continue;
			if(num != minv) continue;
			good = true;
			for(int i = k-1; i >= 0; i--) {
				if(check[i][j] == 1) continue;
				if(g[i][j] != num) {
					good = false;
					break;
				}
			}
			if(good) {
				for(int i = n-1; i >= 0; i--) {
					if(check[i][j] == 0) precnt++;
					check[i][j] = 1;
				}
				//break;
			}
		}
		
		//printf("precnt : %d\n", precnt);
		if(precnt == 0)
			return false;

		cnt -= precnt;
	}
	return true;
}
*/

bool process2(int i, int j)
{
	int k;
	for(k = 0; k < n; k++) {
		if(g[k][j] > g[i][j]) break;
	}
	if(k == n) return true;
	for(k = 0; k < m; k++) {
		if(g[i][k] > g[i][j]) break;
	}
	if(k == m) return true;
	return false;
}

bool process()
{
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(!process2(i, j)) return false;
		}
	}
	return true;
}

int main()
{
	//FILE *fp = fopen("input.txt", "r");
	FILE *fp = fopen("B-large.in", "r");
	fscanf(fp, "%d", &test);
	for(int t = 1; t <= test; t++) {
		fscanf(fp, "%d %d", &n, &m);
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				fscanf(fp, "%d", &g[i][j]);
				check[i][j] = 0;
			}
		}
		
		if(process())
			fprintf(fo, "Case #%d: YES\n", t);
		else
			fprintf(fo, "Case #%d: NO\n", t);
	}

	fclose(fp);
	fclose(fo);
	//scanf("%d");
	return 0;
}