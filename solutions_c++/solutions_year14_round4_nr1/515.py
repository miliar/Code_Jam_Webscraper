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

int tests, n, x;
vector<int> vc;

int main ()
{
  ios_base :: sync_with_stdio(0);
  cin >> tests ;
  for(int counter = 1 ; counter <= tests ; counter++)
    {
      cin >> n >> x ;
      vc.resize(n);
      for(int i = 0 ; i < n ; i++)
	cin >> vc[i] ;
      int ret = 0;
      sort(vc.begin(), vc.end());
      for(int i = 0 ; i < vc.size() ; i++)
	{
	  ret ++;
	  if(i + 1 < vc.size() && vc[i] + vc[i + 1] <= x)
	    {
	      int j = i + 1;
	      while(j < vc.size() && vc[j] + vc[i] <= x)
		j ++;
	      j --;
	      vc.erase(vc.begin() + j);
	    }
	}
      cout << "Case #" << counter << ": " << ret << endl ;
    }
}
