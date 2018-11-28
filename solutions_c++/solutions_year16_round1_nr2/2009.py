#include<bits/stdc++.h>
using namespace std ; 

int main()
{
    int T ; cin >> T ; 

    for ( int l = 1 ; l <= T ; l++ )
    {
        int N ; cin >> N ; 

        int f[ 2505 ] ; 
        memset ( f , 0 , sizeof ( f ) ) ;
        int x ; 

        for ( int i = 0 ; i < 2*N-1 ; i++ )
        {
            for ( int j = 0 ; j < N ; j++ )
            {
                cin >> x ; 
                f[ x ]++;
            }   
        }

        cout << "Case #" << l << ": " ;

        for ( int i = 0 ; i < 2505 ; i++ )
        {
            if ( f[ i ] % 2 == 1 ) cout << i << " " ;
        }
        cout << endl;
    }
    return 0 ; 
}

