#include <bits/stdc++.h>

using namespace std;

int T, N;
char a[5][5];
bool b[5][5];
bool visr[5];

bool check() {
	memset(visr, 0, sizeof(visr));
	for(int i = 0; i < N; i ++) if(!visr[i]) {
		int c = 0, d = 1;
		for(int j = 0; j < N; j ++) if(b[i][j]) {
			c ++;
		}
		for(int k = i+1; k < N; k ++) if(!visr[k]) {
			bool ok = 0;
			for(int j = 0; j < N && !ok; j ++) if(b[i][j] && b[k][j]) {
				ok = 1;
			}
			if(ok) {
				for(int j = 0; j < N; j ++) if(b[i][j] != b[k][j]) {
					return 0;
				}
				visr[k] = 1;
				d ++;
			}
		}
		if(c != d) return 0;
		visr[i] = 1;
	}
	return 1;
}


int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas ++) {
		scanf("%d", &N);
		for(int i = 0; i < N; i ++) {
			scanf("%s", a[i]);
		}
		int res = N*N;
		for(int mask = 0; mask < (1 << N*N); mask ++) {
			for(int i = 0; i < N*N; i ++) {
				if(a[i/N][i%N] == '1' || (mask & (1 << i))) {
					b[i/N][i%N] = 1;
				} else {
					b[i/N][i%N] = 0;
				}
			}
			if(check()) {
				res = min(res, __builtin_popcount(mask));
			}
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}
