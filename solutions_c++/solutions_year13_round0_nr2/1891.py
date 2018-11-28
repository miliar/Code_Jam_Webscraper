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
#define mxn       	105
using namespace std;

int id,test;
int n,m;
int mat[mxn][mxn];
int x[mxn],y[mxn];

void read(){
//	freopen( ".in" , "r" , stdin );
//	freopen( ".out" , "w" , stdout );
	int i,j;
	scanf( "%d %d" , &n , &m );
	for( i=1 ; i<=n ; i++ )
	for( j=1 ; j<=m ; j++ ){
		scanf( "%d" , mat[i]+j );
		x[i] = MAX( x[i] , mat[i][j] );
		y[j] = MAX( y[j] , mat[i][j] );
	}

	return;
}

void solve(){

	int i,j,f;

	scanf( "%d" , &test );

	for( id=1 ; id<=test ; id++ ){

		FILL( x,0 );
		FILL( y,0 );
		read();

		f = 1;

		for( i=1 ; i<=n && f ; i++ )
		for( j=1 ; j<=m && f ; j++ )
			if( mat[i][j]<x[i] && mat[i][j]<y[j] )	f=0;

		if( f )		printf( "Case #%d: YES\n" , id );
		else		printf( "Case #%d: NO\n" , id );

	}

	return;
}

int main(){
	solve();
	return 0;
}
