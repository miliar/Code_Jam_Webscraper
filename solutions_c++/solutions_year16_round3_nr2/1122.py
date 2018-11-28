#include <bits/stdc++.h>

#define sf scanf
#define pf printf
#define pb push_back
#define mp make_pair
#define PI ( acos(-1.0) )
#define mod 1000000007
#define maxn 500005
#define DBG pf("Hi\n")
#define loop(i,n) for(i=1 ; i<=n ; i++)

using namespace std ;

typedef long long int i64 ;

char s[100][100] ;

bool checkbit(i64 n, i64 pos) { return (bool)(n&(1<<pos)) ;  }

int main()
{
    i64 i , j , k , l , m , n , t=1 , tc , b , sum ;

    freopen("B.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;

    sf("%lld",&tc) ;

    while(t<=tc)
    {
        sf("%lld %lld",&b,&m) ;
        for(i=0 ; i<b ; i++)
        {
            for(j=0 ; j<b ; j++) s[i][j] = '0' ;
            s[i][j] = '\0' ;
        }

        for(i=1 ; i<b ; i++){
            for(j=i+1 ; j<b ; j++) s[i][j] = '1' ;
        }

        pf("Case #%lld: ",t++) ;
        if( (1LL<<(b-2))<m ) pf("IMPOSSIBLE\n") ;

        else{
            pf("POSSIBLE\n") ;

            s[0][b-1] = '1' ;
            m-- ;

            for(i=b-2,j=0 ; i>=1 ; i--,j++)
            {
                if( checkbit(m,j)==1 ) s[0][i] = '1' ;
            }
            for(i=0 ; i<b; i++) pf("%s\n",s[i]) ;
        }
    }

    return 0 ;
}
