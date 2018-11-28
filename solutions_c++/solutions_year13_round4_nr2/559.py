//============================================================================
// Author       : LAM PHAN VIET - lamphanviet@gmail.com
// Problem Name : 
// Time Limit   : .000s
// Description  : 
//============================================================================
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1LL<<(n))
#define sqr(x) ((x) * (x))

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define eps 1e-7
#define maxN 100111

int64 n, pos, m;

int64 get(int64 a) {
	a++;
	int64 res = 0;
	while (a > 1) {
		res++;
		a /= 2;
	}
	return res;
}

int64 cal1(int64 a) {
	int64 res = 0;
	repr(i, n) {
		if (a) {
			res += BIT(i);
			a--;
		}
	}
	return res;
}

int64 cal0(int64 a) {
	int64 res = 0;
	repr(i, n) {
		if (a == 0) res += BIT(i);
		else a--;
	}
	return res;
}

int64 getLow() {
	int64 lo = 0, hi = m - 1, res = 0;
	while (lo <= hi) {
		int64 mid = (lo + hi) / 2;
		int64 val = get(mid);
		val = cal1(val);
		if (val < pos) {
			res = mid;
			lo = mid + 1;
		}
		else hi = mid - 1;
	}
	return res;
}

int64 getHigh() {
	int64 lo = 0, hi = m - 1, res = 0;
	while (lo <= hi) {
		int64 mid = (lo + hi) / 2;
		int64 val = get(m - mid - 1);
		val = cal0(val);
		if (val < pos) {
			res = mid;
			lo = mid + 1;
		}
		else hi = mid - 1;
	}
	return res;
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("Blarge.inp", "r", stdin);
		freopen("Blarge.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		cin >> n >> pos;
		m = BIT(n);
		/*int resA = 0, resB = 0;
		rep(i, m) {
			int a = get(i), b = get(m - i - 1);
			//printf("%d: %d %d => %d %d\n", i, a, b, cal1(a), cal0(b));
			a = cal1(a);
			b = cal0(b);
			if (a < pos) resA = i;
			if (b < pos) resB = i;
		}*/
		printf("Case #%d: ", ++caseNo);
		cout << getLow() << " " << getHigh() << endl;
	}
	return 0;
}
