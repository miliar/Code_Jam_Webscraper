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

#define PI 3.1415926535897932385
#define INF 1000111222
#define EPS 1e-7
#define N 20
#define MOD 1000000007

const int n = 4;
int ans1, ans2, val;
int r1[N], r2[N];

int solve() {
	int res = INF;
	fr(i, 1, 16)
		if (r1[i] == ans1 && r2[i] == ans2) {
			if (res != INF) return INF + 1;
			res = i;
		}
	return res;
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("test.inp", "r", stdin);
		freopen("test.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		scanf("%d", &ans1);
		fr(i, 1, n) fr(j, 1, n) {
			scanf("%d", &val);
			r1[val] = i;
		}
		scanf("%d", &ans2);
		fr(i, 1, n) fr(j, 1, n) {
			scanf("%d", &val);
			r2[val] = i;
		}
		printf("Case #%d: ", ++caseNo);
		int res = solve();
		if (res == INF)
			puts("Volunteer cheated!");
		else if (res == INF + 1)
			puts("Bad magician!");
		else printf("%d\n", res);
	}
	return 0;
}
