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

int main()
{_
    int K , r;
    int a[ 4 ];
    cin >> K;
    forn( i , K )
    {
        set< int > ini;
        set< int > sec;
        cin >> r;
        forn(j,4)
        {
            forn( k , 4 ) cin >> a[ k ];
            if( j + 1 == r )
            {
                forn( k , 4 )
                {
                    ini.insert( a[ k ] );
                }                    
            }
        }
        cin >> r;
        forn(j,4)
        {
            forn( k , 4 ) cin >> a[ k ];
            if( j + 1 == r )
            {
                forn( k , 4 )
                {
                    if( ini.find( a[ k ] ) != ini.end() )
                    {
                        sec.insert( a[ k ] );
                    }
                }
            }
        }
        if( sec.size() > 1 )
            cout << "Case #" <<  i+1 << ": "<< "Bad magician!" << endl;
        else if( sec.size() == 0 )
            cout << "Case #" <<  i+1 << ": "<< "Volunteer cheated!" << endl;
        else
            cout << "Case #" <<  i+1 << ": "<< *sec.begin() << endl;
    }
	return 0;
}
