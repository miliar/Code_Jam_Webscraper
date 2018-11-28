#include <cstdio>

int main (){
    
    int t;
    scanf( "%d", &t );
    int ret = 0;
    for( int i = 0; i < t; ++i ){
      int a, b, k;
      scanf( "%d%d%d", &a, &b, &k );
      for( int j = 0; j < a; ++j )
        for( int l = 0; l < b; ++l )
          if( (j & l) < k ) ++ret;
    
      printf( "Case #%d: %d\n", i+1, ret );
      ret = 0;
    }
    
    return 0;   
}
