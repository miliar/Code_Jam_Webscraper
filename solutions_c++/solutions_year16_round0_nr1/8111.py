#include <cstdio>
#include <iostream>
using namespace std ;
void work() {
     long long n ;     
     cin >> n ;
     if ( n == 0 )
        cout << "INSOMNIA" << endl;
     else {
         int ans = 0 ;
         long long now = 0 ;
         long long mask = 0 ;
         const long long aim = (1<<10) - 1 ;
         for ( int i = 1 ; ; ++i ) {

               now += n;
               long long t = now ;
               while ( t > 0 ) {
                     mask |= ( 1 << (t%10) );
                     t /= 10 ;
               }
               if ( mask == aim ) {
                  cout << now << endl ;
                  break;
               }
         }
    }

}

int main() {
    
    int T ;
    cin >> T ;
    for ( int cases = 1 ; cases <= T ; ++cases ) {
        cout << "Case #" << cases << ": "; 
        work();
    }
    
    return 0;
} 
