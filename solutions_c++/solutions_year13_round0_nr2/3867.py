//// GCJ 2013.04.13 Qualification B
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define N 110

int map[N][N], n, m;
FILE *fp, *fw;

int main() {
	int cse, i, j, k, h, g = 1, cnt, mx;
	bool res, ok;
	fp = fopen("/home/uriel/workspace/B-large.in", "r");
	fw = fopen("/home/uriel/workspace/outB_l.txt", "w");
	fscanf(fp, "%d", &cse);
	while(cse--) {
		fscanf(fp, "%d %d", &n, &m);
		for(i = 0; i < n; ++i) {
			for(j = 0; j < m; ++j) {
				fscanf(fp, "%d", &map[i][j]);
			}
		}
		cnt = 0;
		ok = true;
		while(cnt < n * m) {
			mx = 101;
//			for(i = 0; i < n; ++i) {
//				for(j = 0; j < m; ++j) {
//					printf("%d ", map[i][j]);
//				}
//				puts("");
//			}
//			puts("");
			for(i = 0; i < n; ++i) {
				for(j = 0; j < m; ++j) {
					if(map[i][j] < mx) mx = map[i][j];
				}
			}
			res = false;
			for(i = 0; i < n; ++i) {
				for(j = 0; j < m; ++j) {
					if(map[i][j] == mx) {
						for(k = 0; k < n; ++k) {
							if(map[k][j] != mx && map[k][j] != 101) break;
						}
						if(k == n) {
							res = true;
							for(k = 0; k < n; ++k) {
								if(map[k][j] != 101) {
									map[k][j] = 101;
									cnt++;
								}
							}
						}
						for(k = 0; k < m; ++k) {
							if(map[i][k] != mx && map[i][k] != 101) break;
						}
						if(k == m) {
							res = true;
							for(k = 0; k < m; ++k) {
								if(map[i][k] != 101) {
									map[i][k] = 101;
									cnt++;
								}
							}
						}
					}
				}
			}
			if(!res) {
				ok = false;
				break;
			}
		}
		if(ok) {
			fprintf(fw, "Case #%d: YES\n", g++);
		}
		else {
			fprintf(fw, "Case #%d: NO\n", g++);
		}
	}
	fclose(fp);
	fclose(fw);
	return 0;
}
