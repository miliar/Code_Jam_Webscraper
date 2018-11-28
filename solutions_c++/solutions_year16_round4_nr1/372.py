#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <cstdlib>
#include <memory>
#include <queue>
#include <cassert>
#include <cmath>
#include <ctime>
#include <complex>
#include <bitset>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <numeric>

using namespace std;

#define pb push_back
#define fst first
#define snd second
#define mp make_pair 
#define sz(C) ((int) (C).size())
#define forn(i, n) for (int i = 0; i < (int) n; ++i)
#define ford(i, n) for (int i = ((int) n) - 1; i >= 0; --i)
#define y1 gftxdtrtfhyjfctrxujkvbhyjice
#define y0 ehfoiuvhefroerferjhfjkehfjke
#define left sdhfsjkshdjkfsdfgkqqweqweh
#define right yytrwtretywretwreytwreytwr
#define next jskdfksdhfjkdsjksdjkgf
#define prev koeuigrihjdkjdfj
#define hash kjfdkljkdhgjdkfhgurehg
#define all(C) begin(C), end(C)

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int,int> pii;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vector <int> > vvi;
typedef vector<pii> vii;
typedef long double ld;
typedef complex<double> cd;
typedef vector<cd> vcd;

#define FILE_NAME "a"


const int MAXN = 1e5 + 10;
const string NO = "IMPOSSIBLE";

int n;
int r, p, s;

int who(char c1, char c2) {
	if  (c1 == c2) {
		return 0;
	}
	
	if  (c1 == 'r' && c2 == 's') {
		return 1;
	}
	if  (c1 == 's' && c2 == 'r') {
		return -1;
	}

	if  (c1 == 's' && c2 == 'p') {
		return 1;
	}
	if  (c1 == 'p' && c2 == 's') {
		return -1;
	}

	if  (c1 == 'p' && c2 == 'r') {
		return 1;
	}
	if  (c1 == 'r' && c2 == 'p') {
		return -1;
	}

	assert(false);
	return 0;
}

bool read() {
	if  (scanf("%d", &n) < 1) {
		return false;
	}
	scanf("%d%d%d", &r, &p, &s);
	return true;
}

string ans;
string cur;

bool ok(const string& order) {
	assert(sz(order) == (1 << n));
	vi ids(1 << n);
	iota(all(ids), 0);
	while (sz(ids) > 1) {
		vi nids;
		for (int i = 0; i < sz(ids); i += 2) {
			int w = who(order[ids[i]], order[ids[i + 1]]);
			if  (w == 0) {
				return false;
			}
			if  (w == 1) {
				nids.pb(ids[i]);
			} else {
				nids.pb(ids[i + 1]);
			}
		}
		ids.swap(nids);
	}
	return true;
}

void rec(int i, int r, int p, int s) {
	if  (i == (1 << n)) {
		if  (ok(cur)) {
			if  (ans.empty()) ans = cur;
			ans = min(ans, cur);
		}
		return;
	}

	if  (r > 0) {
		cur.pb('r');
		rec(i + 1, r - 1, p, s);
		cur.pop_back();
	}

	if  (p > 0) {
		cur.pb('p');
		rec(i + 1, r, p - 1, s);
		cur.pop_back();
	}

	if  (s > 0) {
		cur.pb('s');
		rec(i + 1, r, p, s - 1);
		cur.pop_back();
	}
}

string solve() {
	ans.clear();
	cur.clear();
	rec(0, r, p, s);
	if  (ans.empty()) return NO;
	for (auto & c : ans) c = toupper(c);
	return ans;
}

string gen(char c, int depth) {
	if  (depth == 0) {
		return string(1, c);
	}

	string S = "rps";
	for (char c2 : S) {
		if  (who(c, c2) == 1) {
			string L = gen(c, depth - 1);
			string R = gen(c2, depth - 1);
			return min(L + R, R + L);
		}
	}

	assert(false);
	return "";
}

string norm(string S) {
	vi cnt(300, 0);
	for (char c : S) {
		++cnt[c - 'a'];
	}
	if  (cnt['r' - 'a'] != r || cnt['s' - 'a'] != s || cnt['p' - 'a'] != p) {
		return string(sz(S), 'z');
	}
	return S;
}

string smart_solve() {
	string R = gen('r', n);
	string P = gen('p', n);
	string S = gen('s', n);
	R = norm(R);
	P = norm(P);
	S = norm(S);
	auto ans = min(R, min(P, S));
	if  (ans[0] == 'z') return NO;
	for (auto& c : ans) c = toupper(c);
	return ans;
}

int main() {
#ifdef LOCAL
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
#endif


	int T;
	scanf("%d\n", &T);
	forn(t, T) {
		assert(read());
		// cout << solve() << endl;
		// cout << smart_solve() << endl;
		// assert(solve() == smart_solve());
		printf("Case #%d: %s\n", t + 1, smart_solve().c_str());
		cerr << t << endl;
	}

#ifdef LOCAL
	// printf("%.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
	return 0;
}
