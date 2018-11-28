#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int t;
ll k, c, s;

ll pow(ll b, ll e)
{
	ll r=1;
	while(e) {
		if(e&1) r*=b;
		e>>=1;
		b*=b;
	}
	return r;
}

ll take(ll cur, ll lev=1)
{
	if(lev==c) return cur;
	else return (cur-1)*pow(k, c-lev)+take(min(k, cur+1), lev+1);
}

int main()
{
	scanf("%d", &t);
	for(int q=1; q<=t; q++) {
		scanf("%lld%lld%lld", &k, &c, &s);
		printf("Case #%d:", q);
		if(s<(k%min(k, c)==0 ? k/min(k, c) : k/min(k, c)+1)) {
			printf(" IMPOSSIBLE\n");
			continue;
		}
		for(ll i=1; i<=k; i+=c) printf(" %lld", take(i));
		printf("\n");
	}

	return 0;
}
