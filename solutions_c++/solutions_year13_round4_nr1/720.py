#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;

const ll mod=1000002013LL;

struct ud {
	ll kde;
	int vystup;
	ll p;
	bool operator<(const ud &u) const { return kde<u.kde || (kde==u.kde && vystup<u.vystup); }
} events[2005];

ll cena(ll st);

vector<ud> halda;

int T;
ll N, M;
ll o, e, p;
ll puv, nov;

int main()
{
	scanf("%d", &T);

for(int t=1; t<=T; t++) {
	puv=nov=0;
	scanf("%lld%lld", &N, &M);
	for(int i=0; i<M; i++) {
		scanf("%lld%lld%lld", &o, &e, &p);
		events[2*i].kde=o;
		events[2*i].vystup=-1;
		events[2*i].p=p;
		events[2*i+1].kde=e;
		events[2*i+1].vystup=1;
		events[2*i+1].p=p;
		puv=( puv + p*cena(e-o) ) % mod;
	}
	sort(events, events+2*M);
	for(int i=0; i<2*M; i++) {
		if(events[i].vystup==-1) {
			halda.push_back(events[i]);
			push_heap(halda.begin(), halda.end());
		}
		else {
			p=events[i].p;
			while(p) {
				ll lidi=min(p, halda.front().p);
				nov=( nov + lidi*cena(events[i].kde-halda.front().kde) ) % mod;
				halda.front().p-=lidi;
				if(halda.front().p==0) {
					pop_heap(halda.begin(), halda.end());
					halda.pop_back();
				}
				p-=lidi;
			}
		}
	}
	printf("Case #%d: %lld\n", t, (puv-nov+mod)%mod);
}

	return 0;
}

ll cena(ll st)
{
	return ( ( st * (2*N+1-st) ) / 2 ) % mod;
}
