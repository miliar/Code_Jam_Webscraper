//============================================================================
// Author	   : LAM PHAN VIET - lamphanviet@gmail.com
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
#include <deque>
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

#define PI	3.1415926535897932385
#define EPS	1e-7
#define MOD	1000000007
#define INF	1000111222
#define MAX	10

int n, m, group[MAX];
string s[MAX];
int best, counter;
bool ok[MAX];

int calGroup(int p) {
	set<string> v;
	fr(i, 1, m) {
		if (group[i] != p) continue;
		fr(j, 1, s[i].size())
			v.insert(s[i].substr(0, j));
	}
	return v.size() + 1;
}

void compute() {
	fill(ok, false);
	fr(i, 1, m) ok[group[i]] = true;
	fr(i, 1, n) if (!ok[i]) return;
	int total = 0;
	fr(i, 1, n) total += calGroup(i);
	if (total == best) counter++;
	else if (total > best) {
		best = total;
		counter = 1;
	}
}

void recursive(int pos) {
	if (pos > m) {
		compute();
		return;
	}
	fr(i, 1, n) {
		group[pos] = i;
		recursive(pos + 1);
	}
}

void solve() {
	best = -1; counter = 0;
	recursive(1);
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("test.inp", "r", stdin);
		freopen("test.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		scanf("%d %d", &m, &n);
		fr(i, 1, m) cin >> s[i];
		solve();
		printf("Case #%d: %d %d\n", ++caseNo, best, counter % MOD);
	}
	return 0;
}
