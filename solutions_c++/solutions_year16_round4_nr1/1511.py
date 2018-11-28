#include <bits/stdc++.h>
using namespace std;

char toChar ( int i ) { return "PRS"[i]; }
int toInt ( char c ) { return c == 'P' ? 0 : ( c == 'R' ? 1 : 2 ); }
int cnt[3];
int ans[(1<<12)+1], n;

bool check ( ) {
  deque<int> v;
  for ( int i = 0; i < (1<<n); ++i )
    v.push_back ( ans[i] );
  for ( int left = (1<<n); left >= 2; left /= 2 ) {
    for ( int i = 0; i < left; i += 2 ) {
      if ( v[0] == v[1] ) return false;
      if ( (v[0]+1)%3 == v[1] )
        v.push_back ( v[0] );
      else v.push_back ( v[1] );
      v.pop_front();
      v.pop_front();
    }
  }
  return true;
}

const int order[] = { 0, 2, 1 };
bool go ( int idx = 0 ) {
  if ( cnt[0] + cnt[1] + cnt[2] == 0 )
    return check();

  for ( int id = 0; id < 3; ++id ) {
    int i = order[id];
    if ( cnt[i] > 0 && cnt[(i+1)%3] > 0 ) {
      cnt[i]--;
      cnt[(i+1)%3]--;
      ans[idx] = min ( i, (i+1)%3 );
      ans[idx+1] = max ( i, (i+1)%3 );
      if ( go ( idx+2 ) )
        return true;
      cnt[i]++;
      cnt[(i+1)%3]++;
    }
  }
  return false;
}

bool brute ( ) {
  vector<int> r;
  for ( int i = 0; i < 3; ++i )
    for ( int j = 0; j < cnt[i]; ++j )
      r.push_back ( i );
  do {
    copy ( r.begin(), r.end(), ans );
    if ( check() ) return true;
  } while ( next_permutation(r.begin(),r.end()) );
  return false;
}

int main ( )
{
  freopen ( "A-small-attempt1.in", "r", stdin );
  freopen ( "output", "w", stdout );
  int ntc;
  cin >> ntc;
  for ( int test = 1; test <= ntc; ++test ) {
    cin >> n;
    cin >> cnt[toInt('R')] >> cnt[toInt('P')] >> cnt[toInt('S')];
    printf ( "Case #%d: ", test );
    if ( go ( ) ) {
      for ( int i = 0; i < (1<<n); ++i )
        printf ( "%c", toChar(ans[i]) );
      printf ( "\n" );
    }
    else printf ( "IMPOSSIBLE\n" );
  }
  return 0;
}
