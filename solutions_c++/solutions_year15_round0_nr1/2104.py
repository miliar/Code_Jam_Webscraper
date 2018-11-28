#include <cstdio>
#include <algorithm>
#include <cstring>

#define MAXN 1100

using namespace std;

int n, sum = 0, ans;
char S[ MAXN + 1 ];

int main( void ) {
  int T;
  freopen("test.in","rt",stdin);
  freopen("test.out","wt",stdout);
  scanf("%d", &T );
  for( int t = 0; t < T; t++ ) {
    sum = ans = 0;
    scanf("%d%s", &n, S );
    for( int i = 0; i <= n; i++ ) {
      if( sum < i ) {
        ans += i - sum;
        sum = i;
      }
      sum += S[ i ] - '0';
    }
    printf("Case #%d: %d\n", t + 1, ans );
  }
  return 0;
}
