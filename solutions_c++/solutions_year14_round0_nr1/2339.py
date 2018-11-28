#include "stdio.h"

int main(){

  FILE *fp = fopen( "A-small-attempt0.in" , "r" );
  FILE *fo = fopen( "out" , "w" );

  int n;

  fscanf( fp , "%d" , &n );

  for( int l = 0; l < n; l++ ){
    int r;
    int cards[4][4];


    fscanf( fp , "%d" , &r );
    for( int i = 0; i < 4; i++ )
      for( int j = 0; j < 4; j++ )
	fscanf( fp , "%d" , &cards[i][j] );

    int koho[4];
    for( int i = 0; i < 4; i++ )
      koho[i] = cards[r-1][i];


    fscanf( fp , "%d" , &r );
    for( int i = 0; i < 4; i++ )
      for( int j = 0; j < 4; j++ )
	fscanf( fp , "%d" , &cards[i][j] );

    int ans = -1;
    for( int i = 0; i < 4; i++ ){
      for( int j = 0; j < 4; j++ ){
	if( koho[j] == cards[r-1][i] ){
	  if( ans == -1 ) ans = cards[r-1][i];
	  else if( ans > 0 ) ans = -2;
	}
      }
    }

    fprintf( fo , "Case #%d: ", l+1 );
    if( ans > 0 ) fprintf( fo , "%d\n" , ans );
    if( ans == -2 ) fprintf( fo , "Bad magician!\n" );
    if( ans == -1 ) fprintf( fo , "Volunteer cheated!\n" );
      
  }
  

}
