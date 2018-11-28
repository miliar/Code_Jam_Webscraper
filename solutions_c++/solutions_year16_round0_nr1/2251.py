#include <bits/stdc++.h>

#define sf scanf
#define pf printf
#define INF 2000000000
#define PI (acos(-1.0))
#define mp make_pair
#define pb push_back
#define i64 long long int

using namespace std ;

bool fl[15] ;

int main()
{
    i64 i , j , k  , l , m , n , t=1 , tc , cnt , ret ;

    freopen( "large.in" ,"r" ,stdin ) ;
    freopen( "out.txt" ,"w" ,stdout ) ;

    sf("%lld",&tc) ;

    while(t<=tc)
    {
        sf("%lld",&n) ;

        pf("Case #%lld: ",t++) ;

        if(n==0)
        {
            pf("INSOMNIA\n") ;
            continue ;
        }
        memset(fl,0,sizeof(fl)) ;
        cnt = 0 ; i = 1 ;
        while(cnt<10)
        {
            ret = n*i ;
            while(ret!=0)
            {
                m = ret%10 ;
                if(!fl[m]){
                    fl[m] = 1 ;
                    cnt++ ;
                }
                ret = ret/10 ;
            }
            i++ ;
        }
        pf("%lld\n",n*(i-1) ) ;
     //   pf("%lld\n",i-1) ;
    }

    return 0 ;
}
