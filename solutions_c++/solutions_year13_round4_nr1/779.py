#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#pragma comment(linker, "/STACK:36777216")

#define INF (2000000000)

const long long mod = 1000002013;

struct S
{
	int s, e, p;
	void read() {
		scanf("%d%d%d", &s, &e, &p);
	}
};

struct E
{
	int e;
	int x;
	int p;
	E(int e = 0, int x = 0, int p = 0): e(e), x(x), p(p) {}
	bool operator<(const E& other) const {
		if (x != other.x) {
			return x < other.x;
		}
		return e > other.e;
	}
};

int N;

long long f(int i, int j) {
	int count = j - i;
	return ((2LL * N - (count - 1)) * count / 2) % mod;
}

const int nmax = 1 << 10;

S a[nmax];
E e[nmax * 2];
int n;

void readTest() {
	scanf("%d%d", &N, &n);
	for(int i = 0; i < n; ++i) {
		a[i].read();
	}
}

stack<E> q;

void solveTest() {

	long long I = 0;
	for(int i = 0; i < n; ++i) {
		I += (f(a[i].s, a[i].e) * a[i].p) % mod;
		I %= mod;
	}

	int cnt = 0;

	for(int i = 0; i < n; ++i) {
		e[cnt++] = E(1, a[i].s, a[i].p);
		e[cnt++] = E(-1, a[i].e, a[i].p);
	}

	sort(e, e + cnt);

	long long S = 0;

	for(int i = 0; i < cnt; ++i) {
		if (e[i].e > 0) {
			q.push(e[i]);
		} else {

			int t = e[i].p;
			while(t) {
				E& et = q.top();
				int source = et.x;
				int quantity = min(et.p, t);
				et.p -= quantity;
				t -= quantity;
				if (et.p == 0) {
					q.pop();
				}
				S += quantity * f(source, e[i].x) % mod;
				S %= mod;
			}

		}
	}

	printf("%lld\n", ((I - S) + mod) % mod);

}

int main()
{
	freopen("A.in", "rt", stdin);

	bool submit = true;

	if (submit) {
		freopen("A.out", "wt", stdout);
	}

	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt) {
		readTest();
		printf("Case #%d: ", tt + 1);
		solveTest();
		if (submit) {
			cerr << "Case " << tt + 1 << " done\n";
		}
	}
	return 0;
}