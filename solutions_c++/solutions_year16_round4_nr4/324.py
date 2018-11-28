// lamphanviet@gmail.com
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define ull unsigned long long
#define ll long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define EPS 1e-7
#define MAX 20
#define MOD 1000000007

int n, res, a[MAX], b[MAX];
char s[MAX][MAX];
bool chosen[MAX];

bool check2(int cost) {
	rep(i, n) chosen[i] = false;
	rep(i, n) {
		if (s[a[i]][b[i]] == '1' && !chosen[b[i]]) {
			chosen[b[i]] = true;
			continue;
		}
		bool ok = false;
		rep(j, n) if (!chosen[b[j]] && s[a[i]][b[j]] == '1') {
			ok = true;
		}
		if (!ok) {
			return false;
		}
	}
	return true;
}

void check(int cost) {
	rep(i, n) a[i] = i;
	do {
		rep(i, n) b[i] = i;
		do {
			if (!check2(cost))
				return;
		} while (next_permutation(b, b + n));
	} while (next_permutation(a, a + n));
	res = min(res, cost);
}

void go(int i, int j, int cost) {
	if (i == n) {
		check(cost);
		return;
	}
	if (j == n - 1) {
		go(i + 1, 0, cost);
	} else {
		go(i, j + 1, cost);
	}

	// change
	if (s[i][j] == '0') {
		s[i][j] = '1';
		if (j == n - 1) {
			go(i + 1, 0, cost + 1);
		} else {
			go(i, j + 1, cost + 1);
		}
		s[i][j] = '0';
	}
}

int solve() {
	res = INF;
	go(0, 0, 0);
	return res;
}

int main() {
	//ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("dsmall.inp", "r", stdin);
		freopen("dsmall.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		scanf(" %d ", &n);
		rep(i, n) scanf(" %s ", s[i]);
		printf("Case #%d: %d\n", ++caseNo, solve());
	}
	return 0;
}

