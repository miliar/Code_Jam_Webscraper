#include <cstdio>
#define ll long long
const int LIM = 20 * 1000 * 1000;
using namespace std;

ll list[100 * 1000];

inline bool is_pal(ll x) {
    
    ll aux = x, mirr = 0;

    for(; aux ;) {
        mirr = mirr * 10 + aux % 10;
        aux /= 10;
    }

    return (mirr == x);
}

int main() {
    
    int i, t;
    freopen("fair.in","r",stdin);
    freopen("fair.out","w",stdout);

    for(i = 1; i <= LIM; ++i) 
        if(is_pal(1LL * i * i) && is_pal(i)) 
            list[++list[0]] = 1LL * i * i;

    scanf("%d",&t);
    
    for(int t_case = 1; t_case <= t; ++t_case) {

        int ans = 0;
        ll a, b;
        scanf("%lld %lld",&a,&b);

        for(i = 1; i <= list[0]; ++i)
            if(list[i] >= a && list[i] <= b)
                ans++;

        printf("Case #%d: %d\n", t_case, ans);
    }

    return 0;
}
