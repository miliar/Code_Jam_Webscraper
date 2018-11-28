#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>
#include <ctime>


using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll rdtsc() {
    ll tmp;
    asm("rdtsc" : "=A"(tmp));
    return tmp;
}

#define TASKNAME "text"
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
#define INF ((int)1e9 + 10)
#define sqr(x) ((x) * (x))         
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

struct Graph {
	vvi es, cs;
	int n;

	void build(int _n) {
		n = _n;
		es = cs = vvi(n);
	}

	void adde(int s, int t, int c) {
		es[s].pb(t);
		cs[s].pb(c);
	}

	vi dist;

	void countDists(int S) {
		dist = vi(n, INF);
		dist[S] = 0;
		vi used(n, 0); 
		for (int iter = 0; iter < n; iter++) {
			int v = -1;
			for (int i = 0; i < n; i++) {
			 	if (!used[i] && (v == -1 || dist[v] > dist[i]))
			 		v = i;
			}

			if (v == -1 || dist[v] == INF)
				break;

			used[v] = 1;
			for (int it = 0; it < sz(es[v]); it++) {
				int u = es[v][it];
				if (dist[u] > dist[v] + cs[v][it]) {
					dist[u] = dist[v] + cs[v][it];
				}
			}	
		}
	}
} g1, g2;

const int maxm = 2000;
int edges[maxm][4];

void solve(int testCase) {
	printf("Case #%d: ", testCase);
	int n, m, p;
	scanf("%d%d%d", &n, &m, &p);
	g1.build(n), g2.build(n);
	for (int i = 0; i < m; i++) {
		int s, t, a, b;
		scanf("%d%d%d%d", &s, &t, &a, &b);
		--s, --t;
		g1.adde(t, s, a);
		g2.adde(t, s, b);
		edges[i][0] = s, edges[i][1] = t;
		edges[i][2] = a, edges[i][3] = b;
	}
	g1.countDists(1);
	g2.countDists(1);
	Graph g3 = g2;

	int minVal = INF;
	int sum = 0;
	vi perm(p), sums(p);
	int ans = -1;
	for (int i = 0; i < p; i++)
		scanf("%d", &perm[i]);
	for (int i = 0; i < p; i++) {
		--perm[i];
		minVal = min(minVal, g2.dist[edges[perm[i]][0]] + sum);
		sums[i] = sum;
		sum += edges[perm[i]][2];
		//eprintf("minVal = %d, sum = %d, curVal = %d\n", minVal, sum, sum + g1.dist[edges[perm[i]][1]]);
		if (sum + g1.dist[edges[perm[i]][1]] > minVal) {
			ans = perm[i] + 1;
			break;
		}
		//eprintf("from %d\n", edges[perm[i]][1]);
		g3.countDists(edges[perm[i]][1]);
		bool ok = 1;
		for (int j = 0; ok && j <= i; j++) {
			int v = edges[perm[j]][0];
			//eprintf("%d %d\n", v, g3.dist[v] + sums[j]);
			if (g3.dist[v] + sums[j] < sum) {
				ok = 0;
				break;	
			}
		}

		if (!ok) {
			ans = perm[i] + 1;
			break;
		}	
	}

	if (ans == -1)
		printf("Looks Good To Me\n");
	else
		printf("%d\n", ans);
	//exit(0);
}


int main() {
	srand(rdtsc());
#ifdef DEBUG
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);
#endif
	
	int testCase = 0, n;
	while (scanf("%d", &n) >= 1) {
		for (int i = 0; i < n; i++)
			solve(++testCase);
		//break;
	}
	return 0;
}
