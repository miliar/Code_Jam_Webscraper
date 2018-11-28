#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

#define MAXN 25

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

int a[MAXN][MAXN];
int n, m, k;
int N;


void rec(int x, int y) {
	a[x][y] = 2;
	for(int i=0; i<4; ++i) {
		int xx = x + dx[i];
		int yy = y + dy[i];
		if (a[xx][yy] == 0) rec(xx, yy);
	}
}

void debug() {
	for(int i=1; i<=n; ++i) {
		for(int j=1; j<=m; ++j) printf("%i ", a[i][j]);
		printf("\n");
	}
	printf("\n");
}

int main(){
    int tc;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    //freopen("C.in", "r", stdin);
    //freopen("C.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
		fprintf(stderr, "test %i\n", tt);
		int best = 1000;
        printf("Case #%i: ", tt);        
		scanf("%i %i %i", &n, &m, &k);
		N = 1<<(n*m);
		memset(a, 1, sizeof(a));
		for(int mask=0; mask<N; ++mask) {			
			int step = 0;
			int cnt  = 0;
			for(int i=1; i<=n; ++i) 
				for(int j=1; j<=m; ++j) {
					if ((mask >> step) & 1) {
						a[i][j] = 1; 
						cnt++;
					}else a[i][j] = 0;
					step++;
				}
			//debug();
			// check
			for(int i=1; i<=n; ++i) {
				if (a[i][1] == 0) rec(i, 1);
				if (a[i][m] == 0) rec(i, m);
			}

			for(int j=1; j<=m; ++j) {
				if (a[1][j] == 0) rec(1, j);
				if (a[n][j] == 0) rec(n, j);
			}

			int total = 0;
			for(int i=1; i<=n; ++i) 
				for(int j=1; j<=m; ++j) if (a[i][j] <= 1) total++;

			if (total >= k && cnt < best) {
				best = cnt;
				//debug();
				//printf("best = %i\n\n", cnt);
			}			

		}

		printf("%i\n", best);

    }

    return 0;
}

