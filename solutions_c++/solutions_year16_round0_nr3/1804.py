#include <cstdio>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include "BigIntegerLibrary.hh"

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define int64 long long

int b[32];

int main() {
	srand(time(0));
	int c = 32, n = 500;
	puts("Case #1:");
	set<BigInteger> ans;
	while (n > 0) {
		b[0] = b[c-1] = 1;
		FOR(i, 1, c-2) b[i] = rand() % 2;
		bool ok = 1;
		BigInteger x;
		vector<int> factor;
		FOR(base, 2, 10) if (ok) {
			x = 0;
			REP(i, c) x = x * base + b[i];
			// cout << x << endl;
			ok = 0;
			for (int f = 2; f <= 30000; ++f) if (x % f == 0) {
				ok = 1;
				factor.push_back(f);
				break;
			}
			// if (!ok) puts("FAIL");
		}
		if (ok && ans.find(x) == ans.end()) {
			ans.insert(x);
			--n;
			REP(i, c) printf("%d", b[i]);
			REP(i, 9) printf(" %d", factor[i]);
			puts("");
		}
	}
}
