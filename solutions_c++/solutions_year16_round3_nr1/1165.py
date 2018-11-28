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

int a[30] ;

int main()
{
    int i , j , k , l , m , n , t=1 , tc , id1 , id2,sum ;

    freopen("inp.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;

    sf("%d",&tc) ;

    while(t<=tc)
    {
        sf("%d",&n) ;

        for(i=1 ; i<=n ; i++) sf("%d",&a[i]) ;
        for( i=1 , sum=0 ; i<=n ; i++ ) sum+= a[i] ;
        for(i=1,id1=1 ; i<=n ; i++)
        {
            if( a[i]>a[id1] ) id1 = i ;
        }

        pf("Case #%d:",t++) ;

        if(sum%2==1){
            pf(" %c",id1+'A'-1) ;
            sum-- ;
            a[id1]-- ;
        }

        for(  ; sum!=0 ;  )
        {
            id1 = 1 ; id2 = 2 ;
            if( a[id2]>a[id1] ){
                id1 = 2 ; id2 = 1 ;
            }
            for(j=3 ; j<=n ; j++)
            {
                if( a[j]>a[id2] ) id2 = j ;
                if( a[id2]>a[id1] ) {
                    k = id1 ;
                    id1 = id2 ;
                    id2 = k ;
                }

                }
                 if( a[id1]>a[id2] )
                {
                    a[id1]-=2 ;

                    pf(" %c%c",id1+'A'-1,id1+'A'-1) ;

                }
                else{
                    a[id1]-- ; a[id2]-- ;

                    pf(" %c%c",id1+'A'-1,id2+'A'-1) ;
            }
            sum -= 2 ;
        }
        pf("\n") ;

    }


    return 0 ;
}
