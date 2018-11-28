#include <cstdio>

using namespace std;
#define ll long long
int i, j, T, t_case;

ll r, t;

ll calc(ll value) {
    
    if((10e18 - 2 * r * value) / value < (2 * value - 1)) return -1;
    return 2 * r * value + (2 * value - 1) * value;
}

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    scanf("%d",&T);

    for(t_case = 1; t_case <= T; ++t_case) {
        
        scanf("%lld %lld",&r,&t);

        ll left = 0, right = t / (2 * r);
        ll ans = 0;

        for(; left <= right;) {
            ll mid = (left + right) >> 1;
            if(calc(mid) != -1 && calc(mid) <= t) {
                ans = mid;
                left = mid + 1;
            }
            else right = mid - 1;
        }

        printf("Case #%d: %lld\n", t_case, ans);
    }

    return 0;
}   
