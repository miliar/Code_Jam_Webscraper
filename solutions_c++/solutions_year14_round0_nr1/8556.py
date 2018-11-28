#include <cstdio>

int mat[5][5];
int bio[17];
int res;
int sol;

int main (){
    
    int t;
    scanf( "%d", &t );
    
    for( int k = 0; k < t; ++k ){
      int firans;
      scanf( "%d", &firans );
      for( int i = 0; i < 4; ++i )
        for( int j = 0; j < 4; ++j )
          scanf( "%d", &mat[i][j] );
      
      for( int i = 0; i < 4; ++i ) bio[mat[firans-1][i]]++;
      
      int secans;
      scanf( "%d", &secans );
      for( int i = 0; i < 4; ++i )
        for( int j = 0; j < 4; ++j )
          scanf( "%d", &mat[i][j] );
      
      for( int i = 0; i < 4; ++i ) bio[mat[secans-1][i]]++;
      
      for( int i = 1; i <= 16; ++i )
        if( bio[i] == 2 ){ ++res; sol = i; }
      
      if( res == 1 )
        printf( "Case #%d: %d\n", k+1, sol );
      else if( res > 1 )
        printf( "Case #%d: Bad magician!\n", k+1 );
      else
        printf( "Case #%d: Volunteer cheated!\n", k+1 );  
      
      
      for( int i = 1; i <= 16; ++i ) bio[i] = 0;
      res = 0;
    }   
    return 0;   
}
