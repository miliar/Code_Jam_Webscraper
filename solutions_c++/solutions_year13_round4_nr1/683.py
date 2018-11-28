#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>


using namespace std;
const int MOD = 1000002013; // check!!!
const int INF = 100000000; //1e8

typedef long long ll;
typedef pair<int,int> Pii;
typedef pair<ll,ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())
#define ten(n) ((int)1e##n)

ll money(ll diff){ return diff * (diff+1) / 2 % MOD;}

ll solve(){
	ll n;
	int m; cin>>n>>m;

	ll s1 = 0;
	map<ll,ll> l,r;
	FOR(i,m){
		ll a,b,c; cin>>a>>b>>c;
		l[a] = (l[a] + c) % MOD;
		r[b] = (r[b] + c) % MOD;
		s1 = (s1 + money(b-a) * c % MOD) % MOD;
	}

	ll s2 = 0;

	for(auto it = l.rbegin(); it != l.rend(); ++it){
		ll rem = it->second;
		auto e = r.lower_bound(it->first);

		while(rem){
			ll rem2 = e->second;
			if(rem < rem2){ //I‚í‚è
				ll add = money(e->first - it->first) * rem % MOD;
				s2 = (s2 + add) % MOD;
				r[e->first] = rem2 - rem;
				rem = 0;
			} else {
				rem -= rem2;
				ll add = money(e->first - it->first) * rem2 % MOD;
				r.erase(e);
				e = r.lower_bound(it->first);
				s2 = (s2 + add) % MOD;
			}
		}
	}

	return (s2 - s1 + MOD) % MOD;

}

int main(){

	int t; cin>>t;
	for(int i = 1; i <= t; i++){
		ll ans = solve();
		printf("Case #%d: %lld\n",i,ans);
	}

	return 0;
}
