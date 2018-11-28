#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cfloat>
#include <climits>
#include <algorithm>
#include <numeric>
using namespace std;

typedef long long LL;

template<class T> inline void checkmax(T& a, const T& b) { if ( a < b ) a = b; }
template<class T> inline void checkmin(T& a, const T& b) { if ( a > b ) a = b; }
template<class T> inline T sqr(T& a) { return a * a; } 

LL calc1(LL n, LL p) {
	if ( p == (1LL << n) ) return p - 1;
	LL UP = 1LL << (n-1);
	LL r = 0;
	for (;;) {
		if ( p <= UP ) break;
		p -= UP;
		r++;
		UP /= 2;
	}
	return (1LL << (r + 1)) - 2;
}

LL adjust(LL n, LL v) {
	return (1LL << n) - v;
}

LL calc2(LL n, LL p) {
	for ( int i = 0; i <= n; ++i ) {
		if ( p >= (1LL << n - i) ) return adjust( n, (1LL << i) );
	}
}

void solve( int ri ) {
	LL n, k; cin >> n >> k;
	printf("Case #%d: ", ri);
	cout << calc1(n, k) << " " << calc2(n, k) << endl;
}

int main() {
	int re; cin >> re;
	for ( int ri = 1; ri <= re; ++ri ) solve(ri);
}
