#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

typedef long long LL;

LL M[1005], B, N;


LL bs() {
    LL l, r, mid, cur, div, mx, ans, i;
    l = 0; mx = r = 1000000000000000;
    while(1) {
        mid = (l+r)/2;

        for ( div = cur = i = 0 ; i < B ; i ++ ) {
            cur += mid/M[i] + 1;
            if ( mid%M[i] == 0 ) div ++;
            if ( cur > mx ) break;
        }
        if ( i != B ) {
            r = mid;
        }
        else {
            if ( div == 0 ) {
                if ( cur >= N )
                    r = mid;
                else
                    l = mid + 1;
            }
            else {
                if ( N < cur-div+1 )
                    r = mid;
                else if ( N > cur )
                    l = mid + 1;
                else
                {
                    for ( ans = cur-div+1, i = 0 ; i < B ; i ++ ) {
                        if ( mid%M[i] == 0 ) {
                            if ( ans == N ) {
                                return (i+1);
                            }
                            ans ++;
                        }
                    }
                }
            }
        }
        //printf("cur = %lld, div = %lld, mid = %lld\n",cur,div, mid);
        //system("pause");
    }
}



int main() {
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("B-small-attempt1.out","w",stdout);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t, T, i;

    scanf("%d",&T);

    for ( t = 1 ; t <= T ; t ++ ) {
        scanf("%lld %lld",&B,&N);

        for ( i = 0 ; i < B ; i ++ ) {
            scanf("%lld",&M[i]);
        }

        printf("Case #%d: %lld\n",t,bs());


    }
    //system("pause");
    return 0;
}
