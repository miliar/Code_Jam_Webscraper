#pragma comment(linker, "/STACK:128777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <functional>
#include <numeric>
#include <sstream>
#include <exception>
#include <cassert>

typedef long long i64;
typedef unsigned int u32;
const int null = 0;

using namespace std;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T abs(const T &a) {
	return (a < 0? -a: a);
}
template<class T> T sqr(const T &a) {
	return a * a;
}

#define all(a) a.begin(),a.end()

struct Jour {
	int s, t;
	int v;
	int id;
	void scan(int id) {
		this->id = id;
		scanf("%d %d %d", &s, &t, &v);
	}
	bool operator < (const Jour &j) const {
		return s < j.s || s == j.s && t < j.t;
	}
} jx;

struct CMPs {
	bool operator()(const Jour &j1, const Jour &j2) const {
		return j1.s < j2.s || j1.s == j2.s && j1.id < j2.id;
	}
};
struct CMPt {
	bool operator()(const Jour &j1, const Jour &j2) const {
		return j1.t < j2.t || j1.t == j2.t && j1.id < j2.id;
	}
};
set<Jour, CMPs> s;
set<Jour, CMPt> t;

const int mod = 1000002013;
int n;
int dist(int f, int t) {
	return ((n + (n - (t - f) + 1LL)) * (t - f + 0LL) / 2) % mod;
}

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	jx.id = 2e9;
	for (int iTest = 1; iTest <= T; iTest++) {
		int m;
		scanf("%d %d", &n, &m);
		int res = 0;
		for (int i = 0; i < m; i++) {
			Jour j;
			j.scan(i);
			s.insert(j);
			t.insert(j);
			res = (res + dist(j.s, j.t) * i64(j.v)) % mod;
		}
		while (t.size()) {
			Jour j = *t.begin();
			t.erase(j);
			jx.s = j.t;
			while (j.v) {
				set<Jour, CMPt>::iterator it = s.lower_bound(jx);
				it--;
				if (it->v <= j.v) {
					res = (res - dist(it->s, j.t) * (0LL + it->v)) % mod;
					j.v -= it->v;
					s.erase(it);
				} else {
					res = (res - dist(it->s, j.t) * (0LL + j.v)) % mod;
					Jour c = *it;
					s.erase(it);
					c.v -= j.v;
					s.insert(c);
					j.v = 0;
				}
			}
		}
		if (res < 0) {
			res += mod;
		}
		printf("Case #%d: %d\n", iTest, res);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}