#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

#define FOR(i,a,b) for (int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define PB push_back

#define N 30
const int inf = 1 << 28;
bool e[N+N][N+N], vis[N+N];
int cntL, cntR, n;
map<int, int> p2cnt;
map<map<int, int>, int> opt;

void dfs(int u) {
	vis[u] = 1;
	if (u < n) ++cntL; else ++cntR;
	REP(v, n+n) if (e[u][v] && !vis[v]) dfs(v);
}

void deleteOne(map<int, int>& p2cnt, int p) {
	if (--p2cnt[p] == 0) p2cnt.erase(p);
}

int calc(const map<int, int>& p2cnt) {
	if (opt.count(p2cnt)) return opt[p2cnt];
	if (p2cnt.empty()) return 0;
	int res = inf;
	for (map<int, int>::const_iterator itr1 = p2cnt.begin(); itr1 != p2cnt.end(); ++itr1)
	for (map<int, int>::const_iterator itr2 = itr1; itr2 != p2cnt.end(); ++itr2) {
		int p1 = itr1->first, p2 = itr2->first;
		if (p1 == p2 && itr1->second < 2) continue;
		int p = p1 + p2, cost = 0;
		map<int, int> np = p2cnt;
		deleteOne(np, p1);
		deleteOne(np, p2);
		if (p / N == p % N) cost = (p / N) * (p / N);
		else ++np[p];
		res = min(res, calc(np) + cost);
	}
	return opt[p2cnt] = res;
}

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int m = 0;
		cin >> n;
		memset(e, 0, sizeof(e));
		REP(i, n) {
			string s;
			cin >> s;
			REP(j, n) {
				e[j+n][i] = e[i][j+n] = s[j] - '0';
				m += e[i][j+n];
			}
		}
		p2cnt.clear();
		memset(vis, 0, sizeof(vis));
		int ans = 0;
		REP(i, n+n) if (!vis[i]) {
			cntL = cntR = 0;
			dfs(i);
			// printf("cL = %d, cR = %d\n", cntL, cntR);
			if (cntL == cntR) ans += cntL*cntL;
			else ++p2cnt[cntL*N+cntR];
		}
		ans += calc(p2cnt);
		printf("Case #%d: %d\n", cN, ans - m);
	}
}
