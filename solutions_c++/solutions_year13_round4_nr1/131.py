#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <math.h>
#include <memory.h>

using namespace std;
long long MOD = 1000002013;



int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int N, M;
		scanf("%d%d", &N, &M);
		vector< pair<pair<long long, long long>, long long> > events;
		long long should = 0;
		for (int i = 0; i < M; i++)
		{
			long long o, e, p;
			scanf("%lld%lld%lld", &o, &e, &p);
			long long q = e - o;
			should = should + (q * N - q * (q-1) / 2) % MOD * p; 
			should %= MOD;

			events.push_back(make_pair(make_pair(o, -1), p));
			events.push_back(make_pair(make_pair(e, 1), p));
		}
		sort(events.begin(), events.end());
		stack<pair<long long, long long> > route;
		long long have = 0;
		for (int i = 0; i < events.size(); i++)
		{
			if (events[i].first.second == -1)
			{
				route.push(make_pair(events[i].first.first, events[i].second));
			}
			else
			{
				long long place = events[i].first.first;
				long long need = events[i].second;
				while (need > 0)
				{
					pair<long long, long long> p = route.top();
					route.pop();
					long long cnt = min(p.second, need);
					
					long long q	= place - p.first;
					have = have + (q * N - q * (q-1) / 2) % MOD * cnt;
					have %= MOD;
					need -= cnt;
					p.second -= cnt;
					if (p.second > 0)
						route.push(p);
				}
			}
		}
		long long res = (should - have + MOD) % MOD;
		printf("Case #%d: %lld\n", t+1, res);
	}

	return 0;
}