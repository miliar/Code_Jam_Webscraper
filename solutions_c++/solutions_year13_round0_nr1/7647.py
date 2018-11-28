#include<iostream>
#include<fstream>

using namespace std ;


int main()
{
    
    freopen( "in.txt" , "rt" , stdin ) ;
    freopen( "out.txt" , "wt" , stdout ) ;
    
    int n ;
    char s[4][4] ;
    int  x  , o  ;
    bool nc , d = 0 , t = 0 , flagx  , flago ;
    cin >> n ;
    for ( int k = 1 ; k <= n ; k++ )
    {
        flagx = 0 ; flago = 0 ; nc = 0 ;
        
        for ( int i=0 ; i < 4 ; i++ )
            for ( int j=0 ; j < 4 ; j++ )
                cin >> s[i][j] ;
        
        for ( int i=0 ; i<4 ; i++ )
        {
            x = 0 ; o = 0 ; t = 0 ; d = 0 ;
            for ( int j = 0 ; j<4 ; j++ )
            {
                if ( s[i][j] == 'X' )
                    x++ ;
                else if ( s[i][j] == 'O' )
                    o++ ;
                else if ( s[i][j] == 'T' )
                    t = 1 ;
                else if ( s[i][j] == '.' )
                    d = 1 ;
                //cout << s[i][j] << " , " ; 
            }
            //cout << endl ;
            
            if ( t+x == 4 )
                flagx = 1 ;
            else if ( t+o == 4 )
                flago = 1 ;
            if ( d != 0  )
                nc = 1 ;  
            //cout << "result: " << "x : " << flagx <<  " , O: " << flago << " , not com : " <<  nc << endl ;    
        }
        
        //cout << "__________________________________________\n" ;
        for ( int i=0 ; i<4 ; i++ )
        {
            x = 0 ; o = 0 ; t = 0 ; d = 0 ;
            for ( int j = 0 ; j<4 ; j++ )
            {
                if ( s[j][i] == 'X' )
                    x++ ;
                else if ( s[j][i] == 'O' )
                    o++ ;
                else if ( s[j][i] == 'T' )
                    t = 1 ;
                else if ( s[j][i] == '.' )
                    d = 1  ;
                //cout << s[j][i] << " , " ;
            }
            //cout << endl ;
            if ( t+x == 4 )
                flagx = 1 ;
            else if ( t+o == 4 )
                flago = 1 ;
            if ( d != 0 )
                nc = 1 ;   
            //cout << "result: " << "x : " << flagx <<  " , O: " << flago << " , not com : " <<  nc << endl ;    
        } 
       
        x = 0 ; o = 0 ; t = 0 ;       
        for ( int i = 0  ; i < 4 ; i++  )
        {
            if ( s[i][i] == 'X' )
                x++ ;
            else if ( s[i][i] == 'O' )
                o++ ;
            else if ( s[i][i] == 'T' )
                t = 1  ; 
        }
        if ( x+t == 4 )
            flagx = 1 ;
        else if ( o+t == 4 )
            flago = 1 ;
            
        x = 0 ; o = 0 ; t = 0 ; 
        for ( int i=0  ; i < 4 ; i++ )
        {
            if ( s[i][3-i] == 'X' )
                x++ ;
            else if ( s[i][3-i] == 'O' )
                o++ ;
            else if ( s[i][3-i]  == 'T' )
                t = 1  ;
        }
        if ( x+t == 4 )
            flagx = 1 ;
        else if ( o+t == 4 )
            flago = 1 ;
        
        if (  flagx == 1 && flago == 1 )
            cout << "Case #" << k << ": Draw" << endl ;
        else if ( flagx == 1 )
            cout << "Case #" << k << ": X won" << endl ; 
        else if ( flago == 1 )
            cout << "Case #" << k << ": O won" << endl ; 
        else if ( nc == 0 )
            cout << "Case #" << k << ": Draw" << endl ;
        else
            cout << "Case #" << k << ": Game has not completed" << endl ;
    }   
   
    return 0 ;
}


