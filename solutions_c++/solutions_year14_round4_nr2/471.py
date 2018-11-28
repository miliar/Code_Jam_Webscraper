#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std ;

const int MAXN = 1009 ;

int N , MAXi , MAX ;
int L[MAXN] , R[MAXN] , Lsum[MAXN] , Rsum[MAXN] , A[MAXN] ;

void Init() {
    cin >> N ;
    for ( int i = 1 ; i <= N ; i ++ ) cin >> A[i] ;
//    MAXi = 1 ;
//    for ( int i = 2 ; i <= N ; i ++ ) if ( A[i] > A[MAXi] ) MAXi = i ;
//    MAX = A[MAXi] ;
//    for ( int i = MAXi ; i < N ; i ++ ) A[i] = A[i+1] ;
//    N -- ;
    
    L[1] = 0 ;
    for ( int i = 2 ; i <= N ; i ++ ) {
        L[i] = 0 ;
        for ( int j = 1 ; j < i ; j ++ ) if ( A[i] < A[j] ) L[i] ++ ;
    }
    R[N] = 0 ;
    for ( int i = N-1 ; i >= 1 ; i -- ) {
        R[i] = 0 ;
        for ( int j = N ; j > i ; j -- ) if ( A[i] < A[j] ) R[i] ++ ;
    }
    
    //cout << MAXi << "\n" ;
    //for ( int i = 1 ; i <= N ; i ++ ) cout << L[i] << "," << R[i] << "\n" ;
}

void Solve() {
    int ret = 0 ;
    for ( int i = 1 ; i <= N ; i ++ ) ret += min(L[i] , R[i]) ;
    /*
    Lsum[1] = L[1] ;
    for ( int i = 2 ; i <= N ; i ++ ) Lsum[i] = Lsum[i-1] + L[i] ;
    Rsum[N] = R[N] ;
    for ( int i = N-1 ; i >= 1 ; i -- ) Rsum[i] = Rsum[i+1] + R[i] ;
    
    for ( int i = 0 ; i <= N ; i ++ ) {
        int tmp ;
        if ( i < MAXi ) tmp = MAXi - i - 1 ;
        else            tmp = i - MAXi + 1 ;
        int tmp1 ;
        if ( i >= 1 ) tmp1 = Lsum[i] ; else tmp1 = 0 ;
        int tmp2 ;
        if ( i+1 <= N ) tmp2 = Rsum[i+1] ; else tmp2 = 0 ;
        
        if ( tmp1 + tmp2 + tmp < ret ) ret = tmp1 + tmp2 + tmp ;
    }
    */
    cout << ret << "\n" ;
}

int main() {
    freopen("B.in","r",stdin) ;
    freopen("B.out","w",stdout) ;
    int Test ; cin >> Test ;
    for ( int i = 1 ; i <= Test ; i ++ ) {
        Init() ;
        cout << "Case #" << i << ": " ;
        Solve() ;
    }
}
