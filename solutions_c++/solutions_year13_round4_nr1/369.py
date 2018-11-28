#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
#include <queue>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <stack>
#include <map>
#include <cassert>
#include <set>
#include <iomanip>
using namespace std;

#include "gmpxx.h"
typedef mpz_class big;

#define REP(i,n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define MP make_pair
#define PB push_back

const ll MOD = 1000002013;
const int N = 1005;
ll n, m, o[N], e[N], p[N];
map<int, ll> on, off;

ll f_mod(ll x) {
    //does proper modulus (x % mod) correctly handling negatives
    return x >= 0 ? x % MOD : (MOD - ((-x) % MOD)) % MOD;
}

ll cost_dist(ll x, ll y) {
	x = y - x;
	return f_mod( ((x * n)%MOD - (x * (x - 1) / 2)%MOD) );
}

int main() {
	/* big x, y;
	cin >> x >> y;
	cout << (x+y) << endl; /**/
	
	int T;
	cin >> T;
	REP(qqq,T) {
		//logic start
		cin >> n >> m;
		
		ll costA = 0, costB = 0;
		vector<ll> v;
		on.clear();
		off.clear();
		
		REP(i,m) { 
			cin >> o[i] >> e[i] >> p[i];
			
			on[ o[i] ] += p[i];
			off[ e[i] ] += p[i];
			
			v.PB(o[i]);
			v.PB(e[i]);
			
			costA += (cost_dist(o[i], e[i]) * p[i]) % MOD;
			costA %= MOD;
		}
		
		sort(v.begin(), v.end());
		v.erase(unique(v.begin(), v.end()), v.end());
		
		priority_queue<pair<ll,ll> > pq;
		REP(i,v.size()) {
			//cout << "!" << v[i] << endl;
			
			if (on[v[i]])
				pq.push(MP(v[i], on[ v[i] ]));
			
			ll out = off[ v[i] ];
			while (out) {
				ll match = min(out, pq.top().second);
				
				//cout << match << " " << pq.top().first << " " << v[i] << " " << pq.top().second << endl;
				
				costB += (cost_dist(pq.top().first, v[i]) * (match%MOD)) % MOD;
				costB %= MOD;
				
				if (match == pq.top().second)
					pq.pop();
				else {
					pair<ll,ll> p = pq.top();
					pq.pop();
					p.second -= match;
					pq.push(p);
				}
				out -= match;
			}
		}
		
		//logic end
		ll ans = f_mod(costA - costB);
		cout << "Case #" << (qqq+1) << ": " << ans << endl;
		//cout << costA << " " << costB << endl;
		//if (qqq == 1) return 0;
	}
}
