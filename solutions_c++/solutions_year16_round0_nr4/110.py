#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

typedef bitset<101> Mask;

ll fpow ( ll b, int e ) {
  ll r = 1;
  while ( e ) {
    if ( e&1LL ) r = r*b;
    b = b*b;
    e >>= 1;
  }
  return r;
}

Mask mask ( ll i, ll K, ll C ) {
  Mask r;
  r.reset();
  if ( C == 1 ) {
    r[i] = 1;
    return r;
  }
  r[i%K] = 1;
  r |= mask ( i/K, K, C-1 );
  return r;
}

void check ( const vector<ll>& ans, ll K, ll C ) {
  Mask r;
  r.reset();
  for ( ll i : ans )
    r |= mask ( i, K, C );
  for ( int i = 0; i < K; ++i )
    assert ( r[i] );
}

int main ( )
{
  int ntc;
  cin >> ntc;
  for ( int test = 1; test <= ntc; ++test ) {
    int K, C, S;
    cin >> K >> C >> S;

    cout << "Case #" << test << ":";
    if ( C*S < K ) {
      cout << " IMPOSSIBLE\n";
      continue;
    }

    vector<ll> ans;
    for ( int i = 0; i < K; i += C ) {
      ll idx = 0;
      for ( int j = i; j < i+C; ++j )
        idx = idx*ll(K) + ll(min(j,K-1));
      ans.push_back ( idx );
    }

    assert ( ans.size() <= K );
    check ( ans, K, C );

    for ( ll x : ans )
      cout << ' ' << x+1;
    cout << endl;
  }
  return 0;
}
