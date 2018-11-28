#include <bits/stdc++.h>
using namespace std ;


int main ( )
{
    int t ; cin >> t ; 
    long long n ; 
    for ( int i = 1 ; i <= t ; i++ )
    {
        cin >> n ; 
        //cout << endl << n << endl;
        printf("Case #%d: ",i);
        if ( n == 0 )
        {
            printf("INSOMNIA\n") ;
        }
        else
        {
            set<long long> s ; 
            long long j = 0LL ; 
            while ( s.size() < 10 )
            {
                j++;
                long long aux = n * j ; 

                while ( aux > 0 )
                {
                    s.insert( aux % 10 ) ; 
                    aux /= 10 ; 
                }

            }
            cout << n*j << endl;
        }
        
    }
    return 0 ; 
}