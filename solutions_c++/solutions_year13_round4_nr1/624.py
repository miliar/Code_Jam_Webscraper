#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;

#define MOD 1000002013
#define INF 2000000000

struct Bod {
	int o;
	int e;
	int pocet;
};

ll n, m;
Bod start[11111];
Bod konec[11111];
vector<Bod> hp;

bool cmpo(const Bod &a, const Bod&b) {
	return (a.o<b.o);
}
bool cmpe(const Bod &a, const Bod&b) {
	return (a.e<b.e);
}

ll cena(ll k) {
	return ((k*(n + n - k + 1))/2)%MOD;
}

void solve() {
	hp.clear();
	scanf("%lld%lld", &n, &m);
	ll puv = 0;
	REP (i, m) {
		int o, e, p;
		scanf("%d%d%d", &o, &e, &p);
		start[i] = (Bod){o, e, p};
		konec[i] = (Bod){o, e, p};
		puv = (puv + p*cena(e-o))%MOD;
	}
	sort(start, start+m, cmpo);
	sort(konec, konec+m, cmpe);
	start[m] = (Bod){INF, INF, INF};
	konec[m] = (Bod){INF, INF, INF};
	int i = 0;
	int j = 0;
	ll ans = 0;
	while (i<m || j<m) {
		//printf("%d %d %d %d\n", i, j, start[i].o, konec[j].e);
		if (start[i].o<=konec[j].e) {
			//printf("o%d %d\n", start[i].o, start[i].pocet);
			hp.push_back(start[i]); push_heap(hp.begin(), hp.end(), cmpo);
			i++;
		}
		else {
			//printf("o%d %d\n", konec[j].e, konec[j].pocet);
			int akt = konec[j].pocet;
			while (akt>0) {
				if (hp.empty()) {printf("ERROR\n"); return ;}
				int diff = min(akt, hp[0].pocet);
				akt -= diff; hp[0].pocet -= diff;
				ans = (ans + diff*cena(konec[j].e-hp[0].o))%MOD;
				if (hp[0].pocet==0) {
					pop_heap(hp.begin(), hp.end(), cmpo); hp.pop_back();
				}
			}
			j++;
		}
	}
	printf("%lld\n", (puv-ans+MOD)%MOD);
}

int main()
{
	int t;
	scanf("%d", &t);
	REP (i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
