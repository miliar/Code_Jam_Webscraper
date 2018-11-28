#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <fstream>
#include <cassert>
#include <set>
#include <queue>
#include <iostream>
#include <utility>
#include <stack>
#include <complex>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <list>
#include <functional>
#include <cctype>
//#include <unordered_set>
//#include <unordered_map>
using namespace std;
typedef long double ld;
typedef long long ll;
typedef pair<int,int> ppi;
typedef pair<ll,ll> ppl;
typedef pair<double,double> ppd;
#define PB push_back
#define MP make_pair
#define FIR first
#define SEC second
#define FOR(a,b,c) for(int a=(b);a<(c);++a)
#define FR(a,b) for(typeof(b.begin()) a=b.begin();a!=b.end();++a)
const int N = 1007;
int p[N];
int q[N];
void add( int v, int val )
{
  for( int i = v; i < N; i += ( i & (-i) ) )
    {
      q[i] += val;
    }
}
int que( int v )
{
  int r(0);
  for( ; v; v ^= ( v & ( -v ) ) )
    {
      r += q[v];
    }
  return r;
}
int main()
{
  int T;
  scanf("%d", &T);
  for( int t = 0; t < T; ++t )
    {
      int n;
      scanf("%d", &n);
      set< pair<int,int> > sett;
      memset( q, 0, sizeof(q) );
      for( int i = 0 ; i < n; ++i )
	{
	  scanf("%d", p + i);
	  sett.insert( make_pair( p[i], i ) );
	  add( i + 1, 1 );
	}
      int ans(0);
      for( int left = n; !sett.empty(); --left)
	{
	  int pos = sett.begin()->second;
	  sett.erase( sett.begin() );
	  int num = que( pos );
	  int tmp = min( num, left - 1 - num );
	  // cout << tmp << ' ' << num << endl;
	  ans += tmp;
	  add( pos + 1, -1 );
	}
      printf("Case #%d: %d\n", t + 1, ans);
    }
  return 0;
}
