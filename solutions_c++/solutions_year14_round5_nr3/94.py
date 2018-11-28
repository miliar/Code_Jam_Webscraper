#pragma comment(linker, "/STACK:20000000")
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
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif

const int SIZE = 1024;
const int VERTS = SIZE * SIZE;
const int MULT = 10000;

int n;
int v, s, t;

struct Edge {
	int a, b;
	int flow;
	int cap, cost;
	int anti;
};
vector<Edge> edges;
vector<int> nbr[VERTS];

void AddEdge(int a, int b, int cap, int cost) {
	Ef("%d %d %d %d\n", a, b, cap, cost);
	Edge e1;
	e1.a = a;
	e1.b = b;
	e1.flow = 0;
	e1.cap = cap;
	e1.cost = cost;
	e1.anti = edges.size() + 1;
	Edge e2;
	e2.a = b;
	e2.b = a;
	e2.flow = 0;
	e2.cap = 0;
	e2.cost = -cost;
	e2.anti = edges.size();
	nbr[a].push_back(edges.size());
	nbr[b].push_back(edges.size() + 1);
	edges.push_back(e1);
	edges.push_back(e2);
}

bool used[VERTS];
int dist[VERTS];
int father[VERTS];
int deq[VERTS];
//Pape-Levit algorithm
bool Dijkstra(int &allFlow, int &allCost) {
	memset(dist, 63, sizeof(dist));
	memset(father, -1, sizeof(father));
	memset(used, false, sizeof(used));
	dist[s] = 0;

	int l = 0, r = 1;
	deq[0] = s;

	while (l < r) {
		int best = deq[l++];
		used[best] = true;

		for (int i = 0; i<nbr[best].size(); i++) {
			int eidx = nbr[best][i];
			const Edge& e = edges[eidx];
			if (e.flow == e.cap) continue;

			int newd = dist[best] + e.cost;
			if (dist[e.b] > newd) {
				bool first = dist[e.b] > 1000000000;
				dist[e.b] = newd;
				father[e.b] = eidx;

				if (used[e.b]) {
					used[e.b] = false;
					deq[--l] = e.b;
				}
				if (first)
					deq[r++] = e.b;
			}
		}
	}

	if (!used[t]) return false;

	allFlow++;

	int curr = t;
	while (curr != s) {
		int eidx = father[curr];
		Edge &e = edges[eidx];
		int pp = e.a;
		e.flow++;
		edges[e.anti].flow--;
		allCost += e.cost;
		curr = pp;
	}

	return true;
}

typedef pair<int, int> pii;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
	    v = 0;
	    for (int i = 0; i<VERTS; i++) nbr[i].clear();
	    edges.clear();

	    scanf("%d", &n);

	    map<int, int> idmap;
	    int k = 0;
	    vector<vector<pii>> goes;

	    idmap[-1] = k++;
	    goes.push_back(vector<pii>());

	    int currtime = 0;
	    for (int i = 0; i<n; i++) {
	    	char mode;
	    	int id;
			scanf(" %c%d", &mode, &id);
			id--;
			int sgn = (mode == 'E' ? 1 : -1);

			if (!idmap.count(id)) {
				idmap[id] = k++;
				goes.push_back(vector<pii>());
			}
			id = idmap[id];

			goes[id].push_back(pii(sgn, currtime));
			currtime++;
	    }

		s = v++;
		t = v++;
		int q = v++;

        int anybase = v;
		for (int i = 0; i < goes[0].size(); i++) {
			int u = v++;
			if (goes[0][i].first > 0)
				AddEdge(s, u, 1, -MULT);
			else
				AddEdge(u, t, 1, -MULT);
		}
		Eo(k);

		for (int i = 1; i < k; i++) {
			map<int, int> tmap;
			for (int j = 0; j < goes[i].size(); j++)
				tmap[goes[i][j].second] = 0;
			for (int j = 0; j < goes[0].size(); j++)
				tmap[goes[0][j].second] = 0;
			Eo(tmap.size());

			int ttt = 0;
			for (auto it = tmap.begin(); it != tmap.end(); it++)
				it->second = ttt++;

			int pos = 0;
			for (int a = 0; a <= ttt; a++) {
				if (a == 0)
					AddEdge(s, v+a, 1, 0);
				else if (a == ttt)
					AddEdge(v+a-1, q, 1, 0);
				else
					AddEdge(v+a-1, v+a, 1, 0);
			}

			for (int j = 0; j < goes[i].size(); j++) {
				auto x = goes[i][j];
				int u = v + tmap[x.second];
				if (x.first > 0)
					AddEdge(s, u, 1, -MULT);
				else
					AddEdge(u, t, 1, -MULT);
			}
			for (int j = 0; j < goes[0].size(); j++) {
				auto x = goes[0][j];
				int u = v + tmap[x.second];
				int any = anybase + j;
				if (x.first > 0)
					AddEdge(any, u, 1, 0);
				else
					AddEdge(u, any, 1, 0);
			}            

			Eo(v);
			Eo(ttt);
			v += ttt;
		}

		AddEdge(q, t, n, 1);


		int optCost = 0;
		int optFlow = 0;
		int tflow = 0;
		int tcost = 0;
		while (Dijkstra(tflow, tcost)) {
			Ef("!");
			if (tcost >= optCost)
				break;
			optCost = tcost;
			optFlow = tflow;
		}
		Ef("\n%d %d\n", optFlow, optCost);

		int qq = optCost + n * MULT;
		if (qq >= MULT)
			printf("Case #%d: CRIME TIME\n", tt);
		else
			printf("Case #%d: %d\n", tt, qq);

		fflush(stdout);
	}

	return 0;
}
