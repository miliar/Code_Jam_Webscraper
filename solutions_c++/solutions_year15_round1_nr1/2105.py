#include<bits/stdc++.h>
using namespace std ;

int main() {
    freopen("A-large.in","r",stdin) ;
    freopen("A-large.out","w",stdout) ;
    long long cases , caseno =1 ;
    cin >> cases ;
    while( cases -- ) {
        long long n ;
        cin >> n ;
        long long arr[n] ;
        for( long long i = 0 ; i < n ; i ++ )cin >> arr[i] ;
        long long eat1 = 0 , eat2 = 0 ;
        for( long long i = 1 ; i < n ; i++ ) {
            if( arr[i-1]-arr[i] >= 0 ) {
                eat1 += arr[i-1]-arr[i] ;
            }
        }
        long long rt = -1 ;
        for(int i = 1 ;i < n ; i++ ){
            rt = max( arr[i-1] - arr[i] , rt ) ;
        }
        long long tot = 0 ;
        for( long long i = 0 ; i < n-1 ; i++ ) {
            if( arr[i] > rt )eat2 += rt ;
            else eat2 += arr[i] ;
        }
        cout << "Case #" << caseno++ << ": " << eat1 << " " << eat2 << endl ;
    }
    return 0 ;
}
