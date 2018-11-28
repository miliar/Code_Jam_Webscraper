#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std ;

const int MAXN = 100000 + 10 ;

struct Fac {
    double money ;
    double time ;
}f[MAXN];


int main() {

    freopen("B-large.in" , "r" , stdin) ;
    freopen("B.out" , "w" , stdout ) ;

    int step = 0 ;
    int T ; scanf("%d" , &T ) ;
    while( T -- ) {

        double C , F , X ; scanf("%lf%lf%lf" , &C , &F , &X ) ;

        int MAX_F_NUM = (int)X + 1 ;

        f[0].money = 2.0 ;
        f[0].time = 0.0 ;
        for( int i = 1 ; i <= MAX_F_NUM ; i ++ ) {
            f[i].money = F + f[i-1].money ;
            f[i].time = f[i-1].time + C / f[i-1].money ;
        }

        double ans = X ;
        for( int i = 0 ; i <= MAX_F_NUM ; i ++ ) {
            ans = min( ans , X / f[i].money + f[i].time ) ;
        }

        printf("Case #%d: %.7lf\n" , ++ step , ans ) ;
    }


    return 0 ;
}
