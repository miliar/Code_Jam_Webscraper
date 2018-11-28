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
#include <ctime>
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
typedef complex<ll> point;
typedef pair<int, int> pii;
typedef pair<pii, int> piii;

int tests, n, m;
vector<string> vc;

inline int solve (int mask)
{
  // int cp = mask;
  
  int ret = 0;
  vector<string> all[4];
  set<string> trie[4];
  for(int i = 0 ; i < m ; i++, mask /= n)
    all[mask % n].push_back(vc[i]);

  // if(cp == 2)
  //   {
  //     cerr << "HERE" << endl ;
  //     for(int i = 0 ; i < n ; i++, cerr << endl)
  // 	for(int j = 0 ; j < all[i].size() ; j++)
  // 	  cerr << all[i][j] << ' ' ;
  //     cerr << endl ;
  //   }

  for(int i = 0 ; i < n ; i++)
    for(int j = 0 ; j < all[i].size() ; j++)
      for(int k = 0 ; k <= all[i][j].size() ; k++)
	trie[i].insert(all[i][j].substr(0, k));
  for(int i = 0 ; i < n ; i++)
    ret += trie[i].size();
  
  // if(cp == 2)
  //   {
  //     cerr << "RET IS " << ret << endl ;
  //     for(int i = 0 ; i < n ; i++)
  // 	cerr << trie[i].size() << endl ;
  //   }
  
  return ret;
}

int main ()
{
  ios_base :: sync_with_stdio(0);
  cin >> tests ;
  for(int counter = 1 ; counter <= tests ; counter++)
    {
      cin >> m >> n  ;
      vc.resize(m);
      for(int i = 0 ; i < m ; i++)
	cin >> vc[i] ;
      int tot = 1;
      for(int i = 0 ; i < m ; i++)
	tot *= n;
      int Max = 0, cnt = 0;
      for(int mask = 0 ; mask < tot ; mask++)
	{
	  int hlp = solve(mask);
	  if(hlp > Max)
	    {
	      Max = hlp;
	      cnt = 1;
	    }
	  else if(hlp == Max)
	    cnt ++;
	}
      cout << "Case #" << counter << ": " << Max << ' ' << cnt << endl ;
    }
}
