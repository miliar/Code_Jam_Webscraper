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

int a[10010];

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int n, C;
		cin >> n >> C;
		REP(i, n) cin >> a[i];
		sort(a, a+n);
		int ans = 0;
		int L = 0, R = n-1;
		while (L <= R) {
			++ans;
			if (L == R) break;
			if (a[L] + a[R] <= C) ++L, --R;
			else --R;
		}
		printf("Case #%d: %d\n", cN, ans);
	}
}
