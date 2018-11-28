#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <deque>
using namespace std;

#define F first
#define S second
#define MP make_pair
#define PB push_back
#define rep( i , a , b )  for( int i = (a) ;   i <= (b) ; ++i)
#define foreach(c , itr) for(__typeof((c).begin()) itr = (c).begin(); itr != (c).end(); ++itr)
#define SZ(x) (int)x.size()
#define LEN(x) (int)x.length()

typedef long long int64; 
int main (){ 
    int T ; 
    
    freopen("a.in","r",stdin); 
    freopen("a.out","w",stdout); 
    cin >> T ; 
    for(int Cas = 1 ; Cas <= T ; ++Cas){ 
        int64 r, t ; 
        cin >> r >> t ; 
        
        int64 ll = 0 , rr = 1000000000LL*1000000000LL ;  
        while( ll < rr ){  
            
            int64 mid = ( ll + rr+1 ) >> 1 ;
            double x= 1.*mid*(4.*mid+4.*r-2) / 2 ; 
            if( x < t|| fabs(x-t) < 1e-9 )  ll = mid ; 
            else {
               rr= mid-1 ;
            } 
        }  
       // int64 x = r ;     
         
        cout << "Case #"<<Cas <<": "<< ll << endl ;  
    }
    return 0; 
}

