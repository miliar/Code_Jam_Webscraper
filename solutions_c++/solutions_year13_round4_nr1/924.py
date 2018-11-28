#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

#define iter(c) __typeof((c).begin())
#define Tr(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)
#define Fr(a,b,c) for(int a = b; a < c; ++a)
#define Rp(a,c) Fr(a,0,c)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define oo 0x3F3F3F3F

#define dbg if(0)

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long rash;

#define MAXN 2000
typedef pair<ll,ll> pll;

int n, m;
pll ini[MAXN];
pll fim[MAXN];
multiset<pii> conj;

ll custo(ll tam) {
	if(tam == 0) return 0;
	if(tam == 1) return n;
	
	return tam * n - (tam * (tam - 1)) / 2;
}

int main() {
	int t, caso = 0; scanf("%d", &t);
	while(t--) {
		scanf("%d%d", &n, &m);
		Rp(i,m) scanf("%lld%lld%lld", &ini[i].F, &fim[i].F, &ini[i].S), fim[i].S = ini[i].S;
		
		ll cost = 0;
		Rp(i,m) cost += custo(fim[i].F - ini[i].F) * ini[i].S;
		
		sort(ini, ini + m);
		sort(fim, fim + m);
		
		conj.clear();
		int p = 0;
		ll ans = 0;
		Rp(i,m) { //para cada dest[]
//			dbg printf("%2d: fim (%d, %d)\n", i, fim[i].F, fim[i].S);
			while(p < m && ini[p].F <= fim[i].F) conj.insert(ini[p++]);
			int how = fim[i].S;
//			dbg printf(" how %d\n", how);
			while(how) {
				pii last = *(--conj.end());
//				dbg printf("  last (%d, %d)\n", last.F, last.S);
				conj.erase(--conj.end());
				int mini = min(how, last.S);
				ans += custo(fim[i].F - last.F) * mini;
				how -= mini, last.S -= mini;
				
				if(last.S > 0) conj.insert(last);
			}
		}
		
		printf("Case #%d: %lld\n", ++caso, cost - ans);
	}
	
	return 0;
}


