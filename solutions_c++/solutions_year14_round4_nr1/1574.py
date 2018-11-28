#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define DEBUG(x) cout << ">>> " << #x << " : " << x << endl
#define MP make_pair
#define PB push_back
#define REP(i,b) for ( int i = 0; i < int(b); ++i )
#define FOR(i,a,b) for ( int i = int(a); i <= int(b); ++i )
#define FORD(i,a,b) for ( int i = int(a); i >= int(b); --i )
#define RI(a) scanf("%d", &a)
#define RII(a,b) scanf("%d%d", &a, &b)
#define RIII(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define RIIII(a,b,c,d) scanf("%d%d%d%d", &a, &b, &c, &d)
#define MM(x,b) memset( x, b, sizeof( x ) )
const int INF = 1<<29;
typedef long long ll;

vi files;

int main( ) {
  int caseCnt, n, x, tmp;
  cin >> caseCnt;
  FOR( caseNr, 1, caseCnt ) {
    cin >> n >> x;
    files.resize( n );
    REP( i, n )
      cin >> files[i];
    sort( files.begin( ), files.end( ) );
    int cnt = 0;
    for ( ; !files.empty( ); ++cnt ) {
      int big = files.back( );
      int small = x - big;
      files.pop_back( );
      if ( files.empty( ) )
        continue;
      auto it = lower_bound( files.begin( ), files.end( ), small );
      if ( it == files.end( ) || ( *it > small && it != files.begin( ) ) )
        --it;
      if ( *it <= small )
        files.erase( it );
    }
    cout << "Case #" << caseNr << ": " << cnt << endl;
  }

  return 0;
}
