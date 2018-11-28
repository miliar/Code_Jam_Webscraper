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
vector<int> ans;
int a[4][4];
int b[4][4];
int y;
void solve( )
{
  ans.clear();
  int ch[2];
  cin >> ch[0];
  for( int i = 0 ; i < 4; i ++)
    {
      for( int j = 0 ; j < 4; j ++)
	cin >> a[i][j];
    }
  ch[0] --;
  cin >> ch[1];
  for(int i = 0 ;i < 4; i ++)
    for(int j = 0 ; j  < 4; j ++)
      cin >> b[i][j];
  ch[1] --;
  for(int i = 0 ; i < 4; i ++)
    {
      for(int j = 0; j < 4; j ++)
	{
	  if(a[ch[0]][i] == b[ch[1]][j])
	    ans.pb(a[ch[0]][i]);
	}
    }
  cout << "Case #" << y + 1 << ": ";
  if( SZ(ans) > 1)
    {
      cout << "Bad magician!" << endl;
      return;
    }
  if(!SZ(ans))
    {
      cout << "Volunteer cheated!" << endl;
      return ;
    }
  cout << ans[0] << endl;
}
int main()
{
  int t;
  cin >> t;
  for(y = 0 ; y< t; y  ++)
    {
      solve();
    }
  return 0;
}

