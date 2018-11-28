#include<iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

int main() {
    long test , step = 0 ;
    long *arr;
    long n , i , j , max1=0 , min1 , sum ;
    freopen("in","r",stdin) ;
    freopen("2.out","w",stdout) ;
    cin >> test ;
    while( test-- ) {
        cin >> n ;
        arr = new long[n];
        for(i = 0 ; i < n ; i++) {
            cin >> arr[i] ;
            max1 = max(max1,arr[i]) ;
        }
        min1 = max1 ;
        for(i = 1 ; i <= max1 ; i++) {
            sum = i ;
            for(j = 0 ; j < n ; j++) {
                if( arr[j] > i ) {
                    if( arr[j]%i == 0 )
                        sum += (arr[j]/i-1) ;
                    else
                        sum += (arr[j]/i) ;
                }
            }
            min1 = min(min1,sum) ;
        }
        cout << "Case #"<<++step<<": "<< min1 << "\n" ;
    }
    return 0 ;
}
