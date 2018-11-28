#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>

#define MAXN 110
#define INF 1234567890

using namespace std;

string S;

int main( void ) {
  int T;
  freopen("test.in","rt",stdin);
  freopen("test.out2","wt",stdout);
  scanf("%d", &T );
  for( int t = 1; t <= T; t++ ) {
    cin >> S;
    int ans = 0, n = S.length() - 1;
    for( int i = 0; i < n; i++ ) {
      if( S[ i ] != S[ i + 1 ] ) ans++;
    }
    if( S[ 0 ] == '-' && S[ n ] == '-' ) ans++;
    if( S[ 0 ] == '+' && S[ n ] == '-' ) ans++;
    printf("Case #%d: %d\n", t, ans );
  }
  return 0;
}
