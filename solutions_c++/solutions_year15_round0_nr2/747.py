#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small.out","w",stdout);
    freopen("B-large.in","r",stdin);
    freopen("B-Large.out","w",stdout);
    int t, T, ans, N, tmp, i, j;
    int n[1005];
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; t ++ ) {
        ans = 0;

        scanf("%d",&N);
        for ( i = 0 ; i < N ; i ++ ) {
            scanf("%d",&n[i]);
            ans = max(ans,n[i]);
        }

        for ( i = ans-1 ; i >= 1 ; i -- ) {
            for ( tmp = i, j = 0 ; j < N ; j ++ ) {
                    tmp += ( n[j]%i == 0 ? (n[j]/i) - 1 : n[j]/i );
            }
            ans = min(ans, tmp);
        }

        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
