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
#define maxN 11

int R, N, M, K, p[maxN];
vector<vi> sta;
vector<set<int> > stp;
vi tmpGroup;
set<int> tmpSet;

void gen(int i) {
	if (i == N) {
		sta.pb(tmpGroup);
		return;
	}
	fr(v, 2, M) {
		tmpGroup.pb(v);
		gen(i + 1);
		tmpGroup.pop_back();
	}
}

void genSet(int pos, int i, int val) {
	if (i == N) {
		tmpSet.insert(val);
		return;
	}
	genSet(pos, i + 1, val);
	genSet(pos, i + 1, val * sta[pos][i]);
}

void init() {
	gen(0);
	rep(i, sta.size()) {
		tmpSet.clear();
		genSet(i, 0, 1);
		stp.pb(tmpSet);
	}
	/*rep(i, sta.size()) {
		rep(j, sta[i].size()) printf("%d", sta[i][j]);
		printf(": ");
		foreach(it, stp[i]) printf(" %d", *it);
		puts("");
	}*/
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("Csmall.inp", "r", stdin);
		freopen("Csmall.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		printf("Case #%d:\n", ++caseNo);
		scanf("%d %d %d %d", &R, &N, &M, &K);
		init();
		rep(_, R) {
			rep(j, K) scanf("%d", &p[j]);
			bool solved = false;
			rep(i, sta.size()) {
				bool ok = true;
				rep(j, K) if (stp[i].find(p[j]) == stp[i].end()) {
					ok = false;
					break;
				}
				if (ok) {
					solved = true;
					rep(j, N) printf("%d", sta[i][j]);
					puts("");
					break;
				}
			}
			if (!solved) {
				rep(i, N) putchar('2');
				puts("");
			}
		}
	}
	return 0;
}
