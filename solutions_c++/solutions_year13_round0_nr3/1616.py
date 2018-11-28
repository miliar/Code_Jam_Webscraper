#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
ll make_palindrome( ll n, int f )
{
  ll a=0,b=n,c=1;
  while( b > 0 ){
    a = a*10 + b % 10;
    b /= 10;
    c *= 10;
  }
  if( !f ) n /= 10;
  return n*c + a;
}
int is_palindrome( ll a )
{
  int d[32],n=0;
  while( a > 0 ){
    d[n++] = a % 10;
    a /= 10;
  }
  for( int i=0; i<n/2; i++ )
    if( d[i] != d[n-1-i] ) return 0;
  return 1;
}
int main( void )
{
  vector<ll> v;
  ll a = 1;
  for( int i=1; i<=4; i++ ){
    for( int j=0; j<=1; j++ ){
      for( ll k=a; k<=a*10-1; k++ ){
        ll b = make_palindrome( k, j );
        b *= b;
        if( is_palindrome( b ) ){
          v.push_back( b );
        }
      }
    }
    a *= 10;
  }
  int T;
  cin >> T;
  for( int testcase = 1; testcase <= T; testcase++ ){
    ll a,b;
    cin >> a >> b;
    int r=0;
    for( int i=0; i<v.size(); i++ ){
      if( a <= v[i] && v[i] <= b )
        r++;
    }
    cout << "Case #" << testcase << ": " << r << endl;
  }
  return 0;
}
