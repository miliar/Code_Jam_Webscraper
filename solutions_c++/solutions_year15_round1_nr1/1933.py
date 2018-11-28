#define NDEBUG
#include <iostream>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <vector>
#include <cassert>
#include <climits>
#define INT    stoi
#define LLONG  stoll
#define UINT   stoui
#define ULLONG stoull
#define DOUBLE stod
#define mp make_pair
#define pb push_back
#define all(v) begin(v), end(v)
#define sz(v) distance(all(v))
#define FOR(i, n) for (int i = 0; i < (int)n; ++i)
#define FIN(x, xs) for (auto & x: xs)
int _case_nb = 1;
#define out printf((_case_nb>1)?"\nCase #%d: ":"Case #%d: ",_case_nb);_case_nb++;printf
char _tmp[100];
#ifndef NDEBUG
#define debug(x) cerr<<"DEBUG (l. "<<__LINE__<<"): "<<#x<<" = "<<x<<endl
#else
#define debug(x)
#endif
#define read(i, fn) scanf(" %s", _tmp); i = fn(_tmp);
#define readarray(v, fn) FIN(x, v){read(x, fn);}

using namespace std;
typedef unsigned long long int LL;

void run() {
	int N; read(N, INT);
	vector<int> a(N); readarray(a, INT);
	vector<int> diffs(N-1);
	FOR(i, N-1) diffs[i] = a[i+1]-a[i];

	// nb 1
	int ans1 = 0;
	FIN(x, diffs) if (x < 0) ans1-=x;

	// nb2
	int min = *min_element(all(diffs));
	if (min > 0) min = 0;
	else min *= -1;
	int ans2 = 0, curr = 0;
	FOR(i, N-1) {
		curr = a[i];
		int old_curr = curr;
		curr -= min;
		if (curr < 0) curr = 0;
		debug(old_curr-curr);
		ans2 += old_curr-curr;
	}
	out("%d %d", ans1, ans2);
}

int main() {
	freopen("in", "r", stdin); freopen("out", "w", stdout);
	int T;
	read(T, INT);
	FOR(t, T) {
		run();
	}
}
