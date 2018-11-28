#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define ll long long
#define PII pair<int,int>
#define pll pair<ll,ll>
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SIZE(v) (int)v.size()
#define MOD 1000002013ll

int T,cs,N,M;
ll s[1111], e[1111], p[1111];
map<pll,ll> mp;
map<pll,ll>::iterator it;

ll f(ll cnt) {
	return N * cnt - (cnt + 1) * cnt / 2;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&T);
	for(cs=1;cs<=T;++cs) {
		scanf("%d%d",&N,&M), mp.clear();

		ll tot = 0;
		for(int i=0;i<M;++i) scanf("%lld %lld %lld",s + i, e + i, p + i);
		for(int i=0;i<M;++i) {
			mp[MP(s[i],e[i])] += p[i];
			tot += f(e[i] - s[i]) * p[i];
		}
		
		ll ans = 0;
		while(mp.size()) {
			pll cur = mp.begin()->first;
			ll cnt = mp.begin()->second;
			ll cs = cur.first;
			ll ce = cur.second;
			mp.erase(mp.begin());

			if(cnt == 0) continue;

			for(it=mp.begin();it!=mp.end();++it) {
				if(cnt == 0) break;
				if(it->second == 0) continue;
				ll ns = it->first.first;
				ll ne = it->first.second;
				ll nct = it->second;
				if(cs < ns && ns <= ce && ce < ne) {
					ll sum = min(cnt,nct);
					cnt -= sum;
					mp[MP(ns,ne)] -= sum;
					mp[MP(ns,ce)] += sum;
					mp[MP(cs,ne)] += sum;
				}
			} ans += f(ce - cs) * cnt;
		} printf("Case #%d: %lld\n", cs, tot - ans);
	}
}