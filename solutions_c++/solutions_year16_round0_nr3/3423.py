#include <bits/stdc++.h>
using namespace std ;

long long toD ( int base , string s )
{
    long long ans = 0 ; 
    for ( int i = 0; i < s.size() ; i++)
    {
        ans *= base ; 
        ans += ( s [ i ] - '0' ) ;
    }
    return ans ; 
}

string toS ( int num , int N )
{
    string s ; 
    for ( int i = 0 ; i < N ; i++ ) s+= "0" ;
    int i = N-1 ; 
    while ( num > 0 )
    {
        s[ i ] = ( num % 2 == 0 ? '0' : '1' ) ;
        num /= 2 ; 
        i--;
    }
    return s ; 
}

long long getfactor ( long long num )
{
    long long m = min ( num , max ( 2LL , ( long long ) ( sqrt ( num ) + 1.0 ) ) ) ;
    for ( long long  i = 2 ; i < m ; i++ )
    {
        if ( num % i == 0) return i ;
    }
    return -1; 
}

vector<long long> v ;

bool check ( string s )
{
    if ( s[ 0 ] != '1' ) return false ;
    if ( s[ s.size() - 1 ] != '1' ) return false ;

    long long aux , factor ; 
    
    for ( int base = 2 ; base <= 10 ; base++ )
    {
        aux = toD ( base , s ) ; 
        factor = getfactor ( aux ) ; 
        if ( factor != -1 ) v.push_back ( factor ) ;
    }

    if ( v.size() != 9 ) return false ;

    return true ; 
}

int main ( )
{
    int T; cin >> T ; 
    int N , J ; 
    string s ; 
    for ( int i = 1 ; i <= T ; i++ )
    {
        cin >> N >> J ; 
        
        printf("Case #%d:\n",i ) ; 
        int tot = 0 ; 
        for ( int i = 0 ; i < ( 1 << N ) ; i++ )
        {
            s = toS( i , N ) ; 

            v.clear() ; 

            if ( tot < J && check ( s ) )
            {
                cout << s << " " ;

                for ( int i = 0 ; i < 9 ; i++ )
                {
                    cout << v[ i ] << " " ; 
                }
                cout << endl; 
                tot++;
            }
        }
    }
    return 0 ; 
}