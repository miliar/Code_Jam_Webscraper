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

char sir [ 1011 ] ;

int main ( void )
{
    int t ;
    cin >> t ;
    FORN ( tests , 1 , t )
    {
        int l ;
        cin >> l ;
        cin >> ( sir ) ;
        int s = sir [ 0 ] - '0' ;
        int add = 0 ;
        FORN ( i , 1 , l ){
            if ( i > s ){
                add = add + i - s ;
                int cate = i - s ;
                s = s + cate ;
            }
            s = s + sir [ i ] - '0' ;
        }
        cout << "Case #" << tests << ": " << add << '\n' ;

    }
    return 0;
}
