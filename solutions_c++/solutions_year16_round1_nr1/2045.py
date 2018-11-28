#include<bits/stdc++.h>
using namespace std ; 

int main()
{
    int T ; cin >> T ; 
    string s ; 
    for ( int i = 1 ; i <= T ; i++ )
    {
        list<char> l ; 
        cin >> s ; 
        l.push_back ( s[ 0 ] ) ;

        for ( int j = 1 ; j < s.size() ; j++ )
        {
            if ( l.back() >= s[ j ] )
            {
                l.push_back ( s[ j ] ) ;
            }
            else if ( l.front() <= s[ j ] )
            {
                l.push_front( s[ j ] ) ; 
            }
            else
            {
                l.push_back( s[ j ] ) ;
            }
        }
        cout << "Case #" << i << ": " ;
        for ( list<char>::iterator it=l.begin(); it!=l.end(); ++it) cout << *it;
        cout << endl;
    }
    return 0 ; 
}

