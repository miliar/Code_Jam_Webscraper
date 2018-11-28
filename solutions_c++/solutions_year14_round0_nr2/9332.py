#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <climits>
#include <cfloat>
using namespace std;
double c, f, x;
double ans;
void rec( double cookie, double time ){
  if( time > ans )
    {
      return;
    }
  ans = min( ans, time + x / cookie );
  rec( cookie + f, time + c / cookie);
}
void solve(){
  ans = DBL_MAX;
  rec ( 2, 0 );
  printf("%.7lf\n", ans);

}
int main(){
  int t;
  cin >> t;
  for( int i  = 0 ; i < t; ++i )
    {
      cout << "Case #" << i+1 << ": ";
      cin >> c >> f >> x;
      solve();
    }
  return 0;
}
