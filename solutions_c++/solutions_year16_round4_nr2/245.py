#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for (int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define PB push_back

double p[210], pr[2][210];

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int n, k;
		cin >> n >> k;
		REP(i, n) cin >> p[i];
		sort(p, p+n);
		double ma = 0;
		FOR(low, 0, k) {
			int o = 0;
			memset(pr[o], 0, sizeof(pr[o]));
			pr[0][0] = 1;
			REP(i, n) {
				if (i >= low && i < n-k+low) continue;
				o = 1-o;
				memset(pr[o], 0, sizeof(pr[o]));
				double q = p[i];
				pr[o][0] = (1-q) * pr[1-o][0];
				FOR(j, 1, k) pr[o][j] = q * pr[1-o][j-1] + (1-q) * pr[1-o][j];
			}
			ma = max(ma, pr[o][k/2]);
		}
		printf("Case #%d: %.9lf\n", cN, ma);
	}
}
