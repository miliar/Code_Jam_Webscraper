#include <bits/stdc++.h>

#define sz(z) (int)z.size()
#define fo(i,a,b) for (auto (i) = (a); (i) < (b); (i)++)
#define mp make_pair
#define pb push_back

using namespace std;

#define DEBUGz

#ifdef DEBUG
#define D(x...) printf(x)
#else
#define D(x...) 
#endif

// colour = fuel
// brown = "small hamsters running inside wheels"
// blue = natural gas
// green = solar ofc :P
// or maybe it should be yellow...

typedef long long ll;
typedef pair<int,int> ii;

const int N = 300005;
const ll inf = 1000000000000000000LL+0x420b1a2e17;

struct edge {
	int u, v, w;
	bool operator < (const edge &other) const {
		return w < other.w;
	}
};

int cost[N];

vector <edge> colour[N];

// belongs[k] is the set of colours k belongs to
vector <int> belongs[N];

// has is what is in a colour
vector <int> has[N];
ll dist[N];

vector <vector <int> > LCA[N];
vector <int> depth[N];
vector <vector <int> > wei[N];
vector <int> curLCA;
vector <int> curdep;
vector <int> curdis;
vector <ii> v[N];
vector <int> good[N];
int seen[N];
map <int, int> m[N];

int p[N];
inline int getRoot (int at) { return at == p[at] ? at : p[at] = getRoot(p[at]); }

void dfs (int at, int from, int weight) {
	curdep[at] = curdep[from]+1;
	curLCA[at] = from;
	curdis[at] = weight;
	for (ii asdf : v[at]) {
		int nxt = asdf.second;
		if (nxt != from) {
			dfs(nxt, at, asdf.first);
		}
	}
}

struct state {
	int a; ll b;
	bool operator < (const state &other) const {
		return b > other.b;
	}
};

struct pt {
	ll first; int second;
	bool operator < (const pt &other) const {
		if (first == other.first) return second < other.second;
		return first < other.first;
	}
};

set <pt> s[N];

inline int get (int c, int a, int b) {
	a = m[c][a];
	b = m[c][b];
	int ret = 0;
	if (depth[c][a] < depth[c][b]) swap(a,b);
	int dif = depth[c][a] - depth[c][b];
	for (int i = sz(LCA[c])-1; i >= 0; i--) {
		if (dif >= (1<<i)) {
			dif -= (1<<i);
			ret = max(ret, wei[c][i][a]);
			a = LCA[c][i][a];
		}
	}
	if (a == b) return ret;
	for (int i = sz(LCA[c])-1; i >= 0; i--) {
		if (LCA[c][i][a] != LCA[c][i][b]) {
			ret = max(ret, wei[c][i][a]);
			ret = max(ret, wei[c][i][b]);
			a = LCA[c][i][a];
			b = LCA[c][i][b];
		}
	}
	ret = max(ret, wei[c][0][a]);
	ret = max(ret, wei[c][0][b]);
	return ret;
}

void update (int at, ll dis) {
	ll d = dist[at];
	if (d <= dis) return;
	dist[at] = dis;
	for (int col : belongs[at]) {
		auto it = s[col].find({d,at});
		// this should never happen 
		if (it != s[col].end()) {
			s[col].erase(it);
		}
		s[col].insert({dis,at});
	}
}

int main() {
	int n, r;
	scanf("%d %d", &n, &r);
	for (int i = 1; i <= n; i++) scanf("%d", cost+i), dist[i] = inf;
	fo(i,0,r) {
		int a, b, c, d;
		scanf("%d %d %d %d", &a, &b, &c, &d);
		colour[c].pb({a,b,d});
		belongs[a].pb(c);
		belongs[b].pb(c);
		has[c].pb(a);
		has[c].pb(b);
	}
	int start, end;
	scanf("%d %d", &start, &end);
	dist[start] = 0;
	for (int i = 1; i <= n; i++) {
		sort(belongs[i].begin(), belongs[i].end());
		belongs[i].resize(unique(belongs[i].begin(), belongs[i].end()) - belongs[i].begin());
	}
	for (int i = 1; i <= r; i++) {
		if (sz(has[i]) == 0) continue;
		sort(colour[i].begin(), colour[i].end());
		int j = 0;
		curLCA.clear();
		curdis.clear();
		curdep.clear();
		sort(has[i].begin(), has[i].end());
		has[i].resize(unique(has[i].begin(), has[i].end()) - has[i].begin());
		for (auto it = has[i].begin(); it != has[i].end(); it++) {
			int at = *it;
			s[i].insert({dist[at],at});
			p[j] = j;
			m[i][*it] = j++;
			curLCA.pb(0);
			curdis.pb(0);
			curdep.pb(0);
			if (sz(belongs[*it]) > 1) {
				good[i].pb(*it);
			}
		}
		for (edge e : colour[i]) {
			int a = m[i][e.u];
			int b = m[i][e.v];
			int c = e.w;
			if (getRoot(a) != getRoot(b)) {
				p[getRoot(a)] = getRoot(b);
				v[a].pb(mp(c,b));
				v[b].pb(mp(c,a));
			}
		}
		dfs(0,0,0);
		int k = 0;
		while ((1<<k) < j) k++;
		depth[i] = curdep;
		for (int a = 0; a < k; a++) {
			LCA[i].pb(curLCA);
			wei[i].pb(curdis);
		}
		for (int a = 1; a < k; a++) {
			for (int b = 0; b < j; b++) {
				LCA[i][a][b] = LCA[i][a-1][LCA[i][a-1][b]];
				wei[i][a][b] = max(wei[i][a-1][LCA[i][a-1][b]], wei[i][a-1][b]);
			}	
		}
		for (int a = 0; a < j; a++) v[a].clear();
	}
	return 0;
	priority_queue <state> pq;
	pq.push({start,0});
	ll ans = inf;
	int asdf = 0;
	while (!pq.empty()) {
		int at = pq.top().a;
		D("I'm at %d with weight %lld\n", at, pq.top().b);
		pq.pop();
		printf("count\n");
		if (seen[at]) continue;
		seen[at] = 1;
		for (int col : belongs[at]) {
			auto it = s[col].find({dist[at], at});
			//if (it != s[col].end()) 
		//		s[col].erase(it);
			if (sz(s[col]) == 0) continue;
			it = --s[col].end();
			while (1) {
				asdf++;
				int nxt = it->second;
				ll nxtd = it->first; 
				ll d = dist[at] + cost[at] + get(col, at, nxt);
				D("nxt is %d and d is %lld\n", nxt, d);
				//if (nxtd <= dist[at] + cost[at]) break;
				if (d < nxtd) {
					if (it == s[col].begin()) {
						//s[col].erase(it);
						//update(nxt, d);
						dist[nxt] = d;
						if (sz(belongs[nxt]) > 1) 
							pq.push({nxt,d+cost[nxt]});
						break;
					} else {
						auto itt = it--;
						//s[col].erase(itt);
						//update(nxt, d);
						dist[nxt] = d;
						if (sz(belongs[nxt]) > 1) 
							pq.push({nxt,d+cost[nxt]});
					}
				} else {
					if (it == s[col].begin()) break;
					it--;
				}
			}
		}
	}
	ans = dist[end];
	printf("%lld\n", ans);
	printf("%d\n", asdf);
	return 0;
}
