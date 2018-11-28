#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
using namespace std ;

const int MAXN = 100009 ;

int n , m , Ans , F[MAXN] , G[MAXN] ;
char buf[MAXN] ;

vector<int> A[MAXN] ;
map<string, int> H ;

int h(const string s){ if ( H.find(s) == H.end() ) H[s] = m ++ ; return H[s] ; }
void get( vector<int> &A ) { A.clear() ; gets(buf) ; istringstream iss(buf) ; string t ; while ( iss >> t ) A.push_back( h(t) ) ; }

void dfs(int k = 2){
    if ( k == n ){
        int z = 0;
        for ( int i = 0 ; i < m ; i ++ ) if (F[i] && G[i]) z ++ ;
        if ( z < Ans ) Ans = z ;
    } else {
        //ECH(it, A[k]) ++F[*it];
        if ( !A[k].empty() ) for ( int r = 0 ; r < A[k].size() ; r ++ ) F[A[k][r]] ++ ; dfs(k+1) ;
        if ( !A[k].empty() ) for ( int r = 0 ; r < A[k].size() ; r ++ ) F[A[k][r]] -- ;
        if ( !A[k].empty() ) for ( int r = 0 ; r < A[k].size() ; r ++ ) G[A[k][r]] ++ ; dfs(k+1) ;
        if ( !A[k].empty() ) for ( int r = 0 ; r < A[k].size() ; r ++ ) G[A[k][r]] -- ;
    }
}

int main() {
    freopen( "C.in" , "r" , stdin ) ; freopen( "C.out" , "w" , stdout ) ;
    int Test ; cin >> Test ;
    for ( int _ = 1 ; _ <= Test ; _ ++ ) {
        H.clear() ; m = 0 ; cin >> n ;
        for ( int i = 0 ; i < n ; i ++ ) get(A[i]) ;
        
        if ( !A[0].empty() ) for ( int r = 0 ; r < A[0].size() ; r ++ ) F[A[0][r]] ++ ;
        if ( !A[1].empty() ) for ( int r = 0 ; r < A[1].size() ; r ++ ) G[A[1][r]] ++ ;
        Ans = 0x3f3f3f3f ; dfs(); cout << Ans << "\n" ;
        if ( !A[0].empty() ) for ( int r = 0 ; r < A[0].size() ; r ++ ) F[A[0][r]] -- ;
        if ( !A[1].empty() ) for ( int r = 0 ; r < A[1].size() ; r ++ ) G[A[1][r]] -- ;
    }
}
