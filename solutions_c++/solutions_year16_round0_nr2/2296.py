#include <bits/stdc++.h>

#define sf scanf
#define pf printf
#define INF 2000000000
#define PI (acos(-1.0))
#define mp make_pair
#define pb push_back
#define i64 long long int

using namespace std ;

char s[105] ;

int main()
{
    int i , j , k , l , m  , n , fl ,t=1 , tc , ans ;

    freopen( "B-large.in" ,"r" , stdin ) ;
    freopen( "out.txt" ,"w" , stdout ) ;

    sf("%lld",&tc) ;

    while(t<=tc)
    {
        sf("%s",s) ;
        l = strlen(s) ;

        for( i=l-1,fl=0,ans=0 ; i>=0 ; i-- )
        {
            if(s[i]!=s[i+1]){
                if(s[i]=='+' && fl==1 ) ans++ ;
                if(s[i]=='-'){
                    ans++ ;
                    fl = 1 ;
                }
            }
        }
        pf("Case #%d: %d\n",t++ ,ans) ;
    }

    return 0 ;
}
