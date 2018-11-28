#include <iostream>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

#define REP(i, n) for(int i(0); (i)<(int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= int(b); i++)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair

const int N = 1000006;
int n, m, d, S[N], M[N], ON[N], CN[N];
vector<int> E[N];
vector<pair<int, int> > all;

void solve() {
	

	scanf("%d%d", &n, &d);
	{
		int s0, a,c,r;
		scanf("%d%d%d%d", &s0, &a, &c, &r);
		REP(i, n) {
			S[i] = s0;
			s0 = ((LL)s0 * a + c) % r;
		}
	}
	{
		int s0, a,c,r;
		scanf("%d%d%d%d", &s0, &a, &c, &r);
		REP(i, n) {
			if (i)
				M[i] = s0 % i;
			s0 = ((LL)s0 * a + c) % r;
		}
	}
	REP(i, n) E[i].clear();
	REP(i, n) if (i) E[M[i]].PB(i);

	int ans = 0;
	all.clear();
	REP(i, n) {
		all.PB(MP(S[i] - d, +i + 1));
		all.PB(MP(S[i] + 1, -i - 1));
	}
	REP(i, n) ON[i] = CN[i] = false;
	sort(ALL(all));
	int best = 0;
	REP(i, all.size()) {
		int u = all[i].second;
		if (u < 0) {
			u = -u - 1;
			ON[u] = false;
			if (!u || CN[u]) {
				queue<int> Q;
				Q.push(u);
				while (!Q.empty()) {
					int i = Q.front();
					Q.pop();
					ans--;
					CN[i] = false;
					REP(j, E[i].size()) {
						int v = E[i][j];
						if (CN[v]) {
							Q.push(v);
						}
					}
				}
			}
		} else {
			u = u - 1;
			ON[u] = true;
			if (!u || CN[M[u]]) {
				queue<int> Q;
				Q.push(u);
				while (!Q.empty()) {
					int i = Q.front();
					Q.pop();
					ans++;
					CN[i] = true;
					REP(j, E[i].size()) {
						int v = E[i][j];
						if (ON[v]) {
							Q.push(v);
						}
					}
				}
			}
		}
		best = max(best, ans);
	}

	static int caseCnt = 0;
	cerr << caseCnt << endl;
	printf("Case #%d: %d\n", ++caseCnt, best);
}

int main() {
	int T = 1;
	scanf("%d", &T);
	while (T--) solve();
	return 0;
}

