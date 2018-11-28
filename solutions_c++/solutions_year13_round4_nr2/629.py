#define _CRT_SECURE_NO_WARNINGS
#include <numeric>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <sstream> 
#include <stack>

#pragma comment(linker, "/STACK:256000000")
using namespace std;
typedef long long ll;
template<typename T> int size(T &a) {return (int)a.size();}
template<typename T> T sqr(T a)  { return a * a; }

#define fi first
#define se second
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,a,b) for(int i=(a);i<(b); ++i)
#define REPD(i,a,b)for(int i=(b)-1;i>=a;--i)
#define _(a,b) memset((a), (b), sizeof(a))
#define all(a) a.begin(), a.end()
#define mp make_pair
#define pb push_back
#define ve vector

struct seg {
	ll a, b;
	seg() {}
	seg(ll a, ll b) : a(a), b(b) {}
};

ve<int> stupid(ve<int> ord, int n){
	ve<int> res(1 << n);
	ve<ve<int> > b;
	b.pb(ord);
	REP(rnd, 0, n) {
		REP(iter,0,size(b)) {
			assert(size(b[iter]) % 2 == 0);
			REP(v, 0, size(b[iter])) {
				int A = b[iter][v];
				int B = b[iter][v+1];
				if(A<B) {
					res[A] ^= (1 << (n-rnd-1));
				} else {
					res[B] ^= (1 << (n-rnd-1));
				}
				++v;
			}
		}
		ve<pair<int, int> > g;
		REP(i, 0, 1 << n)
			g.pb(mp(res[i], i));
		sort(all(g));
		b.clear();
		for(int i = 0, j = 0; i < size(g); i = j) {
			for(j = i; j < size(g) && g[i].first == g[j].first; ++j) ;
			ve<int> tmp;
			for(int u = i; u < j; ++u) {
				tmp.pb(g[u].second);
			}
			b.pb(tmp);
		}
	}
	return res;
}
int bestPlace(int n, int x) {
	ve<int> ord(1<<n);
	int p = 0;
	ord[p++]=x;
	if (x == (1<<n) - 1) {
		for(int i = (1<<n) - 2; i >= 0; --i)
			ord[p++] = i;
	} else {
		ord[p++]=x+1;
		if (x+2 <= (1<<n) - 1) {
			for(int i = (1<<n)-1; i >= x+2; --i)
				ord[p++] = i;
		}
		if (x-1 >= 0) {
			for(int i = x-1; i >= 0; --i)
				ord[p++] = i;
		}
	}
	ve<int> res = stupid(ord, n);
	return (1<<n)-res[x]-1;
}
int solve1(int n, int p) {
	int l = 0, r = (1 << n)-1, res = 0;
	while (l <= r) {
		int m = (l+r) / 2;
		if (bestPlace(n, m) < p) {
			res = max(res, m);
			l = m + 1;
		} else {
			r = m - 1;
		}
	}
	return res;
}
int worstPlace(int n, int x) {
	ve<int> ord(1<<n);
	int p = 0;
	ord[p++]=x;
	if (x == 0) {
		for(int i = 1; i < (1<<n); ++i)
			ord[p++] = i;
	} else {
		ord[p++]=x-1;
		if (x-2 >= 0)
			for(int i = 0; i <= x-2; ++i)
				ord[p++] = i;
		if (x+1 <= (1<<n) - 1) {
			for(int i = x+1; i <= (1<<n)-1; ++i)
				ord[p++] = i;
		}
	}
	ve<int> res = stupid(ord, n);
	return (1<<n)-res[x]-1;
}
int solve2(int n, int p) {
	int l = 0, r = (1 << n)-1, res = r+1;
	while (l <= r) {
		int m = (l+r) / 2;
		if (worstPlace(n, m) >= p) {
			res = min(res, m);
			r = m - 1;
		} else {
			l = m + 1;
		}
	}
	return res-1;
}
void solve() {
	int n;
	cin >> n;
	int p;
	cin >> p;

	int r1 = solve1(n, p);
	int r2 = solve2(n, p);
	cout << r2 << " " << r1 << endl;
}

int main() {
#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin>>test;
	REP(it, 0, test) {
		printf("Case #%d: ", it+1);
		solve();
	}


	return 0;
}           