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

char res[1<<15];
map<char,char> comp = { { 'R', 'S' }, { 'S', 'P' }, { 'P', 'R' } };

void solve( int n, int index, char win ) {
  // D( n );
  // D( index );
  // D( win );
  if ( !n ) {
    res[index] = win;
    return;
  }
  if ( win < comp[win] ) {
    solve( n-1, index*2, win );
    solve( n-1, index*2+1, comp[win] );
  } else {
    solve( n-1, index*2, comp[win] );
    solve( n-1, index*2+1, win );
  }
}
string mix( string x ) {
  if ( x.size( ) == 1 )
    return x;
  string a = mix( x.substr( 0, x.size( )/2 ) );
  string b = mix( x.substr( x.size( )/2 ) );
  if ( a < b )
    return a + b;
  return b + a;
}
int main( ) {
  int t, n, r, p, s;
  cin >> t;
  FOR( caseNr, 1, t+1 ) {
    cout << "Case #" << caseNr << ": ";
    cin >> n >> r >> p >> s;
    for ( auto x : comp ) {
      memset( res, 0, sizeof res );
      solve( n, 1, x.ff );
      map<char,int> cnt;
      FOR( i, 1, (1<<(n+1))+1 )
        ++cnt[ res[i] ];
      // D( cnt['R'] );
      // D( cnt['P'] );
      // D( cnt['S'] );
      if ( cnt['R'] == r && cnt['P'] == p && cnt['S'] == s ) {
        cout << mix( string( res+(1<<n) ) ) << endl;
        goto next;
      }
    }
    cout << "IMPOSSIBLE" << endl;
    next:;
  }
  return 0;
}
