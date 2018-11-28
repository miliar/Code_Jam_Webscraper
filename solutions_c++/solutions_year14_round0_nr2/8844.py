#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std ;


int main()
{
    
    freopen( "in.txt" , "rt" , stdin ) ;
    freopen( "out.txt" , "wt" , stdout ) ;
    
    int t , k = 1 ;
    cin >> t ;
    while ( k <= t )
    {
        double c , f , x , z=2 , sum = 0 , w , min ;
        cin >> c >> f >> x ;
        
        min = x / z ;
        
        
        while(1)
        { 
            sum += c/z ;
            z += f ;
            w = x / z ;
            w += sum ;
            if ( min > w )
                min = w ;
            else
                break ;
        }
        cout << fixed << setprecision(7) ;
        cout << "Case #" << k << ": " << min << endl ; 
            
        k++ ;
    }   
   
    return 0 ;
}


