#include <bits/stdc++.h>

#define pf printf
#define sf scanf
#define INF 2000000000000000000
#define pi (acos(-1.0))
#define i64 long long int
#define DBG printf("Hi\n")
#define loop for(i =1 ; i<=n; i++)
#define mp make_pair
#define pb push_back
#define mod 1000000007
#define maxn 300005
#define ff first
#define sc second
#define pii pair<i64,i64>

using namespace std ;

int cnt[2505] ;
// int [105][55] ;
vector <int> v ;

int main()
{
    int i , j , k , l , m , n , t=1, tc ;

    freopen( "Bl.in", "r" , stdin ) ;
    freopen( "out.txt" ,  "w" , stdout ) ;

    sf("%d",&tc) ;

    while(t<=tc)
    {
        memset(cnt,0,sizeof(cnt)) ;

        sf("%d",&n) ;

        for(i=1 ; i<=2*n-1 ; i++)
        {
            for(j=1 ; j<=n ; j++)
            {
                sf("%d",&k) ;
                cnt[k]++ ;
            }
        }

        for(i=1; i<=2500 ; i++)
        {
            if(cnt[i]%2==1) v.pb(i) ;
        }

        sort(v.begin() , v.end()) ;

        pf("Case #%d:",t++) ;
        for(i=0 ; i<v.size() ; i++) pf(" %d",v[i]) ;
        pf("\n") ;
        v.clear() ;
    }


    return 0 ;
}
