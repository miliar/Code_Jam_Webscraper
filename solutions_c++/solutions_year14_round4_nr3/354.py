#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

#define N 100500
#define M 2000009
#define inf 2000000000
#define INT int
struct E {
	int t, next;
	INT flow, cap;
} edge[M];
int node[N], eid;
vector<int> e[N];
int rr[N];
int que[N];
void init() {
	eid = 0;
	memset(rr, -1, sizeof(rr));
	memset(node, -1, sizeof(node));
}
void addedge(int a, int b, INT c) {
	edge[eid].t = b;
	edge[eid].cap = c;
	edge[eid].flow = 0;
	edge[eid].next = node[a];
	node[a] = eid++;

	edge[eid].t = a;
	edge[eid].cap = 0; //0单向，c双向
	edge[eid].flow = 0;
	edge[eid].next = node[b];
	node[b] = eid++;
}
void addedge1(int a, int b, INT c) {
	edge[eid].t = b;
	edge[eid].cap = c;
	edge[eid].flow = 0;
	edge[eid].next = node[a];
	node[a] = eid++;

	edge[eid].t = a;
	edge[eid].cap = c; //0单向，c双向
	edge[eid].flow = 0;
	edge[eid].next = node[b];
	node[b] = eid++;
}
int bfs(int s, int t, int n) {
	memset(rr, -1, sizeof(rr));
	int i;
	for (i = 0; i < n; ++i)
		e[i].clear();
	int u, v;
	int front = 0, rear = 1;
	rr[s] = 0;
	que[0] = s;
	while (rear > front) {
		u = que[front++];
		for (i = node[u]; i != -1; i = edge[i].next) {
			v = edge[i].t;
			if (rr[v] == -1 && edge[i].cap) {
				que[rear++] = v;
				rr[v] = rr[u] + 1;
			}
			if (rr[v] == rr[u] + 1)
				e[u].push_back(i);
		}
	}
	return (rr[t] != -1);
}
INT dinic(int s, int t, int n) {
	int st[N];
	INT maxflow = 0;
	int aux[N];
	int top, cur;
	int p, i, k;
	while (bfs(s, t, n)) {
		top = 0;
		st[top] = s;
		cur = s;
		while (1) {
			if (cur == t) {
				INT minc = inf;
				for (i = 0; i < top; ++i) {
					p = aux[i + 1];
					if (minc > edge[p].cap)
						minc = edge[p].cap, k = i;
				}
				for (i = 0; i < top; ++i) {
					p = aux[i + 1];
					edge[p].cap -= minc;
					edge[p ^ 1].cap += minc;
				}
				maxflow += minc;
				cur = st[top = k];
			}
			int len = e[cur].size();
			while (len) {
				p = e[cur][len - 1];
				if (edge[p].cap && rr[edge[p].t] == rr[cur] + 1)
					break;
				else {
					len--;
					e[cur].pop_back();
				}
			}
			if (len) {
				cur = st[++top] = edge[p].t;
				aux[top] = p;
			} else {
				if (top == 0)
					break;
				rr[cur] = -1;
				cur = st[--top];
			}
		}
	}
	return maxflow;
}

int a[105][1005];
int x1[121], yy1[121], x2[211], y2[121];
int main() {
	int i, j, k;
	int n, m, p;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d%d", &n, &m, &p);
		memset(a, 0, sizeof(a));
		for (i = 0; i < p; ++i) {
			scanf("%d%d%d%d", &x1[i], &yy1[i], &x2[i], &y2[i]);
		}
		init();
		int S, T;
		S = 2 * n * m;
		T = S + 1;
		int dir[4][2] = { 0, 1, 1, 0, 0, -1, -1, 0 };
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				for (k = 0; k < p; ++k) {
					if (i >= x1[k] && i <= x2[k] && j >= yy1[k] && j <= y2[k])
						break;
				}
				if (k < p)
					continue;
				addedge(i * m + j, n * m + i * m + j, 1);

				if (j == 0)
					addedge(S, i * m + j, 1);
				if (j == m - 1)
					addedge(n * m + i * m + j, T, 1);
				for (k = 0; k < 4; ++k) {
					int ii, jj;
					ii = i + dir[k][0];
					jj = j + dir[k][1];
					if (ii < 0 || jj < 0 || ii >= n || jj >= m)
						continue;
					addedge(n * m + i * m + j, ii * m + jj, 1);
				}
			}
		}
		printf("Case #%d: %d\n", cas, dinic(S, T, T + 1));
	}
}
