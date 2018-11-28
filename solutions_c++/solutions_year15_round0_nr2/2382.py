#include <cstdio>
#include <cstring>
#include <fstream>
#include <algorithm>

using namespace std ;

int a[1200] ;

int main() {
        int t , step = 0 ;
        int n , i , j , max1 , min1 , sum ;
        ifstream in("bl.in");
        ofstream out("bl.out");
        in>>t;
        while( t-- ) {
            in>>n;
            for(i = 0 ; i < n ; i++) {
                in>>a[i];
                max1 = max(max1,a[i]) ;
            }
            min1 = max1 ;
            for(i = 1 ; i <= max1 ; i++) {
                sum = i ;
                for(j = 0 ; j < n ; j++) {
                    if( a[j] > i ) {
                        if( a[j]%i == 0 )
                            sum += (a[j]/i-1) ;
                        else
                            sum += (a[j]/i) ;
                    }
                }
                min1 = min(min1,sum) ;
            }
            out<<"Case #"<<++step<<": "<<min1<<endl;

        }
        return 0 ;
    }
