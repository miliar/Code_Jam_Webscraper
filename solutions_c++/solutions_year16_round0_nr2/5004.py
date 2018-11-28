#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define ff first
#define ss second
#define D(a) cerr << ">> " << #a << " = >" << a << "<" << endl
#define PB push_back
#define FOR(i,a,b) for ( int i = (a); i < (b); ++i )
#define FORD(i,a,b) for ( int i = (a); i >= (b); --i )
#define R1(a) scanf("%d",&a)
#define R2(a,b) scanf("%d%d",&a,&b)
#define R3(a,b,c) scanf("%d%d%d",&a,&b,&c)

const int INF = 1e9+7;

string flip( string s, int j ) {
  reverse( s.begin( ), s.begin( ) + j );
  FOR( i, 0, j )
    s[i] = '+' + '-' - s[i];
  return s;
}

int solve1( string s ) {
  int res = 0;
  for ( ; s.find( "-" ) != string::npos; ++res ) {
    while ( !s.empty( ) && s.back( ) == '+' )
      s.pop_back( );
    if ( s[0] == '-' ) {
      s = flip( s, s.size( ) );
    } else {
      int p = s.find_last_of( '+' );
      if ( p == string::npos )
        p = s.size( );
      s = flip( s, p + 1 );
    }
  }
  return res;
}

int solve2( string s ) {
  int res = 0;
  for ( ; s.find( "-" ) != string::npos; ++res ) {
    while ( !s.empty( ) && s.back( ) == '+' )
      s.pop_back( );
    if ( s[0] == '-' ) {
      s = flip( s, s.size( ) );
    } else {
      s = flip( s, 1 );
    }
  }
  return res;
}

int main( ) {
  int t;
  string s;
  cin >> t;
  FOR( caseNr, 1, t+1 ) {
    cin >> s;
    int res = min( solve1( s ), solve2( s ) );
    cout << "Case #" << caseNr << ": " << res << endl;
  }
  return 0;
}
