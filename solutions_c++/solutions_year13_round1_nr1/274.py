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

#define BIT(n) (1<<(n))
#define sqr(x) ((x) * (x))

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define eps 1e-7
#define maxN 100111

int64 r, t;

bool accepted(int64 n) {	
	if ((t - n) / (2LL * r) < n) return false;
	if (n && t / (2LL * n) < n - 1) return false;
	//if (r * n < 0) puts("shit");
	//if (n * (n - 1) * 2 < 0) puts("shit");
	int64 sum = 2LL * r * n + n + 2LL * (n - 1) * n;
	return sum <= t;
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("A.inp", "r", stdin);
		freopen("A.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		cin >> r >> t;
		int64 lo = 0, hi = t / r, res = 0;
		while (lo <= hi) {
			int64 mid = (lo + hi) / 2;
			if (accepted(mid)) {
				res = mid;
				lo = mid + 1;
			}
			else hi = mid - 1;
		}
		printf("Case #%d: %lld\n", ++caseNo, res);
	}
	return 0;
}
