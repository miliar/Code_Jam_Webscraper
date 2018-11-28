#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std ;

const int MAXN = 20 ;
double P[1<<MAXN] , F[1<<MAXN] ;
int N , beg ;

double DP(int x) {
    if ( F[x] >= 0.000 ) return F[x] ;
    // if ( (x | beg) != beg ) return -1.000 ;
    
    F[x] = 0.000 ;
    P[x] = 0.000 ;
    for ( int j = 0 ; j < N ; j ++ ) if ( ((x >> j) % 2 == 1) && ((beg >> j) % 2 == 0) ) {
        double sum = (double)N , tmp = (double)N ;
        int N2 = 1 ;
        for ( int k = (j+N-1)%N ; ((x>>k)%2==1) && k!=j ; k = (k+N-1)%N ) {
            tmp = tmp - 1.000 ;
            sum += tmp ;
            N2 ++ ;
        }
        
        F[x] += ( sum/(double)N2 + DP(x - (1<<j)) ) * (double)N2 / double(N) * P[x - (1<<j)] ;
        P[x] += P[x - (1<<j)] * (double)N2 / double(N) ;
    }
    
    F[x] /= P[x] ;
    
    //cout << "F[" << x << "]=" << F[x] << "\n" ;
    //cout << "P[" << x << "]=" << P[x] << "\n" ;
    return F[x] ;
}

int main() {
    freopen("D.in","r",stdin) ;
    freopen("D.out","w",stdout) ;
    int Test ; cin >> Test ;
    for ( int i = 1 ; i <= Test ; i ++ ) {
        string S ; cin >> S ;
        N = S.size() ;
        
        beg = 0 ;
        for ( int j = N-1 ; j >= 0 ; j -- ) beg = beg*2 + (S[j]=='.'?0:1) ;
        //cout << "beg=" << beg << "\n" ;
        for ( int j = 0 ; j < (1<<N) ; j ++ ) F[j] = -1.000 ;
        F[beg] = 0.000 ;
        P[beg] = 1.000 ;
        
        DP((1<<N)-1) ;
        printf("Case #%d: %.12lf\n" , i , F[(1<<N)-1] * P[(1<<N)-1]) ;
    }
}
