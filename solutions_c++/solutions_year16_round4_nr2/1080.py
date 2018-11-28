#include <bits/stdc++.h>
using namespace std;
vector <int> mask[17][17];


int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.ou", "w", stdout);
	for(int i = 1; i <= 16; i++) {
		for(int j = 1; j < (1 << i); j++) {
			int c = __builtin_popcount(j);
			mask[i][c].push_back(j);
		}
	}
	int T, n, k, cases = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d", &n, &k);
		double p[16];
		double ans = 0.0;
		for(int i = 0; i < n; i++) scanf("%lf", &p[i]);
		for(int i = 0; i < mask[n][k].size(); i++) {
			int z[k];
			int idx = 0, m = mask[n][k][i];
			for(int j = 0; j < n; j++) if(m >> j & 1) z[idx++] = j;
			//for(int j = 0; j < idx; j++) printf("%d ", z[j]); printf("\n");
			double sum = 0;
			for(int j = 0; j < mask[k][k / 2].size(); j++) {
				int y = mask[k][k / 2][j];
				double u = 1.0;
				for(int r = 0; r < k; r++) {
					if(y >> r & 1) {
						u *= p[z[r]];
					} else {
						u *= 1.0 - p[z[r]];
					}
				}
				sum += u;
			}
			ans = max(ans, sum);
		}
		printf("Case #%d: %.10f\n", ++cases, ans);
	}
	return 0;
}
