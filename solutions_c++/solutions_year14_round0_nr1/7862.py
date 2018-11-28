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

int T, fi, se;
set<int> s, t;
vector<int> ans;

int main ()
{
  scanf("%d", &T);
  for(int counter = 1 ; counter <= T ; counter++)
    {
      s.clear();
      t.clear();
      ans.resize(0);
      scanf("%d", &fi);
      fi --;
      for(int i = 0 ; i < 4 ; i++)
	for(int x, j = 0 ; j < 4 ; j++)
	  {
	    scanf("%d", &x);
	    if(i == fi)
	      s.insert(x);
	  }
      scanf("%d", &se);
      se --;
      for(int i = 0 ; i < 4 ; i++)
	for(int x, j = 0 ; j < 4 ; j++)
	  {
	    scanf("%d", &x);
	    if(i == se)
	      t.insert(x);
	  }
      for(int i = 1 ; i <= 16 ; i++)
	if(s.find(i) != s.end() && t.find(i) != t.end())
	  ans.push_back(i);
      printf("Case #%d: ", counter);
      if(ans.size() > 1)
	printf("Bad magician!\n");
      else if(ans.size() == 0)
	printf("Volunteer cheated!\n");
      else
	printf("%d\n", ans[0]);
    }
}
