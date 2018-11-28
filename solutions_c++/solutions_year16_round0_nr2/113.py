#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int solve ( ) {
  string inp, s;
  cin >> inp;
  s = inp.substr(0,1);
  for ( int i = 1; i < inp.size(); ++i )
    if ( inp[i] != s[s.size()-1] )
      s.push_back ( inp[i] );
  if ( s[s.size()-1] == '+' )
    s = s.substr ( 0, s.size()-1 );

  return s.size();
}

int main ( )
{
  int ntc;
  scanf ( "%d", &ntc );
  for ( int test = 1; test <= ntc; ++test ) {
    int r = solve();
    printf ( "Case #%d: %d\n", test, r );
  }
  return 0;
}
