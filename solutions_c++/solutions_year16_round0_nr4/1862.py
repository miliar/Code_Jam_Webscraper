#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long ll;

int main( void ) {
  int T;
  freopen("D.in","rt",stdin);
  freopen("D.out","wt",stdout);
  scanf("%d", &T );
  for( int t = 1; t <= T; t++ ) {
    int K, C, S;
    scanf("%d %d %d", &K, &C, &S );
    ll power = ( ll )pow( K, C - 1 );
    printf("Case #%d:", t);
    ll step = 1LL;
    for( int i = 1; i <= S; i++, step += power ) printf(" %lld", step );
    printf("\n");
  }
  return 0;
}
