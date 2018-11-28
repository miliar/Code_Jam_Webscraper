#include <cstdio>
#include <algorithm>

using namespace std;

bool filled( int occ[] ) {
  for( int i = 0; i < 10; i++ ) {
    if( !occ[ i ] ) return false;
  }
  return true;
}

int main( void ) {
  int T;
  freopen("test.in","rt",stdin);
  freopen("test.out","wt",stdout);
  scanf("%d", &T );
  for( int k = 1; k <= T; k++ ) {
  int N, ans;
    scanf("%d", &N );
    if( N == 0 ) {
      printf("Case #%d: INSOMNIA\n", k );
    } else {
      ans = N;
      int occ[ 10 ] = { 0 };
      do {
        int newN = ans;
        while( newN > 0 ) {
          int dig = newN % 10;
          occ[ dig ] = true;
          newN /= 10;
        }
        if( filled( occ ) ) break;
        ans += N;
      } while( true );
      printf("Case #%d: %d\n", k, ans );
    }
  }
  return 0;
}
