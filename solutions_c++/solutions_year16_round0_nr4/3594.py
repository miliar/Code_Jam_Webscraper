#include <iostream>
using namespace std ;
int main(){
	int k ,c ,s ,t ;
	cin >> t ;
	for( int _ = 1 ;_ <= t ;_ ++ ){
		printf( "Case #%d: " ,_ ) ;
		cin >> k >> c >> s ;
		long long ans = 1 ;
		long long bse = 1 ;
		while( --c ) bse *= k ;
		for( int i = 0 ;i < s ;i ++ ){
			printf( "%lld%c" ,ans ," \n"[i==s-1] ) ;
			ans += bse ;
		}
	}
}
