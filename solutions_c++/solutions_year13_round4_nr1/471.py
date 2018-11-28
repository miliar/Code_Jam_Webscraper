#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

const tint MOD = 1000002013LL;

tint cuenta(tint n, tint k){
	tint ret = k * (n - (k-1LL)/2LL);
	if((k-1LL)%2LL == 1)
		ret -= k/2LL;
	return ret;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	
	int T;
	cin >> T;
	
	forn(t, T){
		tint n; int m;
		cin >> n >> m;
		
		vector<pair<tint, pair<tint, tint> > > info;
		forn(i,m){
			pair<tint, pair<tint, tint> > pi;
			cin >> pi.first >> pi.second.first >> pi.second.second;
			info.push_back(pi);
		}
		
		tint suma = 0, resta = 0;
		sort(info.begin(), info.end());
		map<tint, tint> origs;
		map<tint, tint> fin;
		forn(i, info.size()){
			suma += info[i].second.second * cuenta(n, info[i].second.first - info[i].first);
			suma %= MOD;
			while(fin.size() > 0){
				map<tint,tint>::iterator it = fin.begin();
				if(info[i].first <= it->first) break;
				
				while(it->second > 0){
					map<tint,tint>::iterator ot = origs.lower_bound(it->first);
					if(ot->first > it->first) ot--;
					tint kk = min(ot->second, it->second);
					it->second -= ot->second;
					ot->second -= kk;
					resta += kk * cuenta(n, it->first - ot->first);
					resta %= MOD;
					if(ot->second == 0) origs.erase(ot);
				}
				fin.erase(it);
			}
			
			origs[info[i].first] += info[i].second.second;
			fin[info[i].second.first] += info[i].second.second;
		}
		while(fin.size() > 0){
			map<tint,tint>::iterator it = fin.begin();
			
			while(it->second > 0){
				map<tint,tint>::iterator ot = origs.lower_bound(it->first);
				if(ot->first > it->first) ot--;
				tint kk = min(ot->second, it->second);
				it->second -= ot->second;
				ot->second -= kk;
				resta += kk * cuenta(n, it->first - ot->first);
				resta %= MOD;
				if(ot->second == 0) origs.erase(ot);
			}
			fin.erase(it);
		}

		printf("Case #%i: %lld\n", t+1, suma - resta);
	}
	
	return 0;
}
