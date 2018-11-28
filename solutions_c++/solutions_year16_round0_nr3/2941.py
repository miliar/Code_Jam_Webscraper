#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define pb push_back
#define mp make_pair
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()

typedef pair<int,int> pt;
#define x first
#define y second

typedef long long li;
typedef long double ld;

using namespace std;

bool solve(int);

int main() {
#ifdef SU1
	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
#endif

	int test = 0;
	while (solve(test++));
	
	return 0;
}

vector <int> v;

li find_div(li v) {
	for (li i = 2; i < v && i < 10000; ++i)
		if (v % i == 0)
			return i;
	return -1;
}

li interpret(int x, int base) {
	li res = 0;
	for (int i = 15; i >= 0; --i) {
		res *= base;
		if (x & (1 << i))
			res++;
	}
	return res;
}

bool solve(int) {
	forn(i, (1 << 16))
		if ((i & (1 << 15)) && (i & 1))
			v.pb(i);
	random_shuffle(all(v));

	puts("Case #1:");
	int out = 0;
	forn(i, sz(v)) {
		if (out == 50)
			break;
		vector <li> divs;
		for (int b = 2; b <= 10; ++b)
			divs.pb(find_div(interpret(v[i], b)));
		bool bad = false;
		for (auto x: divs)
			bad |= (x == -1);
		if (bad)
			continue;
		for (int j = 15; j >= 0; --j)
			printf("%d", (v[i] >> j) & 1);
		for (auto x: divs)
			printf(" %d", x);
		puts("");
		out++;
	}
	return false;
}
