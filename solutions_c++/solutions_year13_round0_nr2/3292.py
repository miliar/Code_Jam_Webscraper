#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

const int N = 111;
int a[N][N], b[N];

int main() {
    int T, n, m ;
    cin>>T;
    for( int tc = 1; tc <= T; ++tc ) {
         cin>>n>>m;
         fill( b, b+m, -1);
         bool ok = true;
         for( int i = 0; i < n; ++i ) {
              int maxv = -1;
              for( int j = 0; j < m; ++j ) { 
                   cin>>a[i][j];
                   maxv = max( maxv, a[i][j] );
              }
              if( i ) continue;
              for( int j = 0 ; j < m; ++j ) {
                   if( maxv != a[i][j] ) {
                       b[j] = a[i][j];
                   }
              }
         }
         
         for( int i = 1 ; i < n ; ++i ) {
              int flag = 11111;
              for( int j = 0 ; j < m; ++j ) {
                   if( b[j] != -1 && b[j] > a[i][j] ) {
                       flag = min( flag, a[i][j] );
                       break;
                   }
                   if( b[j] != -1 && b[j] < a[i][j] ) ok = false;
              }
              
              if( flag < 11111 ) {
                  for( int j = 0; j < m; ++j ) {
                       if( (flag > a[i][j] && a[i][j] != a[0][j]) || flag < a[i][j] ) ok = false;
                  }
              } else {
                  int maxv = *max_element( a[i], a[i]+m );
                  for( int j = 0 ; j < m; ++j ) if( maxv > a[i][j] ) {
                        for( int k = 0 ; k < n ;++k ) {
                             if( a[k][j] > a[i][j] ) ok = false;
                        }
                  }
              }
         }
         cout<<"Case #"<<tc<<": ";
         if( ok ) cout<<"YES"<<endl;
         else cout<<"NO"<<endl;
    }
    return 0;
}
