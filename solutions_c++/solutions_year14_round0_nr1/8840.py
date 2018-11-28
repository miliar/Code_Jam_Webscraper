#include<iostream>
#include<fstream>

using namespace std ;


int main()
{
    
    freopen( "in.txt" , "rt" , stdin ) ;
    freopen( "out.txt" , "wt" , stdout ) ;
    
    int t , k = 1 ;
    cin >> t ;
    while ( k <= t )
    {
        int g[4][4] ;
        int c , y = 0 , f ;
        cin >> c ;
        for ( int i=0 ; i<4 ; i++ )
            for ( int j=0 ; j<4 ; j++ )
                cin >> g[i][j] ;
        int S[4] ;
        for ( int i=0 ; i<4 ; i++ )
            S[i] = g[c-1][i] ;
        
        cin >> c ;
        for ( int i=0 ; i<4 ; i++ )
            for ( int j=0 ; j<4 ; j++ )
                cin >> g[i][j] ;
        for ( int i=0 ; i<4 ; i++ )
            for ( int j=0 ; j<4 ; j++ )
                if ( S[i] == g[c-1][j] )
                { 
                    f = S[i] ;
                    y++ ;
                }
        
        if (  y == 1 )
            cout << "Case #" << k << ": " << f << endl ;
        else if ( y > 1 )
            cout << "Case #" << k << ": Bad magician!" << endl ; 
        else 
            cout << "Case #" << k << ": Volunteer cheated!" << endl ; 
            
        k++ ;
    }   
   
    return 0 ;
}


