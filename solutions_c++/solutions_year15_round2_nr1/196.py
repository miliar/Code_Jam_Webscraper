#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

typedef long long LL;

LL a[15], ten[15], N;

void init() {
    int i;
    for ( ten[0] = 1, i = 1 ; i < 15 ; i ++ ) {
        ten[i] = ten[i-1]*10;
    }

    for ( a[1] = 1, a[2] = 10, i = 2 ; i <= 13 ; i ++ ) {
        if ( i%2 == 0 ) {
            a[i+1] = a[i]+(ten[i/2]-1)+1+(ten[i/2]-1);
        }
        else {
            a[i+1] = a[i]+(ten[i/2]-1)+1+(ten[i/2+1]-1);
        }
    }

    /*for ( i = 0 ; i < 15 ; i ++ ) {
        printf("%lld %lld\n",ten[i],a[i+1]);
    }*/
}

LL revers ( LL n ) {
    int i, deg = (int)log10(n) + 1;
    LL tmp = 0;
    for ( i = 0 ; i < deg ; i ++ ) {
        tmp = tmp * 10;
        tmp = tmp + (n/ten[i])%10;
    }
    return tmp;

}


int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t, T, deg;
    LL ans, ans2, ans3, p, q, N2;
    init();
    scanf("%d",&T);

    for ( t = 1 ; t <= T ; t ++ ) {
        scanf("%lld",&N);
        if ( N <= 10 ) {
                printf("Case #%d: %lld\n", t, N);
                continue;
        }
        if ( N%10 == 0 ) {
            ans = 1;
            N--;
        }
        else ans = 0;

        N2 = N;
        deg = (int)log10(N) + 1;
        ans = ans + a[deg];
        ans3 = ans2 = ans;
        p = N/ten[deg/2];
        q = N%ten[deg/2];
        p = revers(p);
        ans = ans + p + 1 + q - 1;
        ans2 = ans2 + 1;
        N = revers(N);
        p = N/ten[deg/2];
        q = N%ten[deg/2];
        p = revers(p);
        ans2 = ans2 + p + 1 + q - 1;

        printf("Case #%d: %lld\n",t,min(min(ans,ans2),ans3+N2-ten[deg-1]));
    }
}
