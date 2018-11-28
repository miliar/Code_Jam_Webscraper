#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;
#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)

int p[1010];

int main() {
	int tN;
	scanf("%d", &tN);
	FOR(cN, 1, tN) {
		int n;
		scanf("%d", &n);
		REP(i, n) scanf("%d", &p[i]);
		int ans = 1000;
		FOR(eat, 1, 1000) {
			int spe = 0;
			REP(i, n) spe += (p[i] / eat - int(p[i] % eat == 0));
			ans = min(ans, eat + spe);
		}
		printf("Case #%d: %d\n", cN, ans);
	}
}
