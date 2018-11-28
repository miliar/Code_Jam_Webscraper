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

void solve() {
const int N = 4;
	int x[2];
	int a[2][N][N];
	forn(i, 2) {
		scanf("%d", &x[i]);--x[i];
		forn(p,N) forn(q,N) scanf("%d",&a[i][p][q]);
	}
	vi r(N*2);
	sort(a[0][x[0]], a[0][x[0]] + N);
	sort(a[1][x[1]], a[1][x[1]] + N);
	auto it = set_intersection( a[0][x[0]], a[0][x[0]] + N, a[1][x[1]], a[1][x[1]] + N, r.begin());
	if( it == r.begin() ) {
		puts("Volunteer cheated!");
	} else if( it != r.begin() + 1 ) {
		puts("Bad magician!");
	} else {
		printf("%d\n", *r.begin());
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	forn(t, T) {
		printf("Case #%d: ", t+1);
		solve();
	}
	return 0;
}
