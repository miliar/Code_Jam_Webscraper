#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

#define debug(x) cerr<<#x<<" = "<<(x)<<endl;

using namespace std;
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define VAR(a,b) __typeof(b) a=(b)
#define REVERSE(c) reverse(ALL(c))
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define MINN(X,Y) ((X) > (Y) ? (Y) : (X))
#define MAXX(X,Y) ((X) < (Y) ? (Y) : (X))
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

int a[1000][1000];

void solve()
{
  int n, m;
  cin>>n>>m;
  int s=1;
  for(int i=0; i<n; i++)
    {
      for(int j=0; j<m; j++)
	{
	  cin>>a[i][j];
	}
    }
  string r="YES";

   for(int i=0; i<n; i++)
    {
      for(int j=0; j<m; j++)
	{
	  bool Hgood = true;
	  bool Vgood = true;
	  for(int k=0; k<m; k++)
	    {
	      if( a[i][k] > a[i][j] )
		{
		  Hgood =false;
		  break;
		}
	    }
	  for( int k=0; k<n; k++)
	    {
	      if( a[k][j] > a[i][j] )
		{
		  Vgood =false;
		  break;
		}
	    }
	  
	  if( !Hgood && !Vgood)
	    {
	      r = "NO";
	    }
	  
	}
    }
   cout<<r<<endl;
}

int main()
{
  int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ", t);
        solve();
    }
  return 0;
}
