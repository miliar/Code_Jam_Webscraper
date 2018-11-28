
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std ;

typedef unsigned long long ll ;

ll dat[110] ;

int main()
{
    int T ;
    scanf("%d", &T) ;
    for(int time = 1 ; time <= T ; time++){
        printf("Case #%d: ", time) ;
        ll A ;
        int N ;
        scanf("%lld%d", &A, &N) ;
        for(int i = 0 ; i != N ; i++)
            scanf("%lld", dat+i) ;
        sort(dat, dat+N) ;
        int ans = 0 ;
        int now = 0 ;
        while(now != N){
            int loc = lower_bound(dat, dat+N, A)-dat ;
            //printf("loc = %d\tA = %lld\tnow = %d\n", loc, A, now) ;
            //getchar() ;
            if(loc == N)
                break ;
            if(loc == now){
                //puts("loc == now") ;
                int want = N-now ;
                ll pw = 1, ds = 0 ;
                int i ;
                for(i = 1 ; i != want ; i++){
                    ds += pw ;
                    pw *= 2 ;
                    //printf("now prodct: %lld >? %lld\n", pw*A-ds, dat[now]) ;
                    if(pw*A-ds > dat[now])
                        break ;
                }
                if(A != 1 && i != want)   A = pw*A-ds ;
                else{
                    ans += want ;
                    //puts("cancel all") ;
                    break ;
                }
                ans += i ;
                //printf("pow %d time\n", i) ;
                continue ;
            }
            for(int i = now ; i != loc ; i++)
                A += dat[i] ;
            now = loc ;
        }
        printf("%d\n", ans) ;
    }
    return 0 ;
}



