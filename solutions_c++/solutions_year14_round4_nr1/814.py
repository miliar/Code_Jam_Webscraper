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
const int N = 10007;
int p[N];
int main()
{
  int T;
  scanf("%d", &T);
  for( int t = 0; t < T; ++t )
    {
      int n, x;
      scanf("%d%d", &n, &x);
      for( int i = 0; i < n; ++i )
	{
	  scanf("%d", p + i );
	}
      sort( p, p + n );
      int ans(0);
      for( int i = 0, j = n - 1; i <= j; )
	{
	  if( i == j )
	    {
	      ++ans;
	      break;
	    }
	  else if( p[i] + p[j] <= x )
	    {
	      ++i;
	      --j;
	      ++ans;
	    }
	  else
	    {
	      --j;
	      ++ans;
	    }
	}
      printf("Case #%d: %d\n", t + 1, ans);
    }
  return 0;
}
