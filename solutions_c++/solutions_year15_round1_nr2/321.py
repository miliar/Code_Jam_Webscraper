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

ll t;
ll b, n;
ll m[1234];

ll ev(ll t, ll j)
{
	ll res=0;
	for(ll i=0; i<b; i++) {
		if(i<=j) res+=t/m[i]+1;
		else res+=(t%m[i]==0 ? t/m[i] : t/m[i]+1);
	}
	return res;
}

int main()
{
scanf("%lld", &t);

for(ll q=1; q<=t; q++) {
	scanf("%lld%lld", &b, &n);
	for(ll i=0; i<b; i++) scanf("%lld", &m[i]);

	ll ans;

	for(ll i=0; i<b; i++) {
		ll l=0, r=n;
		ll res=-1;
		while(l<=r) {
			ll mi=(l+r)/2;
			ll v=ev(mi*m[i], i);
			if(v<n) l=mi+1;
			else if(v>n) r=mi-1;
			else {
				res=mi;
				break;
			}
		}
		if(res!=-1) {
			ans=i+1;
			break;
		}
	}

	printf("Case #%lld: %lld\n", q, ans);
}

	return 0;
}
