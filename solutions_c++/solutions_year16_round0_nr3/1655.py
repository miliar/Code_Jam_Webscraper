#include <cstdio>
#include <algorithm>

using namespace std;

int main( void ) {
  int T;
  freopen("D-large.in","rt",stdin);
  freopen("D-large.out","wt",stdout);
  scanf("%d", &T );
  for( int t = 1; t <= T; t++ ) {
    int K, C, S;
    scanf("%d %d %d", &K, &C, &S );
    if( S < K - 1 || ( S < K && K == 2 ) ) {
      printf("Case #%d: IMPOSSIBLE\n", t);
      continue;
    }
    printf("Case #%d:", t );
    if( K == 1 ) printf(" 1\n");
    else {
      for( int i = 2; i <= K; i++ ) {
        printf(" %d", i );
      }
      printf("\n");
    }
  }
  return 0;
}
