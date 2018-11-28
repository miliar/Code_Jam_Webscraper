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
#define MAX 5005
#define MOD 1000000007

int n, R, P, S;
int r, p, s, ans[MAX], res[MAX];

void compare() {
	rep(i, n) if (ans[i] < 0) return;
	bool ok = false;
	rep(i, n) {
		if (ans[i] == res[i]) continue;
		if (ans[i] < res[i]) {
			ok = true;
			break;
		} else {
			break;
		}
	}
	if (!ok) return;
	rep(i, n) res[i] = ans[i];
}

void play(int lo, int hi, int move) {
	//printf("%d %d: %d\n", lo, hi, move);
	if (lo == hi) {
		ans[lo] = move;
		return;
	}
	int mid = (lo + hi) / 2;
	if (move == 1) {
		play(lo, mid, 1);
		if (r <= 0) return;
		r--;
		play(mid + 1, hi, 2);
	} else if (move == 2) {
		play(lo, mid, 2);
		if (s <= 0) return;
		s--;
		play(mid + 1, hi, 3);
	} else if (move == 3) {
		if (p <= 0) return;
		p--;
		play(lo, mid, 1);
		play(mid + 1, hi, 3);
	}
}

bool cmp(int a, int b, int c, int d) {
	if (b - a != d - c) {
		puts("FAILED");
		return true;
	}
	for (int i = a, j = c; i <= b; i++, j++) {
		if (res[i] == res[j]) continue;
		if (res[i] > res[j]) return false;
		return true; // less
	}
	return false;
}

void sortRes(int lo, int hi) {
	if (lo == hi) return;
	int mid = (lo + hi) / 2;
	sortRes(lo, mid);
	sortRes(mid + 1, hi);
	if (cmp(mid + 1, hi, lo, mid)) {
		for (int i = lo, j = mid + 1; i <= mid; i++, j++) {
			swap(res[i], res[j]);
		}
	}
}

void solve() {
	fill(res, 100);
	for (int i = 1; i <= 3; i++) {
		r = R;
		p = P;
		s = S;
		fill(ans, -1);
		if (i == 1) {
			if (p == 0) continue;
			p--;
		} else if (i == 2) {
			if (r == 0) continue;
			r--;
		} else if (i == 3) {
			if (s == 0) continue;
			s--;
		}
		play(0, n - 1, i);
		compare();
	}
	bool ok = true;
	rep(i, n) if (!(1 <= res[i] && res[i] <= 3)) {
		ok = false;
		break;
	}
	if (!ok) {
		puts("IMPOSSIBLE");
	} else {
		sortRes(0, n - 1);
		rep(i, n) {
			if (res[i] == 1) putchar('P');
			else if (res[i] == 2) putchar('R');
			else if (res[i] == 3) putchar('S');
		}
		puts("");
	}
}

int main() {
	//ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("abig.inp", "r", stdin);
		freopen("abig.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		scanf("%d %d %d %d", &n, &R, &P, &S);
		n = 1 << n;
		printf("Case #%d: ", ++caseNo);
		solve();
	}
	return 0;
}
