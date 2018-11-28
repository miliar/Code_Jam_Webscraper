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

const int maxm = 1000 * 2 + 5;
const LL module = 1000002013;

struct Item {
	LL i, p;
	bool operator < ( const Item& o ) const {
		return i < o.i;
	}
} item[maxm];


Item make_item(LL i, LL p) {
	Item item;
	item.i = i; item.p = p;
	return item;
}

int cnt;

LL calc(LL n, LL c) {
	LL r = (n+1) * c - c * (c+1) / 2; 
	return r % module;
}

void solve( int ri ) {
	int n, m; cin >> n >> m;
	cnt = 0;
	LL org = 0;
	for ( int i = 0; i < m; ++i ) {
		int a, b, p;
		scanf("%d%d%d", &a, &b, &p );
		item[ cnt++ ] = make_item(a, p);
		item[ cnt++ ] = make_item(b, -p);
		org += calc(n, b - a) * p % module;
	}
	sort( item, item + cnt );
	m = 0;
	for ( int i = 0, j; i < cnt; i = j ) {
		j = i + 1;
		while ( j < cnt && item[i].i == item[j].i ) {
			item[i].p += item[j].p;
			++j;
		}
		item[m++] = item[i];
	}
	for ( int i = 1; i < m; ++i ) {
		item[i].p = item[i-1].p + item[i].p;
	}
	LL ans = 0;
	for (;;) {
		int i = 0;
		for (; i < m; ++i) if ( item[i].p ) break;
		if ( i == m ) break;
		int j = i + 1;
		while ( j < m && item[j].p ) ++j;
		LL MIN = LONG_LONG_MAX; 
		for ( int k = i; k < j; ++k ) {
			MIN = min( item[k].p, MIN );
		}
		ans += MIN % module * calc(n, item[j].i - item[i].i) % module;
		for ( int k = i; k < j; ++k ) {
			item[k].p -= MIN;
		}
	}
	ans = org - ans;
	ans = (ans % module + module) % module;
	printf("Case #%d: %d\n", ri, (int)ans);
}

int main() {
	int re; cin >> re;
	for ( int ri = 1; ri <= re; ++ri ) solve(ri);
}
