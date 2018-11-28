#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <map>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const ldb INF = 1e9;
const ldb EPS = 1e-9;
const ldb EPS2 = 1e-6;
const int MAXN = 110;

int n;
ll v, x;

ll readldb() {
	int a, b;
	scanf("%d.%d", &a, &b);
	return a * 10000ll + b;
}

struct source {
	ll r, c;

	bool operator <(const source & s) const {
		return c < s.c;
	}
};

source s[MAXN];

ldb solve() {
	ll curv = 0, curt = 0;
	forn(i, n) {
		curv += s[i].r;
		curt += s[i].c * s[i].r;
	}

	if (curt < x * curv) {
		forn(i, n) {
			curt -= s[i].c * s[i].r;
			curv -= s[i].r;

			if (curt < x * curv)
				continue;


			assert(curv > 0);

			ldb a = (x - curt * 1.0L / curv) / (s[i].c - x) * curv;
			return a + curv;
		}
	}

	if (curt > x * curv) {
		forba(i, n, 0) {
			curt -= s[i].c * s[i].r;
			curv -= s[i].r;
			
			if (curt > x * curv)
				continue;

			assert(curv > 0);

			ldb a = (x - curt * 1.0L / curv) / (s[i].c - x) * curv;
			return a + curv;
		}
	}

	return curv;
}

bool old_solve(ldb & ans) {
	bool good = true;
	ans = 0.0L;

	if (n == 2 && s[1].c == s[0].c) {
		n = 1;
		s[0].r += s[1].r;
	}

	if (n == 1) {
		if (s[0].c != x) {
			good = false;
		} else
			ans = v * 1.0L / s[0].r;
	} else if (n == 2) {
		if (s[0].c > s[1].c) {
			swap(s[0].c, s[1].c);
			swap(s[0].r, s[1].r);
		}
		if (x < s[0].c || s[1].c < x) {
			good = false;
		} else {
			ldb a = (x - s[0].c) * 1.0L / (s[1].c - s[0].c) * v;
			ans = max(a / s[1].r, (v - a) / s[0].r);
		}
	}

	return good;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d ", &T);

	forn(test, T) {
		printf("Case #%d: ", test + 1);

		scanf("%d", &n);
		v = readldb();
		x = readldb();

		forn(i, n) {
			s[i].r = readldb();
			s[i].c = readldb();
		}
		sort(s, s + n);

		//ldb old_ans;

		if (!(x >= s[0].c && x <= s[n - 1].c)) {
			//assert(!old_solve(old_ans));

			printf("IMPOSSIBLE\n");
			continue;
		}

		ldb L = v / solve();

		/*assert(old_solve(old_ans));
		if (abs(old_ans - L) > 1e-9)
			fprintf(stderr, "%d: %.10lf %.10lf\n", test + 1, double(L), double(old_ans));*/

		printf("%.10lf\n", double(L));

	}
	return 0;
}
