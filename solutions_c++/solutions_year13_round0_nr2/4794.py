
#include<cstdio>
#include<cassert>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<vector>
#include<algorithm>

int main() {
   int rowmax[100], rowmin[100], colmax[100], colmin[100];
   int mat[100][100];
   int num, M, N;
   scanf( "%d", &num );
   for( int i = 0; i < num; i++ ) {
      memset( rowmax, -1, sizeof( rowmax ) );
      //memset( rowmin, 200, sizeof( rowmin ) );
      memset( colmax, -1, sizeof( rowmax ) );
      //memset( colmin, 200, sizeof( rowmax ) );
      scanf( "%d %d", &N, &M );
      for( int j = 0; j < N; j++ ) {
         for( int k = 0; k < M; k++ ) {
            scanf( "%d", &mat[j][k] );
            int cur = mat[j][k];
            //if( cur < rowmin[j] ) rowmin[j]=cur;
            //if( cur < colmin[k] ) colmin[k]=cur;
            if( cur > rowmax[j] ) rowmax[j]=cur;
            if( cur > colmax[k] ) colmax[k]=cur;
               
         }
      }
      int possible=1;
      for( int j = 0; j < N && possible; j++ ) {
         for( int k = 0; k < M; k++ ) {
            if( mat[j][k] < rowmax[j] && mat[j][k] < colmax[k] ) {
               possible=0;
               break;
            }
         }
      }
      printf( "Case #%d: %s\n", i+1, possible ? "YES" : "NO" );
   }
   return 0;
}

