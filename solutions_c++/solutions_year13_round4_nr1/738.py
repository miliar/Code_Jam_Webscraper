#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdint.h>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG
#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif
#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

typedef long long ll;

const ll MOD = 1000002013ll;

ll cost(int n, int o, int e)
{

	ll d = e - o;
	ll x = ((d * (d + 1)) / 2)  % MOD;
	ll r = ((d * ll(n)) % MOD + d - x) % MOD;
	return r;
}

int main(){
	//Descomente para acelerar cin
	//ios::sync_with_stdio(false);
	int ntc;
	scanf("%d", &ntc);
	FORN(tc, 0, ntc){
		int n, m;
		scanf("%d%d", &n, &m);
		vector<pair<int, int> > os(m);
		vector<pair<int, int> > es(m);
		ll should = 0;
		FORN(i, 0, m){
			scanf("%d%d%d", &os[i].first, &es[i].first, &es[i].second);
			os[i].second = es[i].second;
			should = (should + (ll(os[i].second) * cost(n, os[i].first, es[i].first)) % MOD) % MOD;
		}
		sort(ALL(es));
		sort(ALL(os));
		ll payed = 0;
		int pos = 0;
		stack<pair<int, int> > s;
		FORN(i, 0, m){
			while(pos < m and os[pos].first <= es[i].first) s.push(os[pos++]);

			while(es[i].second){
				assert(not s.empty());
				int q = min(es[i].second, s.top().second);
				payed = (payed + (ll(q) * cost(n, s.top().first, es[i].first)) % MOD) % MOD;
				s.top().second -= q;
				es[i].second -= q;
				if(s.top().second == 0) s.pop();
			}
		}

		ll lost = (should - payed) % MOD;
		lost = (lost + MOD) % MOD;
		printf("Case #%d: %lld\n", tc + 1, lost);
	}
	
}
