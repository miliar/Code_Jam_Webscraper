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
const int maxn = 30;
const int inf = 1e7;
const int lim = 24;

int T, n, ans;
vector<string> org, g;
vector<vector<int> > p;
int mark[maxn];

inline int bt(int lev, int ord)
{
  // cerr << "here " << lev << ' ' << ord << endl ;
  // for(int i = 0 ; i < n ; i++)
  //   cerr << g[i] << endl ;
  // for(int i = 0 ; i < n ; i++)
  //   cerr << mark[i] << ' ' ; cerr << endl ;
  if(lev == n)
    return 0;
  vector<int> choices;
  for(int i = 0 ; i < n ; i++)
    if(mark[i] == 0 && g[p[ord][lev]][i] == '1')
      choices.push_back(i);
  if(choices.size() == 0)
    return -1;
  for(int i = 0 ; i < choices.size() ; i++)
    {
      mark[choices[i]] = 1;
      if(bt(lev + 1, ord) != 0)
	return -1;
      mark[choices[i]] = 0;
    }
  return 0;
}

inline int solve_small(int mask)
{
  int ret = 0;
  g = org;
  for(int i = 0 ; i < (n*n) ; i++)
    if(mask & (1<<i))
      {     
	if(g[i / n][i % n] == '0')
	  {
	    g[i / n][i % n] = '1';
	    ret ++;
	  }
      }
    else if(g[i / n][i % n] == '1')
      return inf;
  
  if(ret >= ans)
    return ret;

  for(int i = 0 ; i < p.size() ; i++)
    {
      memset(mark, 0, sizeof mark);
      if(bt(0, i) != 0)
	return inf;
    }
  // for(int i = 0 ; i < p.size() ; i++)
  //   for(int i1 = 0 ; i1 < p.size() ; i1++)
  //     for(int i2 = 0 ; i1 < p.size() ; i1++)
  // 	for(int i3 = 0 ; i1 < p.size() ; i1++)
  // 	  for(int i4 = 0 ; i1 < p.size() ; i1++)
  // 	    {
  // 	      vector<int> vc;
  // 	      vc.push_back(i);
  // 	      vc.push_back(i1);
  // 	      vc.push_back(i2);
  // 	      vc.push_back(i3);
  // 	      vc.push_back(i4);
  // 	    }
  return ret;
}

int main ()
{
  cin >> T ; 
  for(int t = 1 ; t <= T ; t++)
    {
      cin >> n ;
      org.resize(n);
      for(int i = 0 ; i < n ; i++)
	cin >> org[i] ;

      vector<int> tmp;
      p.resize(0);
      for(int i = 0 ; i < n ; i++)
	tmp.push_back(i);
      do
	{
	  p.push_back(tmp);
	} while(next_permutation(tmp.begin(), tmp.end()));

      ans = inf;
      for(int mask = 0 ; mask < (1<<(n*n)) ; mask++)
	ans = min(ans, solve_small(mask));
      cout << "Case #" << t << ": " << ans << endl ;
    }
}
