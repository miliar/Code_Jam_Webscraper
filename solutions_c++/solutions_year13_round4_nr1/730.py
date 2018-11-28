#include <stdio.h>
#include <queue>
#include <algorithm>

#define MOD 1000002013LL

using namespace std;

typedef long long ll;

pair< pair<ll, ll>, ll > ent[2048];

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		ll n, m;
		scanf("%lld%lld", &n, &m);

		ll sol = 0;
		for(int i = 0; i < m; i++) {
			ll d;
			scanf("%lld%lld%lld", &ent[2*i].first.first, &ent[2*i+1].first.first, &d);
			ent[2*i].first.second = 0;
			ent[2*i+1].first.second = 1;
			ent[2*i].second = d;
			ent[2*i+1].second = d;
			ll k = ent[2*i+1].first.first - ent[2*i].first.first;
			sol += (d*((((k*n)%MOD)-((k*(k-1)/2)%MOD)+MOD)%MOD))%MOD;
			sol = sol%MOD;
		}

		sort(ent, ent+2*m);

		priority_queue<pair<ll,ll> > fila;
		for(int i = 0; i < 2*m; i++) { 
			if(ent[i].first.second == 0)
				fila.push(make_pair(ent[i].first.first, ent[i].second));
			else while(ent[i].second) {
				pair<ll, ll> topo = fila.top();
				fila.pop();

				ll k = ent[i].first.first - topo.first;
				ll m = min(ent[i].second, topo.second);
				sol -= (m*((((k*n)%MOD)-((k*(k-1)/2)%MOD)+MOD)%MOD))%MOD;
				sol = (sol + MOD)%MOD;

				ent[i].second -= m;
				topo.second -= m;
				if(topo.second != 0) fila.push(topo);
			}
		}
		printf("Case #%d: %lld\n", t, sol);
	}
	return 0;
}
