#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define mp make_pair
#define pb push_back
typedef long long ll;

ll N, M;

ll get(ll x, ll y) {
	return (y*x - (y*(y-1))/2)%1000002013;
}


int main() {
	int T, TC = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%lld%lld", &N, &M);
		ll origin = 0, ans = 0;

		set<ll> t;
		map<ll, ll> in, out;
		while (M--) {
			ll a, b, c;
			scanf("%lld%lld%lld", &a, &b, &c);
			in[a]; in[a]+=c;
			out[b]; out[b]+=c;
			t.insert(a); t.insert(b);
			origin += get(N, b - a) * c;
			origin %= 1000002013;
		}
		//printf("%lld\n", origin);
		vector<pair<ll, ll> > p(t.size());
		ll top = -1;

		for (set<ll>::iterator itr = t.begin(); itr != t.end(); itr++) {
			p[++top] = mp(*itr, in[*itr]);
			ll now = out[*itr];
			
			while (now > 0) {
				if (p[top].second <= now) {
					now -= p[top].second;
					ans += get(N, (*itr) - p[top].first) * p[top].second;
					//printf("%lld %lld %lld\n", (*itr) - p[top].first, p[top].second, ans);
					top--;
				} else {
					p[top].second -= now;
					ans += get(N, (*itr) - p[top].first) * now;
					//printf("%lld %lld %lld\n", (*itr) - p[top].first, now, ans);
					now = 0;
				}
			}
			ans %= 1000002013;
		}
		printf("Case #%d: %lld\n", TC++, ((origin - ans)%1000002013 + 1000002013)%1000002013);
	}
}