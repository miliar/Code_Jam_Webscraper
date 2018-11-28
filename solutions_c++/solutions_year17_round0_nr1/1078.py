#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		string s;
		int k;
		cin >> s >> k;
		int n = s.size(), ans = 0;
		bool ok = 1;
		REP(i, n) {
			if (i+k <= n && s[i] == '-') {
				++ans;
				REP(j, k) s[i+j] = '+' + '-' - s[i+j];
			}
			if (i+k > n && s[i] == '-') ok = 0;
		}
		printf("Case #%d: ", cN);
		if (ok) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
}
