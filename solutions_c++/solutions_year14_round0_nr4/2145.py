#include "stdio.h"
#include "algorithm"
#include "vector"

using namespace std;

int main(){
  
  FILE *fp = fopen( "D-large.in" , "r" );
  FILE *fo = fopen( "wlout" , "w" );

  int n;
  fscanf( fp , "%d" , &n );

  for( int t = 1; t <= n; t++ ){
    int k;
    fscanf( fp , "%d" , &k );
    double massa[2000] , massb[2000];
    for( int i = 0; i < k; i++ )
      fscanf( fp , "%lf" , &massa[i] );
    for( int i = 0; i < k; i++ )
      fscanf( fp , "%lf" , &massb[i] );

    vector<double> ma , mb;
    for( int i = 0; i < k; i++ )
      ma.push_back( massa[i] );
    sort( ma.begin() , ma.end() );
    for( int i = 0; i < k; i++ )
      mb.push_back( massb[i] );
    sort( mb.begin() , mb.end() );

    fprintf( fo , "Case #%d: " , t );
    bool printed = false;
    for( int i = 0; i < k; i++ ){
      bool ok = true;
      for (int j = 0; j < k-i; j++ ){
	if( ma[j+i] < mb[j] ){
	  ok = false;
	  break;
	}
      }
      if( ok ){
	fprintf( fo , "%d " , k-i );
	printed = true;
	break;
      }
    }

    if( !printed ) fprintf( fo , "0 " );
    printed = false;

    vector<double>::iterator ite;
    for( int i = 0; i < k; i++ ){
      ite = upper_bound( mb.begin() , mb.end() , ma[i] );
      if( ite == mb.end() ){
	fprintf( fo , "%d\n" , k-i );
	printed = true;
	break;
      }
      mb.erase( ite );
    }

    if( !printed ) fprintf( fo , "0\n" );
    
  }

  return 0;
}
