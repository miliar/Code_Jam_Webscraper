#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 5;

int t;
int a[MAXN][MAXN];
int b[MAXN][MAXN];

int main( void ){
  scanf( "%d", &t );
  
  for( int tc = 1; tc <= t; ++tc ){
    double c, f, x;
    double add = 2.0;
    double curr = 0.0;
    double elap = 0.0;

    double ans = 1LL << 60LL;
    scanf( "%lf%lf%lf", &c, &f, &x );

    for( int j = 0; j < 1000000; ++j ){
      ans = min( ans, elap + x/add );
      elap += c/add;
      add += f;
    }

    printf( "Case #%d: %lf\n", tc, ans );
  }

  return 0;
}
