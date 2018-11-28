#include<bits/stdc++.h>
using namespace std ;
long long mn ;

int main() {
    freopen("B-large.in","r",stdin) ;
    freopen("B-large.out","w",stdout) ;
    int cases , caseno =1 ;
    scanf("%d",&cases );
    while( cases -- ) {
        int D , P[10000+1] ;
        cin >> D ;
        int M = -(1<<30) ;
        for( int i = 0 ; i  < D ; i++ ) {
            cin >> P[i] ;
            M = max( P[i] , M ) ;
        }
        long long mn = 1<<30 ;
        for( int i = 1 ; i<= M ; i++ ){
            long long time = i ;
            for( int j = 0 ;j < D ; j++ ){
                if( P[j] > i ){
                    int tmp = P[j]-i; ;
                    time += int(ceil(double(tmp)/double(i))) ;
                }
            }
            mn = min( mn , time ) ;
        }
        cout << "Case #" << caseno++ << ": " <<mn<< endl ;

    }
}
