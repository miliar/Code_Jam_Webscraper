#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define mp(x, y) make_pair((x), (y))
#define pb(x) push_back(x)

typedef long long ll;

#define pt pair<ll,ll>

ll cross(pt a, pt b, pt c)
{
	return (b.first-a.first)*(c.second-a.second)-(b.second-a.second)*(c.first-a.first);
}

ll is_on_the_hull(vector<pt> pts, pt tree)
{
	vector<pt> hull;

	sort(pts.begin(), pts.end());
	if(pts[0].first==tree.first || pts[pts.size()-1].first==tree.first) return 1;

	hull.clear();
	for(ll i=0; i<pts.size(); i++) {
		while(hull.size()>1) {
			if(cross(hull[hull.size()-2], hull[hull.size()-1], pts[i])<0) {
				hull.pop_back();
			} else {
				break;
			}
		}
		hull.pb(pts[i]);
	}
	for(ll i=0; i<hull.size(); i++) {
		if(hull[i]==tree) return 1;
	}

	for(ll i=0; i<pts.size(); i++) pts[i].second=-pts[i].second;
	tree.second=-tree.second;
	sort(pts.begin(), pts.end());

	hull.clear();
	for(ll i=0; i<pts.size(); i++) {
		while(hull.size()>1) {
			if(cross(hull[hull.size()-2], hull[hull.size()-1], pts[i])<0) {
				hull.pop_back();
			} else {
				break;
			}
		}
		hull.pb(pts[i]);
	}
	for(ll i=0; i<hull.size(); i++) {
		if(hull[i]==tree) return 1;
	}

	return 0;
}

ll bitcnt(ll m)
{
	ll res=0;
	while(m) {
		res+=(m&1);
		m>>=1;
	}
	return res;
}

ll t;
ll n;
vector<pt> in;

int main()
{
scanf("%lld", &t);

for(ll q=1; q<=t; q++) {
	scanf("%lld", &n);
	in.resize(n);
	for(ll i=0; i<n; i++) {
		scanf("%lld%lld", &in[i].first, &in[i].second);
	}
	printf("Case #%lld:\n", q);
	for(ll i=0; i<n; i++) {
		ll ans=n-1;
		for(ll m=1; m<(1LL<<n); m++) {
			if(!(m&(1LL<<i))) continue;
			vector<pt> pts;
			for(ll k=m, j=0; k>0; k>>=1, j++) {
				if(k&1) pts.pb(in[j]);
			}
			if(is_on_the_hull(pts, in[i])) ans=min(ans, n-bitcnt(m));
		}
		printf("%lld\n", ans);
	}
}

	return 0;
}
