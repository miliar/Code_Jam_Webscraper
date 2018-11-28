#include <cassert>
#include <cstdio>
#include <set>
#include <map>
#include <queue>
using namespace std;
typedef long long llong;

int N, M;
const int mod = 1000002013;

int main(void)
{
	int tc;
	scanf("%d", &tc);
	for (int T = 1; T <= tc; ++T) {
		set<int> pows;
		map<int,llong> entries, leaves;

		llong total_cost = 0;
		scanf("%d %d", &N, &M);
		for (int i = 0; i < M; ++i) {
			int o, e, p;
			scanf("%d %d %d", &o, &e, &p);
			pows.insert(o);
			pows.insert(e);
			entries[o] += p;
			leaves[e] += p;
			llong k = e - o;
			llong ticket_cost = (k*N - (k*k-k)/2) % mod;
			total_cost += p * ticket_cost;
			total_cost %= mod;
		}

		llong swap_cost = 0;
		priority_queue<pair<int,llong> > people;
		for (set<int>::iterator it = pows.begin(); it != pows.end(); ++it) {
			int s = *it;
			if (entries[s] > 0)
				people.push(make_pair(s, entries[s]));
			llong to_leave = leaves[s];
			while (to_leave > 0) {
				assert(people.size() > 0);
				int o = people.top().first;
				llong p = people.top().second;
				people.pop();
				if (p > to_leave) {
					people.push(make_pair(o, p - to_leave));
					p = to_leave;
				}
				llong k = s - o;
				llong ticket_cost = (k*N - (k*k-k)/2) % mod;
				swap_cost += (p%mod) * ticket_cost;
				swap_cost %= mod;
				to_leave -= p;
			}
		}
		assert(people.size() == 0);

		//printf("tc = %lld\nsc = %lld\n", total_cost, swap_cost);
		if (total_cost < swap_cost)
			total_cost += mod;
		printf("Case #%d: %lld\n", T, total_cost-swap_cost);
	}
	return 0;
}
