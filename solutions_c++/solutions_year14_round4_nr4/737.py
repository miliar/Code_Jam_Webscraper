#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>

using namespace std ;

struct Node {
	int next[30] ;
} T[555] ;
int A[111] , TT , ans , num , N , M , TestCase ;
char S[111][111] ;
bool V[111] ;


void trie_insert( int x ) {
	int now = 0 ;
	int len = strlen( S[x] ) ;
	int i ;
	for( i = 0 ; i < len ; i++ ) {
		int ch = S[x][i] - 'A' ;
		if( T[now].next[ch] == -1 ) {
			break ;
		}
		now = T[now].next[ch] ;
	}
	for( ; i < len ; i++ ) {
		int ch = S[x][i] - 'A' ;
		T[now].next[ch] = TT ;
		now = TT ;
		TT++ ;
	}
	return ;
}

int calc() {
	int ret = 0 ;
	for( int i = 0 ; i < M ; i++ ) {
		TT = 1 ;
		memset( T , -1 , sizeof( T ) ) ;
		for( int j = 0 ; j < N ; j++ ) 
		if( A[j] == i ) {
			trie_insert(j) ;
		}
		ret += TT ;
	}
	return ret ;
}


void dfs( int x ) {
	if( x == N ) {
		memset( V , 0 , sizeof( V ) ) ;
		for( int i = 0 ; i < N ; i++ ) {
			V[A[i]] = 1 ;
		}
		bool flag = true ;
		for( int i = 0 ; i < M ; i++ ) {
			if( !V[i] ) {
				flag = false ;
				break ;
			}
		}
		if( !flag ) {
			return ;
		}
		int t = 0 ;
		if( (t = calc()) > ans ) {
			ans = t ;
			num = 1 ;
		} else if( t == ans ) {
			num++ ;
		}
		return ;
	}
	for( int i = 0 ; i < M ; i++ ) {
		A[x] = i ;
		dfs( x + 1 ) ;
	}
	return ;
}

int main(int argc , char* argv[] ) {
	freopen( "D.in" , "r" , stdin ) ;
	freopen( "D.out" , "w" , stdout ) ;
	scanf( "%d" , &TestCase ) ;
	for( int TC = 1 ; TC <= TestCase ; TC++ ) {
		scanf( "%d%d" , &N , &M ) ;
		for( int i = 0 ; i < N ; i++ ) {
			scanf( "%s" , S[i] ) ;
		}
		ans = num = 0 ;
		dfs( 0 ) ;
		printf( "Case #%d: %d %d\n" , TC , ans , num ) ;
	}
	return 0 ;
}
