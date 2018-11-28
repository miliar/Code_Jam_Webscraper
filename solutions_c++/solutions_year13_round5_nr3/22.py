#include <algorithm>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define SIZE(v) ((int)(v).size())

#define BEGIN(v) ((v).begin())
#define END(v) ((v).end())
#define ALL(v) BEGIN(v),END(v)
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) SORT(v);(v).erase(unique(ALL(v)),END(v))

#define FOR(i,l,r) for(int i=(l);i<(r);i++)
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)

const int MAXN = 2048;
const int INF = 1012345678;

int n, m, p;
int u[MAXN], v[MAXN], a[MAXN], b[MAXN];
vector< pair< pair<int, int>, int > > edge[MAXN], redge[MAXN];
bool possible[MAXN];

int dist[MAXN];
bool shortest[MAXN];

void calc() {
	FOR(i, 0, n) {
		dist[i] = INF;
		shortest[i] = false;
	}
	dist[0] = 0;
	priority_queue< pair<int, int>, vector< pair<int, int> >, greater< pair<int, int> > > heap;
	for (heap.push(make_pair(0, 0)); !heap.empty(); ) {
		int value = heap.top().first, idx = heap.top().second;
		heap.pop();
		if (dist[idx] != value) continue;
		FOREACH(it, edge[idx]) if (dist[it->first.first] > dist[idx] + it->first.second) {
			dist[it->first.first] = dist[idx] + it->first.second;
			heap.push(make_pair(dist[it->first.first], it->first.first));
		}
	}
	shortest[1] = true;
	queue<int> q;
	for (q.push(1); !q.empty(); ) {
		int idx = q.front();
		q.pop();
		FOREACH(it, redge[idx]) if (!shortest[it->first.first] && dist[it->first.first] == dist[idx] - it->first.second) {
			shortest[it->first.first] = true;
			q.push(it->first.first);
		}
	}
	FOR(i, 0, n) if (shortest[i]) {
		FOREACH(it, edge[i]) if (shortest[it->first.first] && dist[i] + it->first.second == dist[it->first.first]) {
			possible[it->second] = true;
		}
	}
}

int main() {
	int taskNumber; scanf("%d", &taskNumber);
	for (int taskIdx = 1; taskIdx <= taskNumber; taskIdx++) {
		scanf("%d%d%d", &n, &m, &p);
		FOR(i, 0, m) {
			scanf("%d%d%d%d", &u[i], &v[i], &a[i], &b[i]);
			u[i]--; v[i]--;
		}
		memset(possible, 0, sizeof(bool) * m);
		FOR(mask, 0, 1 << m) {
//printf("start mask = %d\n", mask);
			FOR(i, 0, n) {
				edge[i].clear();
				redge[i].clear();
			}
			FOR(i, 0, m) {
				edge[u[i]].push_back(make_pair(make_pair(v[i], (mask & (1 << i)) ? a[i] : b[i]), i));
				redge[v[i]].push_back(make_pair(make_pair(u[i], (mask & (1 << i)) ? a[i] : b[i]), i));
			}
			calc();
//printf("end mask = %d\n", mask);
		}
		int res = -1;
		FOR(i, 0, p) {
			int x; scanf("%d", &x);
			if (res == -1 && !possible[x - 1]) res = x;
		}
		printf("Case #%d: ", taskIdx);
		if (res == -1) puts("Looks Good To Me");
		else printf("%d\n", res);
	}
	return 0;
}
