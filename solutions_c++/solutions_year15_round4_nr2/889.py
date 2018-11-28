#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define DBG(x) cout << ">>> " << #x << " : " << x << endl
#define PB push_back
#define REP(i,b) for ( int i = 0; i < (b); ++i )
#define FOR(i,a,b) for ( int i = (a); i <= (b); ++i )
#define FORD(i,a,b) for ( int i = (a); i >= (b); --i )
#define RI(a) scanf( "%d", &a )
#define RII(a,b) scanf( "%d%d", &a, &b )
#define RIII(a,b,c) scanf( "%d%d%d", &a, &b, &c )
#define RIIII(a,b,c,d) scanf( "%d%d%d%d", &a, &b, &c, &d )
#define DRI(a) int a; RI(a)
#define DRII(a,b) int a, b; RII(a,b)
#define DRIII(a,b,c) int a, b, c; RIII(a,b,c)
#define DRIIII(a,b,c,d) int a, b, c, d; RIIII(a,b,c,d)
const int INF = 1e9+7;

vector<pair<double,double>> sources;

int main( ) {
  int caseCnt, n;
  double v, t;

  cin >> caseCnt;
  FOR( caseNr, 1, caseCnt ) {
    cin >> n >> v >> t;
    double maxt = 0, mint = 100;
    sources.resize( n );
    REP( i, n ) {
      cin >> sources[i].first >> sources[i].second;
      maxt = max( maxt, sources[i].second );
      mint = min( mint, sources[i].second );
    }
    cout << "Case #" << caseNr << ": ";
    if ( mint > t || maxt < t ) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    if ( sources.size( ) < 2 )
      sources.push_back( { 0, sources[0].second } );

    if ( fabs( sources[0].second - sources[1].second ) < 1e-9 ) {
      cout << fixed << setprecision( 9 ) << v / ( sources[0].first + sources[1].first ) << endl;
      continue;
    }

    if ( sources[1].second > sources[0].second )
      swap( sources[0], sources[1] );

    double lo = 0, hi = v, mi;
    double t0 = sources[0].second, t1 = sources[1].second;
    while ( hi - lo > 1e-12 ) {
      mi = (lo + hi) / 2;
      if ( ( mi * t0 + (v-mi) * t1 ) / v < t )
        lo = mi;
      else
        hi = mi;
    }
    cout << fixed << setprecision( 9 ) << max( mi / sources[0].first, (v - mi) / sources[1].first ) << endl;
  }
  return 0;
}