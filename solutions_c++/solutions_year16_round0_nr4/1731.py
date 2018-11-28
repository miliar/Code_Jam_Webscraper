#include <bits/stdc++.h>

#define READ(x)		freopen(x,"r",stdin)
#define WRITE(x)	freopen(x,"w",stdout)

#define REP(i, n)	for(int i=0;i<n;i++)
#define REPN(i,n)	for(int i=1;i<=n;i++)
#define SET(i,n)	memset(i,n,sizeof(i))

#define MAX			100050
#define INF			1e9
#define EPS			1e-9
#define MOD			1000000007

#define pb			push_back
#define cl			clear

using namespace std;

typedef long long 		ll;
typedef unsigned long long	ull;
typedef double			db;

ll n, k, c;

ll power(ll x, ll y){
    ll ret = 1;
    REP(i, y) ret *= x;
    return ret;
}

int main(){
    READ("D-small-attempt0.in");
    WRITE("D-small-attempt0.out");
    ll tc, cas=1;
    scanf("%lld", &tc);
    while(tc--){
        scanf("%lld %lld %lld", &n, &c, &k);
        ll x = power(n, c);
        ll f = x / k, cur = 1;
        printf("Case #%lld:", cas++);
        REP(i, k){
            assert(cur <= x);
            printf(" %lld", cur);
            cur += f;
        }
        printf("\n");
    }

	return 0;
}
