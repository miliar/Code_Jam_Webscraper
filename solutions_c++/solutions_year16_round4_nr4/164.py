#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std ;

int N , A[20][20] , V[20] , Answer ;
string suf ;

bool Check( int arv , int hhh , int k ) {
	if ( k <= 0 ) return false ;
	if ( hhh > N ) return true ;
	if ( hhh == arv ) return Check( arv , hhh + 1 , k ) ;
	
	bool ret = Check( arv , hhh + 1 , k ) ;
	for ( int i = 1 ; i <= N ; i ++ ) if ( V[i] && A[hhh][i] ) { V[i] = false ; ret &= Check( arv , hhh + 1 , k - 1 ) ; V[i] = true ; }
	return ret ;
}

void DFS( int i , int j , int Value ) {
	if ( i > N ) {
		bool pan = true;
		for ( int i = 1 ; i <= N ; i ++ ) {
			int cnt = 0 ;
			for ( int j = 1 ; j <= N ; j ++ ) { cnt += A[i][j] ; if ( A[i][j] == 1 ) V[j] = 1 ; else V[j] = 0 ; }
			if ( cnt == 0 ) pan = false ; else pan &= Check(i , 1 , cnt) ;
		}
		if ( pan && Value < Answer ) Answer = Value ; return ;
	}
	
	int ni = i , nj = j + 1 ;
	if ( j == N+1 ) { ni ++ ; nj = 1 ; }
	DFS( ni , nj , Value ) ;
	if ( A[i][j] == 0 ) { A[i][j] = 1 ; DFS( ni , nj , Value+1 ) ; A[i][j] = 0 ; }
}

int main() {
	int Test ; cin >> Test ;
	for ( int i = 1 ; i <= Test ; i ++ ) {
		cin >> N ;
		for ( int ii = 1 ; ii <= N ; ii ++ ) {
			cin >> suf ;
			for ( int jj = 1 ; jj <= N ; jj ++ )
				if ( suf[jj-1] == '0' ) A[ii][jj] = 0 ;
				else                    A[ii][jj] = 1 ;
		}
		Answer = 100 ;
		DFS(1 , 1 , 0) ;
		cout << "Case #" << i << ": " << Answer << "\n" ;
	}
}