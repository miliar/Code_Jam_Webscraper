#include "iostream"
#include "cstdio"
#define maxn 10
using namespace std;

int mat[maxn][maxn][maxn];

main(){
     int test;
     cin >> test;
     for( int t = 1; t <= test; t++ ){
          int r1, r2;
          cin >> r1;
          for( int i = 0; i < 4; i++ )
               for( int j = 0; j < 4; j++ )
                    cin >> mat[0][i][j];
          cin >> r2;
          for( int i = 0; i < 4; i++ )
               for( int j = 0; j < 4; j++ )
                    cin >> mat[1][i][j];
          int ans = -1;
          for( int i = 0; i < 4; i++ )
               for( int j = 0; j < 4; j++ )
                    if( mat[0][r1-1][i] == mat[1][r2-1][j] ){
                         if( ans > 0 )       ans = -2;
                         if( ans == -1 )     ans = mat[0][r1-1][i];
                    }
          if( ans > 0 )       printf("Case #%d: %d\n", t, ans );
          if( ans == -1 )     printf("Case #%d: Volunteer cheated!\n", t );
          if( ans == -2 )     printf("Case #%d: Bad magician!\n", t );
     }
}
