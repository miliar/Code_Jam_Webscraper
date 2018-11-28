#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <functional>
using namespace std;

typedef long long int64;
#define PB push_back
#define MP make_pair
#define debug(x) cout<<(#x)<<": "<<(x)<<endl
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define MOD 1000000007

int a[1010];

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int n;
		cin >> n;
		REP(i, n) cin >> a[i];
		int ans = 0;
		REP(i, n) {
			int L = 0, R = 0;
			FOR(j, 0, i-1) if (a[j] > a[i]) ++L;
			FOR(j, i+1, n-1) if (a[j] > a[i]) ++R;
			ans += min(L, R);
		}
		printf("Case #%d: %d\n", cN, ans);
	}
}
