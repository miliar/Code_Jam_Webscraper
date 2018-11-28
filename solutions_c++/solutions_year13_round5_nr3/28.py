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
#include <windows.h>

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

const int max_n = 20, max_e = 20;

struct Edge {
	int f, t;
	int a, b;
	void scan() {
		scanf("%d %d %d %d", &f, &t, &a, &b);
		f--, t--;
	}
	int w;
} edges[max_e];

int d[max_n];
int c[1 << 20][max_n];
int v[max_n];

int n, m;

void solve(int index) {
	memset(d, 127, sizeof(d));
	d[1] = 0;
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < m; j++) {
			Edge &e = edges[j];
			if (d[e.t] + e.w < d[e.f]) {
				d[e.f] = d[e.t] + e.w;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		c[index][i] = d[i];
	}
}

int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int iTest = 1; iTest <= T; iTest++) {
		int u;
		scanf("%d %d %d", &n, &m, &u);
		for (int i = 0; i < m; i++) {
			edges[i].scan();
		}
		for (int i = 0; i < (1 << m); i++) {
			for (int j = 0; j < m; j++) {
				if (i & (1 << j)) {
					edges[j].w = edges[j].a;
				} else {
					edges[j].w = edges[j].b;
				}
			}
			solve(i);
		}
		for (int i = 0; i < u; i++) {
			scanf("%d", &v[i]);
			v[i]--;
		}
		int d = 0, r = -1, mask = 0;
		for (int i = 0; i < u; i++) {
			Edge &e = edges[v[i]];
			d += e.a;
			mask |= 1 << v[i];
			bool g = false;
			for (int j = mask; j < (1 << m); j = ((j + 1) | mask)) {
				int d1 = c[j][e.t];
				int d0 = c[j][0];
				if (d0 == d1 + d) {
					g = true;
					break;
				}
			}
			if (!g) {
				r = v[i] + 1;
				break;
			}
		}
		if (r == -1) {
			printf("Case #%d: Looks Good To Me\n", iTest);
			continue;
		}
		printf("Case #%d: %d\n", iTest, r);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}