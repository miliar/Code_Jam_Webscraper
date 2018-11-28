#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>

using namespace std;

int next_perm(int *p, int n)
{
    int i, j, k, tmp;
    for(i = n - 1; i > 0 && p[i-1] >= p[i]; i--);
    if(i == 0) return 0;
    for(j = n - 1; j > i && p[i-1] >= p[j]; j--);
    tmp = p[i-1], p[i-1] = p[j], p[j] = tmp;
    for(k = 0; k <= ((n-1)-i)/2; k++)
        tmp = p[i+k], p[i+k] = p[(n-1)-k], p[(n-1)-k] = tmp;
    return 1;
}

int T, r, c, m;
char data[5][5];
int dx[8] = {1, 1, 0, -1, -1, -1, 0, 1};
int dy[8] = {0, 1, 1, 1, 0, -1, -1, -1};

void dfs(int y, int x)
{
	int i, j;
	int nx, ny;

	int cnt = 0;
	for (i=0; i<8; i++) {
			nx = x + dx[i];
			ny = y + dy[i];
			if (nx>=0 && nx<c && ny>=0 && ny<r && data[ny][nx] == '*') cnt++;
	}
	data[y][x] = cnt - '0';
	if (cnt>0) return;

	for (i=0; i<8; i++) {
			nx = x + dx[i];
			ny = y + dy[i];
			if (nx>=0 && nx<c && ny>=0 && ny<r && data[ny][nx] == '.')
				dfs(ny, nx);
	}
}

int main(void)
{
	int i, j, k;
	int sx, sy;

	scanf ("%d ", &T);
	for (int t=0; t<T; t++) {
		memset(data, 0, sizeof(data));
		scanf("%d%d%d ", &r, &c, &m);

		int *line = (int *)calloc(r*c, sizeof(int));
		for (i=0; i<r*c; i++) line[i] = 0;
		for (i=0; i<m; i++) line[r*c -2 - i] = 1;
		line[r*c - 1] = 2;

		bool res;

		do {
			k = 0;
			for (i=0; i<r; i++)
				for (j=0; j<c; j++) {
					if (line[k] == 0)
						data[i][j] = '.';
					else if (line[k] == 1)
						data[i][j] = '*';
					if (line[k] == 2)
						data[i][j] = 'c';
					k++;
				}

			bool sp = false;
			for (i=0; i<r; i++) {
				for (j=0; j<c; j++) {
					if (data[i][j] == 'c') {
						sx = j;
						sy = i;
						sp = true;
						break;	
					}
				}
				if (sp) break;
			}
			
			dfs(sy, sx);
			res = true;
			for (i=0; i<r; i++) {
				for (j=0; j<c; j++) {
					if (data[i][j] == '.') {
						res = false;
						break;
					}
				}
				if (!res) break;
			}

			if (res) break;

    } while(next_perm(line, r*c));

		free(line);

		printf("Case #%d:\n", t+1);
		if (res) {
			for (i=0; i<r; i++) {
				for (j=0; j<c; j++) 
					if (i==sy && j==sx)	
						printf("c");
					else if (data[i][j] == '*')
						printf("*");
					else
						printf(".");
				puts("");
			}
		} else {
			printf("Impossible\n");
		}
	}

  return 0;
}
