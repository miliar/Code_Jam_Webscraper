#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>

typedef long long LL;

using namespace std;

const int mo = 1000002013;
int T, n, m, s, t, c, cnt;
pair<int, LL> P[2010];
map<int, LL> S;

int main() {
	scanf("%d", &T);
	for (int Test = 1; Test <= T; Test++) {
		scanf("%d%d", &n, &m);

		LL ans = 0;
		cnt = 0;
		for (int i = 0; i < m; i++) {
			scanf("%d%d%d", &s, &t, &c);
			ans = (ans + (LL)(n + n - (t - s) + 1) * (t - s) / 2 % mo * c) % mo;
			P[cnt].first = s; P[cnt++].second = -c;
			P[cnt].first = t; P[cnt++].second = c;
		}
		sort(P, P + cnt);
		S.clear();
		LL p = 0;
		for (int i = 0; i < cnt; i++) {
			if (P[i].second < 0) {
				S[P[i].first] -= P[i].second;
			} else {
				LL r = P[i].second;
				while (r) {
					LL now = min(r, S.rbegin()->second);
					ans = (ans - (LL)(n + n - (P[i].first - S.rbegin()->first) + 1) * (P[i].first - S.rbegin()->first) / 2 % mo * now) % mo;
					r -= now;
					if (S.rbegin()->second == now) S.erase(S.rbegin()->first);
					else S[S.rbegin()->first] -= now;
				}
			}
		}

		ans = (ans % mo + mo) % mo;
		printf("Case #%d: %d\n", Test, (int)ans);
	}
}
