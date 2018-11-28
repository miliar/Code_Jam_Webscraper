#include <algorithm>
#include <climits>
#include <cmath>
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

int arr[1005];

int solve( int * arr, int n ) {
  if ( n <= 1 )
    return n;
  int tmp;
  int res = n;
  FORD( k, n / 2, 1 ) {
    int cnt   = arr[n];
    arr[k]   += cnt;
    arr[n-k] += cnt;
    arr[n]   -= cnt;
    for ( tmp = n; tmp && !arr[tmp]; --tmp );
    res = min( res, solve( arr, tmp ) + cnt );
    arr[k]   -= cnt;
    arr[n-k] -= cnt;
    arr[n]   += cnt;
  }
  return res;
}

int main( ) {
  DRI( caseCnt );
  FOR( caseNr, 1, caseCnt ) {
    memset( arr, 0, sizeof arr );
    int n = 0;
    DRI( k );
    REP( i, k ) {
      DRI( x );
      n = max( n, x );
      ++arr[x];
    }

    printf( "Case #%d: %d\n", caseNr, solve( arr, n ) );
  }
  return 0;
}