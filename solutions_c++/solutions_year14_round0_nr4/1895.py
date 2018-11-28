#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std ;

int N ;
double A[1009] , B[1009] ;
bool used[1009] ;

void Init() {
    cin >> N ;
    for ( int i = 1 ; i <= N ; i ++ ) cin >> A[i] ;
    for ( int i = 1 ; i <= N ; i ++ ) cin >> B[i] ;
    sort(A+1,A+N+1) ;
    sort(B+1,B+N+1) ;
}

int Solve1() {
    int ans1 = 0 ;
    for ( int i = 1 ; i <= N ; i ++ ) used[i] = false ;
    int L = 1 , R = N ;
    for ( int i = N ; i >= 1 ; i -- ) {
        if ( A[R] > B[i] ) ans1 ++ , R -- ;
        else               L ++ ;
    }
    return ans1 ;
}

int Solve2() {
    int ans2 = 0 ;
    for ( int i = 1 ; i <= N ; i ++ ) used[i] = false ;
    for ( int i = 1 ; i <= N ; i ++ ) {
        int j ;
        for ( j = 1 ; j <= N ; j ++ ) if ( !used[j] && B[j] > A[i] ) break ;
        if ( j == N+1 ) {
            for ( j = 1 ; j <= N ; j ++ ) if ( !used[j] ) break ;
        }
        if ( B[j] > A[i] ) ;
        else ans2 ++ ;
        used[j] = true ;
    }
    return ans2 ;
}

int main() {
    freopen("D.in" , "r" , stdin) ;
    freopen("D.out", "w" , stdout) ;
    int Test ; cin >> Test ;
    for ( int i = 1 ; i <= Test ; i ++ ) {
        Init() ;
        cout << "Case #" << i << ": " << Solve1() << " " << Solve2() << "\n" ;
    }
}
