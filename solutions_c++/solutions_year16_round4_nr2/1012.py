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

double dp[20][20];
double p[205];

int main( ) {
  int t, n, k;
  cin >> t;
  FOR( caseNr, 1, t+1 ) {
    double res = 0;
    cout << "Case #" << caseNr << ": ";
    R2( n, k );
    FOR( i, 0, n )
      cin >> p[i];
    FOR( s, 0, (1 << n) ) {
      vector<double> prob;
      FOR( i, 0, 16 )
        if ( s & (1 << i) )
          prob.PB( p[i] );
      if ( prob.size( ) != k )
        continue;
      memset( dp, 0, sizeof dp );
      dp[0][0] = 1;
      FOR( i, 0, prob.size( ) ) {
        FOR( j, 0, i+1 ) {
          dp[i+1][j+1] += dp[i][j] * prob[i];
          dp[i+1][j]   += dp[i][j] * ( 1 - prob[i] );
        }
      }
      res = max( res, dp[k][k/2] );
    }
    printf( "%.6f\n", res );
  }
  return 0;
}
