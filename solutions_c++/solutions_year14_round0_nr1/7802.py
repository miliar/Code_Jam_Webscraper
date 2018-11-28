#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 5;

int t;
int a[MAXN][MAXN];
int b[MAXN][MAXN];

int main( void ){
  scanf( "%d", &t );
  
  for( int tc = 1; tc <= t; ++tc ){
    int x, y;
    scanf( "%d", &x );

    for( int i = 0; i < 4; ++i )
      for( int j = 0; j < 4; ++j )
	scanf( "%d", &a[i][j] );
    
    scanf( "%d", &y );
    for( int i = 0; i < 4; ++i )
      for( int j = 0; j < 4; ++j )
	scanf( "%d", &b[i][j] );

    --x; --y;
    int neki, cnt;
    neki = 0; cnt = 0;
    for( int i = 0; i < 4; ++i )
      for( int j = 0; j < 4; ++j )
	if( a[x][i] == b[y][j] ){ ++cnt; neki = a[x][i]; }
  
    printf( "Case #%d: ", tc );
    if( cnt == 0 ) printf( "Volunteer cheated!\n" );
    if( cnt == 1 ) printf( "%d\n", neki );
    if( cnt > 1 ) printf( "Bad magician!\n" );
  }

  return 0;
}
