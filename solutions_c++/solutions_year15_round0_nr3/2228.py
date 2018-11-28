#pragma comment(linker, "/stack:32000000")
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <cassert>
#include <string.h>
#include <ctime>

#define pb push_back
#define mp make_pair
#define PI 3.1415926535897932384626433832795
#define sqr(x) (x)*(x)
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define sz(x) int((x).size())
#define X first
#define Y second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;

int matr[5][5] = {
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}
};

int ABS(int x) {
	return x*((x>0)-(x<0));
}

int sgn(int x) {
	return (x>0)-(x<0);
}

struct num {
	int x;
	num(int x):x(x) {}
	num operator*(const num& o) const {
		num res(matr[ABS(x)][ABS(o.x)]);
		res.x *= sgn(x) * sgn(o.x);
		return res;
	}
	num pw(ll n) const {
		num res(1);
		num t = *this;
		while (n) {
			if (n&1) res = res * t;
			t = t * t;
			n >>= 1;
		}
		return res;
	}
};

inline num getq(char c) {
	return num(2 + c - 'i');
}


void solve() {
	int len;
	ll x; cin >> len >> x;
	string s; cin >> s;
	num total(1);
	forn(i, sz(s)) total = total * getq(s[i]);
	total = total.pw(x);
	if (total.x != -1) {printf("NO\n"); return;}
	string r;
	forn(iter, 10) r = r + s;

	const int cinf = 1000000010;
	int lind = cinf;
	int rind = cinf;
	num cur(1);
	forn(i, sz(r)) {
		cur = cur * getq(r[i]);
		if (cur.x == 2) { lind = i; break; }
	}
	reverse(ALL(r));
	cur = 1;
	forn(i, sz(r)) {
		cur = getq(r[i]) * cur;
		if (cur.x == 4) { rind = i; break; }
	}
	if (lind == cinf || rind == cinf) {printf("NO\n"); return;}
	ll lpos = lind;
	ll rpos = x * len - 1 - rind;
	if (lpos < rpos) printf("YES\n");
	else printf("NO\n");

}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; scanf("%d", &T);
	for (int tn = 1; tn <= T; ++tn) {
		cerr << tn << endl;
		printf("Case #%d: ", tn);
		solve();
	}
	return 0;
}
