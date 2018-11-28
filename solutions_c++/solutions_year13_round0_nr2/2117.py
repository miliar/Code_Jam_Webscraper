#include<iostream>
#include<cstdio>
#include<cstring>
#define MAX(a,b) ( (a)>(b) ? (a) : (b) )
#define FILL(a,b)	( memset( a,b,sizeof a ) )
#define mxn    105
using namespace std;

int id,test;
int n,m;
int mat[mxn][mxn];
int x[mxn],y[mxn];

void read(){
int i,j;
scanf( "%d %d" , &n , &m );
for( i=1 ; i<=n ; i++ )for( j=1 ; j<=m ; j++ ){
scanf( "%d" , mat[i]+j );
x[i] = MAX( x[i] , mat[i][j] );
y[j] = MAX( y[j] , mat[i][j] );
}
}

void solve(){

int i,j,f;

scanf( "%d" , &test );
for( id=1 ; id<=test ; id++ ){
FILL( x,0 );FILL( y,0 );read();

f = 1;

for( i=1 ; i<=n && f ; i++ )for( j=1 ; j<=m && f ; j++ )
if( mat[i][j]<x[i] && mat[i][j]<y[j] )	f=0;
if( f )	printf( "Case #%d: YES\n" , id );
else	printf( "Case #%d: NO\n" , id );
}
}

int main(){
solve();
return 0;
}
