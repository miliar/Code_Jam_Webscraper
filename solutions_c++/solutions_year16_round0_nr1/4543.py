#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define rep(i,n) forn(i,0,n)
#define repe(i,n) for( i = 0; i < (n); i++ )
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>

const int MXN = 100100;
const int MXK = 20;

bool was [10];

void solve(){
    int x;
    scanf("%d", &x);

    if(!x){
        printf("INSOMNIA");
        return;
    }

    rep(i,10){
        was[i] = false;
    }

    ll res = 0;
    for(int qq = 0; qq < 1e8; qq++){
        bool ok = true;
        rep(i,10){
            if(!was[i]) ok = false;
        }
        if(ok){
            printf("%lld", ll(res));
            return;
        }

        res += x;
        int t = res;
        while(t){
            was[t%10] = true;
            t /= 10;
        }
    }

    printf("INSOMNIA");
}

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    rep(i,T){
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }

    return 0;
}
