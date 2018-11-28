#include <bits/stdc++.h>

#define READ(x)		freopen(x,"r",stdin)
#define WRITE(x)	freopen(x,"w",stdout)

#define REP(i, n)	for(ll i=0;i<n;i++)
#define REPN(i,n)	for(ll i=1;i<=n;i++)
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

int main(){
    READ("A-large.in");
    WRITE("A-large.out");
    ll tc, cas=1, n;
    scanf("%lld", &tc);
    while(tc--){
        scanf("%lld", &n);
        int F[15];
        SET(F, 0);
        ll ret = -INF;
        REPN(i, 100000){
            ll k = n * i;
            if(k == 0) F[0] = 1;
            else{
                while(k != 0){
                    F[k % 10] |= 1;
                    k /= 10;
                }
            }
            int f = 1;
            REP(i, 10) f &= F[i];
            if(f){
                ret = n*i;
                break;
            }
        }
        if(ret == -INF) printf("Case #%lld: INSOMNIA\n", cas++);
        else printf("Case #%lld: %lld\n", cas++, ret);
    }
	return 0;
}
