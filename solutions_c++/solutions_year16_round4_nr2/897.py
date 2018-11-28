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
#include <limits>
#include <deque>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <map>

#define X first
#define Y second
// #define X real()
// #define Y imag()
// #define cin fin
// #define cout fout
#ifdef linux
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif

using namespace std;
typedef long long ll;
typedef double ld;
typedef pair<ll, ll> pll;
// typedef complex<ld> point;
typedef pair<ll, ll> pii;
typedef pair<pii, ll> piii;
const int maxn = 210;

int t, n, k;
ld p[maxn], dp[maxn][maxn][maxn], b[maxn];
ld dp2[maxn][maxn];

// inline void solve ()
// {
//   // dp[0][0][0] = 1.0;
//   for(int i = 0 ; i <= n ; i++)
//     dp[i][0][0] = 1.0;
//   // for(int i = 0 ; i < n ; i++)
//   //   for(int j = 0 ; j <= i ; j++)
//   //     for(int k = 0 ; k <= j ; k++)
//   // 	{
//   // 	  dp[i + 1][j + 1][k + 1] += (dp[i][j][k] * p[i + 1]) * 0.5;
//   // 	  dp[i + 1][j + 1][k] += (dp[i][j][k] * (1.0 - p[i + 1])) * 0.5;
//   // 	  dp[i + 1][j][k] += dp[i][j][k] * 0.5;
//   // 	}
//   for(int i = 1 ; i <= n ; i++)
//     for(int j = 1 ; j <= i ; j++)
//       for(int k = 0 ; k <= j ; k++)
// 	{
// 	  // if(i == j)
// 	  //   {
// 	  //     if(k != 0)
// 	  // 	dp[i][j][k] = dp[i - 1][j - 1][k - 1] * p[i] + dp[i - 1][j - 1][k] * (1.0 - p[i]);
// 	  //     else
// 	  // 	dp[i][j][k] = dp[i - 1][j - 1][k] * (1 - p[i]);	    
// 	  //   }
// 	  // else
// 	  //   {
// 	      if(k != 0)
// 		dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - 1][k - 1] * p[i] + dp[i - 1][j - 1][k] * (1.0 - p[i]));
// 	      else
// 		dp[i][j][k] = max(dp[i - 1][j][k], (dp[i - 1][j - 1][k] * (1.0 - p[i])));
// 	    // }
// 	  cerr << i << ' ' << j << ' ' << k << ' ' << dp[i][j][k] << endl ;
// 	}
// }


inline ld solve2(vector<ld> b)
{
  for(int i = 0 ; i < maxn ; i++)
    for(int j = 0 ; j < maxn ; j++)
      dp2[i][j] = 0.0;
  int n = b.size() - 1;
  dp2[0][0] = 1;
  for(int i = 1 ; i <= n ; i++ )
    for(int j = 0 ; j <= i ; j++)
      {
	dp2[i][j] = (j == 0 ? 0.0 : dp2[i - 1][j - 1] * b[i]) + dp2[i - 1][j] * (1 - b[i]);
      }
  return dp2[n][n / 2];
}


inline int count (int x)
{
  int ret = 0;
  while(x)
    {
      ret += x & 1;
      x /= 2;
    }
  return ret; 
}

int main ()
{
  int o; cin >> o;
  for (int t = 0; t < o; t ++)
    {
      cerr << t << endl ;
      cin >> n >> k ;
      for(int i = 0 ; i < n ; i++)
	cin >> p[i] ;
      sort(p, p + n);
      ld ans = 0.0;
      vector<ld> b;
      for(int mask = 0 ; mask < (1<<n) ; mask++)
	if(count(mask) == k)
	  {
	    b.resize(0);
	    b.push_back(0);
	    for(int i = 0 ; i < n ; i++)
	      if(mask & (1<<i))
		b.push_back(p[i]);
	    ans = max(ans, solve2(b));
	  }
      cout << "Case #" << t + 1 << ": " << fixed << setprecision(6) << ans << endl ;
    }
}

