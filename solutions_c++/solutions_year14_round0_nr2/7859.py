//In the name of God
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <climits>
#include <complex>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <bitset>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

#define X first
#define Y second
// #define X real()
// #define Y imag()
// #define cin fin
// #define cout fout

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pll;
typedef complex<int> point;
typedef pair<int, int> pii;
typedef pair<pii, ll> piii;
const int maxn = 1e5 + 1e2;

int t;
ld c, f, x, ans, dp[maxn];

int main ()
{
  cin >> t ;
  for(int counter = 1 ; counter <= t ; counter++)
    {
      cin >> c >> f >> x ; 
      ans = x / 2.0;
      dp[0] = 0;
      for(int i = 1 ; i <= x ; i++)
	{
	  dp[i] = dp[i - 1] + (c / (2.0 + (i - 1.0) * f));
	  ans = min(ans, dp[i] + x / (2.0 + (ld)i * f));
	}
      cout << "Case #" << counter << ": " << fixed << setprecision(7) << ans << endl ;
    }
}
