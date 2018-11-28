#include <iostream>
#include <cstdio>
#include <set>
#include <algorithm>

#define MAX_M 2005
#define MOD 1000002013
#define PA pair<lld, lld>

using namespace std;

typedef long long lld;

int tests;
lld answer, n, m, o[MAX_M], e[MAX_M], p[MAX_M];
lld tmp, tmp2, tmp3, tmp4;
PA ev[MAX_M];
multiset<PA> S;
multiset<PA>::iterator it;

int main() {
	scanf("%d", &tests);
	for (int test = 0 ; test < tests ; test ++) {
		scanf("%lld %lld", &n, &m);
		for (int i = 0 ; i < m ; i ++) {
			scanf("%lld %lld %lld", &o[i], &e[i], &p[i]);
			ev[2 * i] = PA(o[i], -p[i]);
			ev[2 * i + 1] = PA(e[i], p[i]);
		}
		//printf("XXX");
		//fflush(stdout);
		sort(ev, ev + 2 * m);
		answer = 0;
		S.clear();
		for (int i = 0 ; i < 2 * m ; i ++) {
			//printf("YYY %d\n", i);
			//fflush(stdout);
			if (ev[i].second < 0) {
				S.insert(PA(ev[i].first, -ev[i].second));
			}	else if (ev[i].second > 0) {
				//printf("TTT %lld %d %d %lld\n", 2 * m,  i, (int)S.size(), ev[i].second);
				//fflush(stdout);
				it = S.end();
				it --;
				lld tmp = min(it->second, ev[i].second);
				answer -= tmp * ((((2 * n - (ev[i].first - it->first) + 1) * (ev[i].first - it->first)) / 2) % MOD);
				if (tmp == it->second) {
					S.erase(it);
				} else {
					tmp3 = it->first;
					tmp4 = it->second;
					S.erase(it);
					S.insert(PA(tmp3, tmp4 - tmp));
				}
				ev[i].second -= tmp;
				if (ev[i].second > 0) {
					i --;
				}
			}
			answer = (answer % MOD + MOD) % MOD;
		}
		for (int i = 0 ; i < m ; i ++) {
			answer += p[i] * ((((2 * n - (e[i] - o[i]) + 1) * (e[i] - o[i])) / 2) % MOD);
			answer = (answer % MOD + MOD) % MOD;
		}
		printf("Case #%d: ", test + 1);
		printf("%lld\n", answer);
	}
	return 0;
}