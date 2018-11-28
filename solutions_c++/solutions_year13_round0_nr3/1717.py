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
#define FILL(a,b)	( memset( a,b,sizeof a ) )
#define mxn       	10000005
using namespace std;

int id,test;
lint ans[mxn];
lint ar[mxn];

void read(){
//	freopen( ".in" , "r" , stdin );
//	freopen( ".out" , "w" , stdout );
}

bool ispal( lint s ){
	
	int sz=0;

	while( s ){

		ar[++sz] = s%10;
		s /= 10;

	}

	for( int i=1 ; i<=sz/2 ; i++ )
		if( ar[i] != ar[sz-i+1] )	return 0;
	return 1;

}

void init(){

	for( lint i=1 ; i<=10000000 ; i++ )	ans[i] = ans[i-1] + ( ispal( i ) && ispal( i*i ) );
			
}

void solve(){

	lint a,b;

	scanf( "%d" , &test );

	init();

	for( id=1 ; id<=test ; id++ ){

		scanf( "%lld %lld" , &a , &b );

		a = sqrt( a-1 )+1;
		b = sqrt( b );

		printf( "Case #%d: %lld\n" , id , ans[b]-ans[a-1] );

	}

	return;
}

int main(){
	solve();
	return 0;
}
