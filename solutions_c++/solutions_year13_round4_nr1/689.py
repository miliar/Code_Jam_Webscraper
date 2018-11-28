#include <cstdio>
#include <set>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstring>
#include <vector>
#include <queue>


using namespace std;

typedef long long LL;
typedef pair<LL, LL> PII;


const int MAXM = 1000+1;
const LL MOD = 1000002013;

LL n, m;

inline LL getCost(LL o, LL e, LL p) {
		LL dist = e-o;
		LL cost = dist*(2*n-dist+1)/2;
		cost %= MOD;
		return (p*cost)%MOD;
}

int solve() {
	scanf("%lld %lld", &n, &m);

	
	LL res = 0;
	LL res2 = 0;

	vector<PII> events;
	for(int i = 0; i < m; i++) {
		int o, e, p;
		scanf("%d %d %d", &o, &e, &p);

		res += getCost(o, e, p);
		
		events.push_back(PII(o, -p));
		events.push_back(PII(e, p));
	}

	sort(events.begin(), events.end());

	priority_queue<PII> Q;


	for(int i = 0; i < events.size(); i++) {
		if(events[i].second < 0) {
			Q.push(PII(events[i].first, -events[i].second));
		} else {
			LL need = events[i].second;
			while(need > 0) {
				LL curr = min(need, Q.top().second);

				res2 += getCost(Q.top().first, events[i].first, curr);
				res2 %= MOD;

				//Q.top().second -= curr;
				PII top = Q.top(); Q.pop();
				top.second -= curr;
				if(top.second) Q.push(top);

				need -= curr;


			}

		}
	}

	res = (res - res2)%MOD;
	return ((res+MOD)%MOD);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: %d\n", i, solve());
	}
}