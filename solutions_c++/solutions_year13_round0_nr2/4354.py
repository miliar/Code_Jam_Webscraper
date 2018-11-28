#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define debug(x) cout<<(#x)<<":"<<(x)<<endl

int h[110][110], rH[110], cH[110];

int main() {
	int tN;
	scanf("%d", &tN);
	FOR(cN, 1, tN) {
		int r, c;
		scanf("%d%d", &r, &c);
		REP(i, r) rH[i] = 0;
		REP(j, c) cH[j] = 0;
		REP(i, r) REP(j, c) {
			scanf("%d", &h[i][j]);
			rH[i] = max(rH[i], h[i][j]);
			cH[j] = max(cH[j], h[i][j]);
		}
		bool ok = 1;
		REP(i, r)
		REP(j, c) if (h[i][j] != min(rH[i], cH[j])) ok = 0;
		printf("Case #%d: ", cN);
		if (ok) puts("YES"); else puts("NO");
	}
}
