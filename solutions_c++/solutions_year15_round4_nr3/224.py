#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define N 8765
#define M 1234567
#define G 234
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
#define mp make_pair

namespace MF {
	int n, m, s, t, fr[M], to[M]; ll fl[M], cp[M]; int dst[N];
	char sn[N];
	vector<int> al[N];
	queue<int> q;

	void init(int _n) {
		n = _n+2; m = 0; s = _n; t = _n+1;
		assert(n < N);
		fo(i,0,n) al[i].clear(), sn[i] = 0;
	}
	void add(int a, int b, ll c) {
		//printf("add %d %d %lld\n", a, b, c);
		al[a].push_back(m); fr[m] = a; to[m] = b; fl[m] = 0; cp[m] = c; m++;
		al[b].push_back(m); fr[m] = b; to[m] = a; fl[m] = 0; cp[m] = 0; m++;
	}
	bool bfs() {
		fo(i,0,n) dst[i] = i==s ? 0 : -1;
		q.push(s);
		while (!q.empty()) {
			int at = q.front(); q.pop();
			fo(i,0,al[at].size()) {
				int e = al[at][i];
				if (dst[to[e]] != -1 || fl[e] == cp[e]) continue;
				dst[to[e]] = dst[at]+1;
				q.push(to[e]);
			}
		}
		return dst[t] != -1;
	}
	ll aug(int at, ll cf) {
		if (at==t) return cf;
		fo(i,0,al[at].size()) {
			int e = al[at][i];
			if (dst[to[e]] != dst[at]+1 || fl[e] == cp[e]) continue;
			ll tf = aug(to[e], min(cf, cp[e] - fl[e]));
			if (tf) {
				fl[e] += tf;
				fl[e^1] -= tf;
				return tf;
			}
		}
		dst[at] = -1;
		return 0;
	}
	ll mf() {
		ll ans = 0;
		while (bfs()) for (int add = aug(s,1e18); add; add = aug(s,1e18)) ans += add;
		return ans;
	}
	void dfs(int at) {
		sn[at] = 1;
		fo(i,0,al[at].size()) {
			int eid = al[at][i];
			if (fl[eid] != cp[eid]) {
				if (!sn[to[eid]]) dfs(to[eid]);
			}
		}
	}
	vector<int> mc() {
		dfs(s);
		vector<int> ret;
		fo(i,0,m) if (sn[fr[i]] && !sn[to[i]]) ret.push_back(i);
		return ret;
	}
}

struct cmp {
	bool operator()(const char* a, const char* b) {
		return strcmp(a,b) < 0;
	}
};

int t, n, nn, sz, aa;
string read;
map<char*,int,cmp> id;
vector<int> grs[G];
int main() {
	freopen("c2.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d", &t);
	fo(tc,1,t+1) {
		id.clear();
		fo(i,0,G) grs[i].clear();

		printf("Case #%d: ", tc);
		scanf("%d", &n);
		fo(i,0,n) {
			scanf("%d", &sz);
			fo(j,0,sz) scanf("%d", &aa), grs[i].pb(aa);
		}
		scanf("%d", &nn);
		MF::init(2*nn);
		fo(i,0,nn) MF::add(2*i, 2*i+1, 1);
		for (int at : grs[0]) MF::add(MF::s, 2*at, nn+1);
		for (int at : grs[1]) MF::add(2*at+1, MF::t, nn+1);
		fo(i,2,n) for (int at1 : grs[i]) for (int at2 : grs[i]) if (at1 != at2) MF::add(2*at1+1, 2*at2, nn+1);
		assert(MF::m < M);
		printf("%lld\n", MF::mf());
	}

	return 0;
}