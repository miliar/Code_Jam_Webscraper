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

int test,id,cnt[mxn];

void read(){

	freopen( "input.in" , "r" , stdin );
	freopen( "output.out" , "w" , stdout );

}

void solve(){
	
  int i,j,ans,r,t,mg;

  scanf( "%d" , &test );
  
  for( id=1 ; id<=test ; id++ ){
  	
  	memset( cnt,0,sizeof cnt );
  	
  	scanf( "%d" , &r );
  	for( i=1 ; i<=4 ; i++ )
	for( j=1 ; j<=4 ; j++ ){
  		
  		scanf( "%d" , &t );
  		if( i==r )	cnt[t]++;  		
  		
  	}
  	
  	scanf( "%d" , &r );
  	for( i=1 ; i<=4 ; i++ )
	for( j=1 ; j<=4 ; j++ ){
  		
  		scanf( "%d" , &t );
  		if( i==r )	cnt[t]++;  		
  		
  	}
  	
  	ans = -1;
  	mg  = 0;
  	
  	for( i=1 ; i<=16 ; i++ )
  	if( cnt[i]==2 ){
  		
  		if( ans==-1 )	ans = i;
  		else 			mg = 1;
  		
  	}
  	
  	printf( "Case #%d: " , id );
  	
  	if( mg==1 )		puts( "Bad magician!" );
  	else
  	if( ans==-1 )	puts( "Volunteer cheated!" );
  	else
  		printf( "%d\n" , ans );
  	
  }

}

int main(){
	read();
	solve();
	return 0;
}
