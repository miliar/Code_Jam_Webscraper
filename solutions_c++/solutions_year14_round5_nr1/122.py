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

int a[1000010];
int64 sum[1000010];

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int n, p, q, r, s;
		cin >> n >> p >> q >> r >> s;
		REP(i, n) a[i] = (1LL*i*p+q) % r + s;
		sum[0] = 0;
		REP(i, n) sum[i+1] = sum[i] + a[i];
		// [0, a), [a, b), [b, n)
		int b = 0;
		int64 ans = 0;
		FOR(a, 0, n) {
			while (b <= n && abs((sum[n]-sum[b]) - (sum[b]-sum[a])) > abs((sum[n]-sum[b+1]) - (sum[b+1]-sum[a]))) ++b;
			ans = max(ans, sum[n] - max(sum[n]-sum[b], max(sum[b]-sum[a], sum[a]-sum[0])));
		}
		double ratio = 1. * ans / sum[n];
		printf("Case #%d: %.10lf\n", cN, ratio);
	}
}
