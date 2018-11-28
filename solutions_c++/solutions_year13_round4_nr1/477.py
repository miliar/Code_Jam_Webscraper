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
#define mxn       	105
using namespace std;

vector<int>inis[mxn],binis;

int id,test;
int n,m,ans,normal;
int sta[mxn];

int calc( int a , int b ){

    int f,ret=0;

    f = b-a;
	ret += f*n;

	f--;
	ret -= f*(f+1)/2;

	return ret;

}


void read(){
//	freopen( ".in" , "r" , stdin );
//	freopen( ".out" , "w" , stdout );

	int i,j,a,b,p;

	scanf( "%d %d" , &n , &m );

	for( i=1 ; i<=m ; i++ ){

		scanf( "%d %d %d" , &a , &b , &p );

		sta[a]+=p;
		normal += p*calc(a,b);

		for( j=a ; j<=b ; j++ )
		for( int k=1 ; k<=p ; k++ )	inis[j].pb( b );

	}

	return;

}

void solve(){

	int i,j;

	scanf( "%d" , &test );

	for( id=1 ; id<=test ; id++ ){

		normal = ans = 0;

		for( i=1 ; i<=100 ; i++ )	inis[i].clear();
		binis.clear();

		read();

		for( i=1 ; i<=n ; i++ ){

			for( j=1 ; j<=sta[i] ; j++ )	binis.pb( i );
			sta[i] = 0;

			sort( binis.begin() , binis.end() );
			sort( inis[i].rbegin() , inis[i].rend() );

			while( binis.size() && inis[i][ binis.size()-1 ]==i ){

				ans += calc( binis[ binis.size()-1 ] , i );
				binis.pop_back();
				inis[i].pop_back();

			}

		}

		printf( "Case #%d: %d\n" , id , normal - ans );

	}


	return;
}

int main(){
	solve();
	return 0;
}
