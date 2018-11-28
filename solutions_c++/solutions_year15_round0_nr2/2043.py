#include <cstdio>
#include <algorithm>

#define MAXN 1100

using namespace std;

int N, P[ MAXN + 1 ];

int check( int upper ) {
  int sol = 0;
  for( int i = 1; i <= N; i++ ) {
    if( P[ i ] > upper ) {
      int n = P[ i ] - upper;
      sol += ( n / upper );
      if( n % upper > 0 ) sol++;
    }
  }
  return sol + upper;
}

int main( void ) {
  int T;
  freopen("test.in","rt",stdin);
  freopen("test.out","wt",stdout);
  scanf("%d", &T );
  for( int t = 1; t <= T; t++ ) {
    int ans = MAXN;
    scanf("%d", &N );
    for( int i = 1; i <= N; i++ ) {
      scanf("%d", &P[ i ] );
    }
    for( int i = 1; i <= MAXN; i++ ) {
      ans = min( ans, check( i ) );
    }
    printf("Case #%d: %d\n", t, ans );
  }
  return 0;
}
