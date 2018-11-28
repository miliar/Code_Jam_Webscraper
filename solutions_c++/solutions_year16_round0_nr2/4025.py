#include <bits/stdc++.h>
using namespace std ;

bool dis ( bool plus ,  char c )
{
    if ( c == '+' and plus ) return false ; 
    if ( c == '-' and !plus ) return false ; 
    return true ; 
}

int solve ( string s )
{
    int ans = 0 ; 
    bool plus = true ; 
    for ( int i = s.size() - 1 ; i >= 0 ; i-- )
    {
        char c = s[ i ] ; 

        if ( dis ( plus , c ) )
        {
            ans++;
            plus = !plus ; 
        }
    }

    return ans ; 
}

int main ( )
{
    int T; cin >> T ; 
    string s ; 
    for ( int i = 1 ; i <= T ; i++ )
    {
        cin >> s ; 
        printf("Case #%d: %d\n", i , solve ( s ) ) ; 
    }
    return 0 ; 
}