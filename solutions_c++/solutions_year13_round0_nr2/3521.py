#include <cstdio>

int main( ) {
  freopen( "input.txt", "r", stdin );
  freopen( "output.txt", "w", stdout );
  
  int T;
  int R, C;
  
  scanf( "%d", &T );
  for( int cs = 1; cs <= T; ++cs ) {
    scanf( "%d %d", &R, &C );
    
    int board[ R ][ C ];
    for( int i = 0; i < R; ++i ) {
      for( int j = 0; j < C; ++j ) {
        scanf( "%d", &( board[ i ][ j ] ) );
      }
    }
    
    bool ok = true;
    
    for( int i = 0; i < R; ++i ) {
      for( int j = 0; j < C; ++j ) {
        bool row_ok = true;
        bool col_ok = true;
        
        for( int k = i-1; k >= 0; --k ) {
          if( board[ k ][ j ] > board[ i ][ j ] ) {
            row_ok = false;
            break;
          }
        }
        
        for( int k = i+1; k < R; ++k ) {
          if( board[ k ][ j ] > board[ i ][ j ] ) {
            row_ok = false;
            break;
          }
        }
        
        for( int k = j-1; k >= 0; --k ) {
          if( board[ i ][ k ] > board[ i ][ j ] ) {
            col_ok = false;
            break;
          }
        }
        
        for( int k = j+1; k < C; ++k ) {
          if( board[ i ][ k ] > board[ i ][ j ] ) {
            col_ok = false;
            break;
          }
        }
        
        if( !col_ok && !row_ok ) {
          ok = false;
          break;
        }
      }
      
      if( !ok ) break;
    }
    
    printf( "Case #%d: ", cs );
    if( ok ) {
      printf( "YES\n" );
    } else {
      printf( "NO\n" );
    }
  }
  
  return 0;
}
      
        
