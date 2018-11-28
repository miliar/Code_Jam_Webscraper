/** Libraries **/
#include "bits/stdc++.h"

/** System **/
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

#if ( WIN32 || __WIN32_ )
   #define lld I64d
#endif

/** Utilities **/
#define forit(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define fori(i,a,b) for( int i = (int)(a); i < (int)(b); i++ )
#define forn(i,n) fori(i,0,n)
#define zeros(a) memset(a,0,sizeof(a))
#define null(a) memset(a,-1,sizeof(a))
#define all(a) (a).begin() , (a).end()
#define sqr(a) ((a)*(a))
#define sz(a) (a).size()
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pii 2*acos(0.0)

/** Name spaces **/
using namespace std;

/** Types **/
typedef long long int i64;
typedef pair< int,int > ii;
typedef map< string , int > msi;

double solve( double Now , double Goal , double Speed , double inc , double cookies)
{
    double ans = 0;
    while( (Goal / Speed) > ( cookies / Speed + Goal /( Speed + inc ) ) )
    {
        ans += cookies / Speed ;
        Speed += inc;
    }
    ans += (Goal / Speed);
    return ans;
}

int main()
{_
    int T , S;   
    double C , F , X;
    
    cin >> T;
    
    forn( ca , T )
    {
        cin >> C >> F >> X;
        printf("Case #%d: %.7lf\n",(ca+1),solve( (0.0) , X , (2.0) , F , C ));      
    }
    
	return 0;
}
