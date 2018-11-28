#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int N;
int m[1005];
ll solve1( void )
{
  ll ret = 0;
  for( int i=1; i<N; i++ ){
    if( m[i-1] > m[i] ){
      ret += m[i-1] - m[i];
    }
  }
  return ret;
}
ll solve2_sub( int d )
{
  int cur = m[0];
  ll ret = 0;
  for( int i=1; i<N; i++ ){
    ret += min( cur, d );
    cur -= d;
    if( cur <= m[i] ) cur = m[i];
    else return -1;
  }
  return ret;
}
ll solve2( void )
{
  int lo = 0;
  int hi = 10000;
  ll ret = -1;
  while( lo <= hi ){
    int mid = (lo+hi)/2;
    ll a = solve2_sub(mid);
    if( a >= 0 ){
      ret = a;
      hi = mid-1;
    } else {
      lo = mid+1;
    }
  }
  return ret;
}
int main( void )
{
  int T;
  cin >> T;
  for( int ti=1; ti<=T; ti++ ){
    cin >> N;
    for( int i=0; i<N; i++ ){
      cin >> m[i];
    }
    cout << "Case #" << ti << ": " << solve1() << ' ' << solve2() << endl;
  }
}
