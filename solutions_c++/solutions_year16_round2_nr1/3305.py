#include<bits/stdc++.h>
#define N 2000
using namespace std;

int caso = 0;
string s;
int F[ 26 ], ans[ 10 ];

int P( char x ){
	return x-'A';
}

void doit(){
	cin>>s;
	//cout<<s<<endl;
	int sz = s.size();
	memset( F, 0 , sizeof( F ) );
	memset( ans, 0 ,sizeof( ans ));
	for( int i=0 ; i<sz; ++i ){
		F[ P( s[ i ] ) ]++;
	}
	//zero
	if( F[ P( 'Z' ) ] >0 ){
		int f = F[ P( 'Z' ) ];
		ans[ 0 ] += f;
		F[ P('Z') ] -=f;
		F[ P('E') ] -=f;
		F[ P('R') ] -=f;
		F[ P('O') ] -=f;
	}
	// two
	if( F[ P( 'W' ) ] >0 ){
		int f = F[ P( 'W' ) ];
		ans[ 2 ] += f;
		F[ P('T') ] -=f;
		F[ P('W') ] -=f;
		F[ P('O') ] -=f;
	}
	// six
	if( F[ P( 'X' ) ] >0 ){
		int f = F[ P( 'X' ) ];
		ans[ 6 ] += f;
		F[ P('S') ] -=f;
		F[ P('I') ] -=f;
		F[ P('X') ] -=f;
	}
	
	//four
	if( F[ P( 'U' ) ] >0 ){
		int f = F[ P( 'U' ) ];
		ans[ 4 ] += f;
		F[ P('F') ] -=f;
		F[ P('O') ] -=f;
		F[ P('U') ] -=f;
		F[ P('R') ] -=f;
	}
	
	//three
	if( F[ P( 'R' ) ] >0 ){
		int f = F[ P( 'R' ) ];
		ans[ 3 ] += f;
		F[ P('T') ] -=f;
		F[ P('H') ] -=f;
		F[ P('R') ] -=f;
		F[ P('E') ] -=f;
		F[ P('E') ] -=f;
	}
	
	//one
	if( F[ P( 'O' ) ] >0 ){
		int f = F[ P( 'O' ) ];
		ans[ 1 ] += f;
		F[ P('O') ] -=f;
		F[ P('N') ] -=f;
		F[ P('E') ] -=f;
	}
	
	//five
	
	if( F[ P( 'F' ) ] >0 ){
		int f = F[ P( 'F' ) ];
		ans[ 5 ] += f;
		F[ P('F') ] -=f;
		F[ P('I') ] -=f;
		F[ P('V') ] -=f;
		F[ P('E') ] -=f;
	}
	
	//seven
	if( F[ P( 'V' ) ] >0 ){
		int f = F[ P( 'V' ) ];
		ans[ 7 ] += f;
		F[ P('S') ] -=f;
		F[ P('E') ] -=f;
		F[ P('V') ] -=f;
		F[ P('E') ] -=f;
		F[ P('N') ] -=f;
	}
	
	//nine
	if( F[ P( 'N' ) ] >0 ){
		int f = F[ P( 'N' ) ]/2;
		ans[ 9 ] += f;
		F[ P('N') ] -=f;
		F[ P('I') ] -=f;
		F[ P('N') ] -=f;
		F[ P('E') ] -=f;
	}
	
	//eight
	if( F[ P( 'H' ) ] >0 ){
		int f = F[ P( 'H' ) ];
		ans[ 8 ] += f;
		F[ P('E') ] -=f;
		F[ P('I') ] -=f;
		F[ P('G') ] -=f;
		F[ P('H') ] -=f;
		F[ P('T') ] -=f;
	}
	
	printf("Case #%d: ", ++caso);
	for( int i=0; i<=9; ++i){
		for( int j=0; j<ans[ i ]; ++j ){
			printf("%d", i );
		}
	}
	puts("");
}


int main(){
	int tc;
	cin>>tc;
	while( tc--)doit();
}
