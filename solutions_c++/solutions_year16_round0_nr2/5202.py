#include <iostream>
#include <cstring>
using namespace std ;
int dp[1000] ;
int main(){
	int t ;
	char s[200] ;
	cin >> t ;
	for( int _ = 1 ;_ <= t ;_ ++ ){
		cin >> s ;
		int l = strlen(s) ,ans = 0 ;
		for( int i = 0 ;i < l - 1 ;i ++ ){
			if( s[i] != s[i+1] ){
				ans ++ ;
				for( int j = 0 ;j <= i/2 ;j ++ ) swap(s[i-j] ,s[j]) ;
				for( int j = 0 ;j <= i ;j ++ )
					s[j] = s[j] == '+' ? '-' : '+' ;
			}
		}
		if( s[0] == '-' ) ans ++ ;
		printf( "Case #%d: %d\n" ,_ ,ans ) ;
	}
}
