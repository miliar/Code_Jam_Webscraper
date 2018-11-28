/*
 * Code by Spiromanul
 */

# include "iostream"
# include "cstring"
# include "vector"
# include "queue"
# include "bitset"
# include "algorithm"
# include "map"
# include "unordered_map"
# include "deque"
# include "string"
# include "iomanip"
# include "cmath"
# include "stack"
# include "cassert"

const char IN [ ] =  "input" ;
const char OUT [ ] = "output" ;
const int MAX = 3333014 ;

# define pb push_back
# define mp make_pair
# define FORN( a , b , c ) for ( int a = b ; a <= c ; ++ a )
# define FORNBACK( a , b , c ) for ( int a = b ; a >= c ; -- a )

using namespace std ;

//ifstream cin ( IN ) ;
//ofstream cout ( OUT ) ;

int v [ 8700 ] , cate , sol ;

int main( void )
{
    int t ;
    cin >> t ;
    FORN ( tests , 1 , t )
    {
        int n ;
        cin >> n ;
        FORN ( i , 1 , n )
            cin >> v [ i ] ;
        int sol = 1 << 30 ;
        FORN ( nespeciale , 1 , 1000 )
        {
            int local = nespeciale ;
            FORN ( i , 1 , n )
            {
                  if ( v [ i ] % nespeciale != 0 )
                        local = local + v [ i ] /nespeciale ;
                  else local = local + v [ i ] /nespeciale - 1 ;
            }
            sol = min ( sol , local ) ;
        }        cout << "Case #" << tests << ": " << sol << '\n' ;
    }
    return 0;
}
