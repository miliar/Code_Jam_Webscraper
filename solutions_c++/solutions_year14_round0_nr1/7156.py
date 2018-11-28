#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main() {
	int t, ans;
	scanf("%d", &t);
	for(int cnt = 1; cnt <= t; cnt++) {
		int rawr;
		scanf("%d", &ans);
		bool tick[17];
		fill(tick, tick+17, false);
		for(int c = 0; c < 16; c++) {
			scanf("%d", &rawr);
			if((c/4)+1 == ans) tick[rawr] = true;
		}
		int cc = 0;
		int res;
		scanf("%d", &ans);
		for(int c = 0; c < 16; c++) {
			scanf("%d", &rawr);
			if((c/4)+1 == ans && tick[rawr]) { res = rawr; cc++; }
		}
		if(cc == 0) printf("Case #%d: Volunteer cheated!\n", cnt);
		else if(cc > 1) printf("Case #%d: Bad magician!\n", cnt);
		else printf("Case #%d: %d\n", cnt, res);
	}
}

/*#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main() {
	int t, n;
	scanf("%d", &t);
	for(; t > 0; t--) {
		scanf("%d", &n);
		int front[n];
		int right[n];
		int maxf[n];
		int maxr[n];
		int grid[n][n];
		memset(grid, 0, sizeof(int)*n*n);
		fill(maxf, maxf+n, 0);
		fill(maxr, maxr+n, 0);
		for(int c = 0; c < n; c++)
			scanf("%d", &front[c]);
		for(int c = 0; c < n; c++)
			scanf("%d", &right[c]);
		int mi = 0;
		int add = 0;
		
		for(int c = 0; c < n; c++) {
			for(int d = 0; d < n; d++) {
				if(front[c] == right[d]) {
					grid[n-d-1][c] = front[c];
					mi += front[c];
				}
			}
		}
		for(int c = 0; c < n; c++) {
			for(int d = 0; d < n; d++) {
				maxf[d] = max(maxf[d], grid[c][d]);
				maxr[n-c-1] = max(maxr[n-c-1], grid[c][d]);
			}
		}
		
		for(int c = 0; c < n; c++) {
			for(int d = 0; d < n; d++) {
				printf("%d ", grid[c][d]);
				if(grid[c][d] == 0) {
					grid[c][d] = min(maxf[d], maxr[n-c-1]);
					add += min(maxf[d], maxr[n-c-1]);
				}
			}
			printf("\n");
		}
		printf("Matty needs at least %d blocks, and can add at most %d extra blocks.\n", mi, add);
	}
}*/

/*#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main() {
	int n, A, B, C;
	scanf("%d", &n);
	for(; n > 0; n--) {
		bool found = false;
		scanf("%d%d%d", &A, &B, &C);
		int x, y, z;
		for(int c = 1; c < B; c++) {
			if(B%c == 0) {
				int g = B/c;
				for(int d = 1; d < g; d++) {
					if(g%d == 0) {
						int tx = c;
						int ty = d;
						int tz = g/d;
						if((tx*tx)+(ty*ty)+(tz*tz) == C) {
							if(tx+ty+tz == A) {
								if(!found) { x = tx; y = ty; z = tz; found = true; }
								else if(tx < x || (tx==x && ty < y) ||(tx==x && ty==y && tz<z)) {
									x = tx; y = ty; z = tz;
									found = true;
								}
							}
							else if(tx-ty-tz == A) {
								if(!found) { x = tx; y = ty; z = tz; found = true; }
								else if(tx < x || (tx==x && -ty < y) ||(tx==x && -ty==y && -tz<z)) {
									x = tx; y = -ty; z = -tz;
									found = true;
								}
							}
							else if(ty-tx-tz == A) {
								if(!found) { x = tx; y = ty; z = tz; found = true; }
								else if(-tx < x || (-tx==x && ty < y) ||(-tx==x && ty==y && -tz<z)) {
									x = -tx; y = ty; z = -tz;
									found = true;
								}
							}
							else if(tz-tx-ty == A) {
								if(!found) { x = tx; y = ty; z = tz; found = true; }
								else if(-tx < x || (-tx==x && -ty < y) ||(-tx==x && -ty==y && tz<z)) {
									x = -tx; y = -ty; z = tz;
									found = true;
								}
							}
						}
					}
				}
			}
		}
		if(!found) printf("No solution.\n");
		else printf("%d %d %d\n", x, y, z);
	}
}*/