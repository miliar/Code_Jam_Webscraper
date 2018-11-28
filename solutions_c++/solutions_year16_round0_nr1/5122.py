#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std ;
int ok ,in[10] ,cnt ;
void parse( int n ){
	while( n ){
		if( !in[n%10] ) cnt ++ ,in[n%10] = 1 ;
		n /= 10 ;
	}
	if( cnt == 10 ) ok = 1 ;
}

int main(){
	int T ;	
	scanf( "%d" ,&T ) ;
	for( int _ = 1 ;_ <= T ;_ ++ ){
		int n ,t = 0 ;
		memset( in ,0 ,sizeof(in) ) ;
		scanf( "%d" ,&n ) ;
		printf( "Case #%d: " ,_ ) ;
		if( n == 0 ){
			puts( "INSOMNIA" ) ;
			continue ;
		}
		ok = cnt = 0 ;
		do{
			parse(t) ;
			t += n ;
		}while( !ok ) ;
		printf( "%d\n" ,t-n ) ;
	}
}

