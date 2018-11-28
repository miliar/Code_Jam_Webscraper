#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define PB push_back

#define maxM 5010
#define maxN 2010
#define RED 0

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int n, L;
		cin >> n >> L;
		printf("Case #%d: ", cN);
		string s;
		bool nosol = 0;
		REP(i, n) {
			cin >> s;
			bool ok = 0;
			REP(j, s.size()) if (s[j] == '0') ok = 1;
			if (!ok) nosol = 1;
		}
		cin >> s;
		if (nosol) puts("IMPOSSIBLE");
		else if (L == 1) puts("? 0");
		else {
			REP(i, L) printf("0?");
			printf(" ");
			REP(i, L-1) printf("1");
			puts("");
		}
	}
}
