#include <stack>
#include <cstdio>
#include <vector>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <iostream>
#define MAXN (1 << 15)
using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> plp;

const ll mod = 1000002013LL;

ll n, m;
ll a[MAXN], b[MAXN], am[MAXN];

vector< plp > events;
stack< pll > beg;

ll calc(ll t, ll p) {
	//printf("into calc %I64d %I64d\n", t, p);
	ll now = t*n - (t * (t-1LL)) / 2LL;
	assert(now >= 0);
	if (now >= mod) now %= mod;
	now *= p;
	assert(now >= 0);
	if (now >= mod) now %= mod;
	
	return now;
}

inline void solve(int test) {
	ll cur = 0LL;
	
	for (int i=0; i < m; ++i) {
		cur += calc(b[i]-a[i], am[i]);
		assert(cur >= 0);
		if (cur >= mod)
			cur -= mod;
	}
//	printf("%I64d\n", cur);
	sort(events.begin(), events.end());
	
	ll best = 0LL;
	for (int i=0; i < (int)events.size(); ++i) {
		ll at = events[i].first;
		
		if (events[i].second.first == 0) {
			beg.push( make_pair(events[i].first, events[i].second.second) );
		} else {
			ll people = events[i].second.second;
			while (people > 0LL) {
				//printf("-- %I64d\n", people);
				if (people >= beg.top().second) {
					//printf("here!\n");
					people -= beg.top().second;
					best += calc(at-beg.top().first, beg.top().second);
					assert(best >= 0);
					if (best >= mod)
						best -= mod;
					
					beg.pop();
				} else {
					//printf("not here!\n");
					best += calc(at-beg.top().first, people);
					assert(best >= 0);
					if (best >= mod)
						best -= mod;
						
					beg.top().second -= people;
					people = 0LL;
					break;
				}
			}
		}
	}

//	printf("%I64d\n", best);
	
	ll ans = cur - best;
	while (ans < 0LL) ans += mod;
	
	if (ans >= mod) ans %= mod;
	
	cout << "Case #" << test << ": " << ans << '\n';
}

inline void read() {
	cin >> n >> m;
	
	for (int i=0; i < m; ++i) {
		cin >> a[i] >> b[i] >> am[i]; 
		events.push_back( make_pair(a[i], make_pair(0, am[i]) ) ); // beg
		events.push_back( make_pair(b[i], make_pair(1, am[i]) ) ); // end
	}
}

inline void clear() {
	while (beg.size() > 0) beg.pop();
	events.clear();
}

int main() {
	int brt = 0, test = 0;
	cin >> brt;
	
	while (brt --) {
		clear();
		read();
		solve(++test);
	}
	return 0;
}