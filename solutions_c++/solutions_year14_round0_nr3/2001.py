#include<iostream>
using namespace std;

int map[5][5];
int f[5][5];
int b[25];
int qx[25];
int qy[25];
bool visit[5][5];
const int tx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
const int ty[8] = {-1, 0, 1, 1, 1, 0, -1, -1};

int main() {
	int m, r, c;
	int testcases;
	scanf("%d", &testcases);
	b[0] = 1;
	for (int i = 1; i < 25; i++)
		b[i] = b[i - 1] * 2;
	for (int test = 0; test < testcases; test++) {
		scanf("%d %d %d", &r, &c, &m);
		
		if (m == r * c - 1) {
			printf("Case #%d:\n", test + 1);
			printf("c");
			for (int i = 0; i < r; i++) {
				int tmp = c;
				if (i == 0) tmp --;
				for (int j = 0; j < tmp; j++) {
					printf("*");
				}
				printf("\n");
			} 
			continue;
		}
		bool found = false;
		for (int p = 0; p < 1 << (r*c); p++) {
			int x = p;
			int tmp_m = 0;
			for (int i = r * c - 1; i >= 0; i--) {
				map[i / c][i % c] = x / b[i];
				tmp_m += map[i / c][i % c];
				x = x % b[i];
			}
			if (tmp_m != m)
				continue;
			int start_x = -1, start_y = -1;
			for (int i = 0; i < r; i++)
				for (int j = 0; j < c; j++) {
					if (map[i][j] == 1) {
						f[i][j] = -1;
						continue;
					}
					int tot = 0;
					for (int t = 0; t < 8; t++) {
						int xx = i + tx[t], yy = j + ty[t];
						if (xx < 0 || xx >= r || yy < 0 || yy >= c)
							continue;
						if (map[xx][yy] == 1)
							tot ++;
					}
					f[i][j] = tot;
					if (tot == 0) {
						start_x = i;
						start_y = j;
					}
				}
			/*
			printf("generated matrix\n");
			printf("%d\n", 1 << (r*c));
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					printf("%d", map[i][j]);
					if (j < c - 1)
						printf(" ");
				}
				printf("\n");
			}
			printf("\n");

			printf("flags\n");
			printf("%d\n", 1 << (r*c));
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					printf("%d", f[i][j]);
					if (j < c - 1)
						printf(" ");
				}
				printf("\n");
			}*/
			if (start_x == -1) 
				continue;

			for (int i = 0; i < 5; i++)
				for (int j = 0; j < 5; j++)
					visit[i][j] = false;
			int head = 0, tail = 0;
			qx[0] = start_x;
			qy[0] = start_y;
			visit[start_x][start_y] = true;
			int tot = 1;
			while (head <= tail) {
				int xx, yy;
				for (int t = 0; t < 8; t++) {
					int xx = qx[head] + tx[t], yy = qy[head] + ty[t];
					if (xx < 0 || xx >= r || yy < 0 || yy >= c)
						continue;
					if (visit[xx][yy])
						continue;
					tot ++;
					visit[xx][yy] = true;
					if (f[xx][yy] == 0) {
						tail ++;
						qx[tail] = xx;
						qy[tail] = yy;
					}
				}
				head ++;
			}
			//printf("tot = %d\n", tot);
			if (tot + m == r * c) {
				printf("Case #%d:\n", test + 1);
				for (int i = 0; i < r; i++) {
					for (int j = 0; j < c; j++) {
						if (i == start_x && j == start_y)
							printf("c");
						else if (map[i][j] == 1)
							printf("*");
						else
							printf(".");
					}
					printf("\n");
				}
				found = true;
				break;
			}
		}
		if (!found) {
			printf("Case #%d:\n", test + 1);
			printf("Impossible\n");
		}
	}
}