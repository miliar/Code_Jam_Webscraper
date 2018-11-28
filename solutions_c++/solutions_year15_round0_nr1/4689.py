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

const int S = 1005;
int shy[S];

int main( ) {
  char c;
  DRI( caseCnt );
  FOR( caseNr, 1, caseCnt ) {
    memset( shy, 0, sizeof shy );
    DRI( s );
    FOR( i, 0, s ) {
      scanf( " %c", &c );
      shy[i] = c - '0';
    }
    int people = 0, friends = 0;
    FOR( i, 0, s ) {
      if ( !shy[i] )
        continue;
      if ( people + friends < i )
        friends = i - people;
      people += shy[i];
    }
    printf( "Case #%d: %d\n", caseNr, friends );
  }

  return 0;
}