#pragma comment(linker, "/STACK:512777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
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

typedef vector<int> VI;

template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T abs(const T &a) {
	return (a < 0 ? -a : a);
}
template<class T> T sqr(const T &a) {
	return a * a;
}

#define all(a) a.begin(),a.end()

const int max_n = 500, max_v = 500 * 100 * 2 + 2, max_e = max_v * 15;

bool a[max_n][max_n];

int di[4] = { -1, 0, 0, 1 };
int dj[4] = { 0, 1, -1, 0 };

struct Edge {
	Edge* p;
	int f;
	int v;
	int u;
	Edge* next;
	void add(int v, int u, Edge* p, Edge* &head) {
		this->v = v;
		this->f = 0;
		this->u = u;
		this->p = p;
		this->next = head;
		head = this;
	}
} edges[max_e], *cedge;
Edge* h[max_v];

void addEdge(int v1, int v2) {
	(cedge + 0)->add(v2, 1, cedge + 1, h[v1]);
	(cedge + 1)->add(v1, 0, cedge + 0, h[v2]);
	cedge += 2;
}

bool was[max_v];

int t;

bool dfs(int i) {
	if (i == t) {
		return true;
	}
	was[i] = true;
	for (Edge* e = h[i]; e; e = e->next) {
		if (e->f < e->u && !was[e->v] && dfs(e->v)) {
			e->f++;
			e->p->f--;
			return true;
		}
	}
	return false;
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
		int n, m, k;
		scanf("%d %d %d", &n, &m, &k);
		memset(a, true, sizeof(a));
		for (int i = 0; i < k; i++) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; x++) {
				for (int y = y1; y <= y2; y++) {
					a[x][y] = false;
				}
			}
		}
		memset(h, 0, sizeof(h));
		cedge = edges;
		int s = n * m * 2;
		t = s + 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (!a[i][j]) continue;
				int v0 = (i * m + j) * 2;
				addEdge(v0, v0 + 1);
				if (j == 0) {
					addEdge(s, v0);
				}
				if (j == m - 1) {
					addEdge(v0 + 1, t);
				}
				for (int dir = 0; dir < 4; dir++) {
					int r = i + di[dir], c = j + dj[dir];
					if (r >= 0 && c >= 0 && r < n && c < m && a[r][c]) {
						addEdge(v0 + 1, (r * m + c) * 2);
					}
				}
			}
		}
		int res = 0;
		while (true) {
			memset(was, 0, sizeof(was));
			if (!dfs(s)) {
				break;
			}
			res++;
		}
		printf("Case #%d: %d\n", iTest, res);
	}
#ifdef pperm
	fprintf(stderr, "\n%.3lf\n", clock() / double(CLOCKS_PER_SEC));
#endif
	return 0;
}