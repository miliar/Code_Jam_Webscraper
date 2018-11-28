#include<iostream>
#include<fstream>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<climits>
#include<ctime>
#include<sstream>
#define mp       	make_pair
#define pb       	push_back
#define st       	first
#define nd       	second
#define wait     	getchar();getchar();
#define lint     	long long
#define KARE(a)	 	( (a)*(a) )
#define MAX(a,b) 	( (a)>(b) ? (a) : (b) )
#define MIN(a,b) 	( (a)<(b) ? (a) : (b) )
#define MAX3(a,b,c)	( MAX( a,MAX(b,c) ) )
#define MIN3(a,b,c)	( MIN( a,MIN(b,c) ) )
#define FILL(ar,a)	memset( ar,a,sizeof ar )
#define oo	 		1e9
#define pii       	pair<int,int>
#define pll			pair<lint,lint>
#define pdd			pair<double,double>
#define y1			yy1
#define eps      	(1e-9)
#define esit(a,b)  	( abs( (a)-(b) ) < eps )
#define sol(a)		( (a)<<1 )
#define sag(a)		( sol(a)|1 )
#define orta(a,b)	( ( (a)+(b) )>>1 )
#define mxn       	1005
using namespace std;

lint id,test,n,p;

lint calc1( lint s ){

	lint b,res;

	b = n;
	res = 0;

	while( s ){

		b >>= 1;
		res += b;

		s -= 1;
		s >>= 1;

	}

	return res+1;

}

lint calc2( lint s ){

	lint b,res;

	b = n;
	res = 0;

	while( s ){

		b >>= 1;
		res += b;
		
		s -= 1;
		s >>= 1;

	}

	return n-res;

}

void solve(){

	lint bas,son,ort;

	scanf( "%lld" , &test );

	for( id=1 ; id<=test ; id++ ){

		scanf( "%lld %lld" , &n , &p );
		n = 1LL<<n;

		bas = 1;
		son = n;

		while( bas<son ){

			ort = orta(bas,son)+1;

			if( calc1( ort-1 )<=p )	bas = ort;
			else					son = ort-1;

		}

		printf( "Case #%lld: %lld " , id , bas-1 );

		bas = 1;
		son = n;

		while( bas<son ){

			ort = orta(bas,son)+1;

			if( calc2( n-ort )<=p )	bas = ort;
			else					son = ort-1;

		}

		printf( "%lld\n" , bas-1 );

	}

	return;
}

int main(){
	solve();
	return 0;
}
