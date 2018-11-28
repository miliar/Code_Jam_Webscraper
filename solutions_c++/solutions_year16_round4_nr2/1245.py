#include <bits/stdc++.h>
using namespace std;

int k;
double dodp ( vector<double> r ) {
  vector<vector<double> > dp ( k, vector<double> ( k/2+1, 0 ) );
  for ( int i = 0; i < k; ++i ) {
    for ( int j = 0; j <= k/2; ++j ) {
      double& d = dp[i][j];
      if ( i == 0 ) {
        if ( !j ) d = 1.0-r[0];
        else if ( j == 1 ) d = r[0];
      }
      else {
        if ( !j ) d = (1.0-r[i])*dp[i-1][0];
        else d = (1.0-r[i])*dp[i-1][j] + r[i]*dp[i-1][j-1];
      }
     // cout << "dp[" << i << "][" << j << "] = " << d << endl;
    }
  }

  return dp[k-1][k/2];
}
double solve ( ) {
  int n;
  cin >> n >> k;
  vector<double> a ( n );
  for ( double& x : a ) cin >> x;
  sort ( a.begin(), a.end() );

  double ans = 0;
  for ( int i = 0; i < (1<<n); ++i ) {
    if ( __builtin_popcount(i) == k ){
      vector<double> r;
      for ( int j = 0; j < n; ++j )
        if ( (i>>j)&1 )
          r.push_back ( a[j] );
      ans = max ( ans, dodp(r) );
    }
  }
  return ans;

  vector<double> r;
  for ( int i = 0; i < k/2; ++i ) {
    r.push_back ( a[i] );
    r.push_back ( a[a.size()-i-1] );
  }

  return dodp(r);
}

int main ( )
{
  freopen ( "B-small-attempt1.in", "r", stdin );
  //freopen ( "input.c", "r", stdin );
  freopen ( "output", "w", stdout );
  fixed(cout);
  cout.precision(10);
  int ntc;
  cin >> ntc;
  for ( int test = 1; test <= ntc; ++test ) {
    double r = solve();
    printf ( "Case #%d: ", test );
    cout << r << endl;
  }
  return 0;
}
