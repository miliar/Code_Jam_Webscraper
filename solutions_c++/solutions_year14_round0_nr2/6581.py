#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <utility>
#include <sstream>
#include <numeric>

#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <cmath>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define dbgv(v) do{cerr<<#v<<':';for(auto x:v) cerr << x << ','; cerr << '\n';}while(0)
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define ford1(i, n) for(int i = (int)(n); i>=1; --i)
#define fored(i, a, b) for(int i = (int)(b); i >= (int)(a); --i)
#define sz(v) ((int)((v).size()))
#define all(v) (v).begin(), (v).end()
#define clr(v) memset(v, 0, sizeof(v))
#define clr1(v) memset(v, 0xFF, sizeof(v))
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define op operator

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
void solve() {
	ld C,F,X;cin>>C>>F>>X;
	ld F0 = 2;
	ld ans = X/F0;
	int rcnt = 0;
	if( C < X ) {
		ld ct = 0;
		int cnt = 0;
		while( ct < ans ) {
			++cnt;
			ct += C/F0;
			F0 += F;
			if( ans > ct + X/F0 ) { rcnt = cnt; }
			ans = min(ans,ct + X/F0);
		}
	}
	cerr << rcnt << '\n';
	cout << ans << '\n';
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;cin >> T;
	cout << fixed;cout.precision(7);
	forn(t, T) {
		cout << ("Case #") << t+1 << ": ";
		solve();
	}
	return 0;
}
