#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <deque>
#include <iomanip> 
#include <set>
#include <stack>
#include <map>
#include <cstdio>
#include <fstream>
using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define SZ(x) (( (int) x.size() ))

typedef long long ll;
typedef pair < int , int> pie;
const int INF = 1000*1000*100 + 321;
const int maxN = (2<<22);
const int mod = 1000*1000*1000 + 7;
int y;
void solve( )
{
  double c, f, x;
  cin >> c >> f >> x;
  int hi = x + 500, lo = 0;
  double l = x / 2, h;
  double speede = 2.00;
  for(int i = 0; i < hi; i ++)
    {
      h += c/speede;
      speede += f;
    }
  h += x / speede;
  while( abs(hi - lo) > 1)
    {
      int mid = (lo + hi) / 2;
      double speed = 2.00;
      double tim = 0.00;
      for(int i = 0 ; i < mid ; i ++)
	{
	  tim += c / speed;
	  speed += f;
	}
      double timp = tim;
      timp += c / speed;
      tim += x / speed;
      speed += f;
      timp += x / speed;
      //cout << timp << ' ' << tim << endl;
      //return;
      if(tim < timp)
	{
	  h = tim;
	  hi = mid;
	}
      else
	{
	  lo = mid;
	  l = tim;
	}
      
    }
  cout << "Case #" << y + 1 << ": " << min (l , h) << endl;   
}
int main()
{
  int t;
  cin >> t;
  cout << fixed << setprecision(7);
  for(y = 0 ; y< t; y  ++)
    {
      solve();
    }
  return 0;
}

