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
const int M = 100;
const int N = 4;
char s[M][107];
vector<int> p[N];
int m, n;
int mNode, cnt;
int qoi[N];
int q[N][ 107 * M ][ 'Z' - 'A' + 7 ];
bool out;
void add( int id, char st[] )
{
  for( int g = 0, j = 0; ; ++j )
    {
      if( st[j] == '\0' )
	break;
      int c = st[j] - 'A';
      // if( c < 0 )
      // 	c = 'Z' + 1;
      if( q[id][g][c] == 0 )
	{
	  q[id][g][c] = ++qoi[id];
	  memset( q[id][ qoi[id] ], 0, sizeof( q[id][ qoi[id] ] ) );
	}
      g = q[id][g][c];
    }
}
void dfs( int v )
{
  if( v == m )
    {
      int c(0);
      for( int i = 0; i < n; ++i )
	if( p[i].size() )
	  {
	    qoi[i] = 0;
	    memset( q[i][0], 0, sizeof( q[i][0] ) );
	    for( int j = 0; j < p[i].size(); ++j )
	      {
		add( i,  s[ p[i][j] ] );
	      }
	    c += ( qoi[i] + 1 );
	  }
      if( c > mNode )
	{
	  mNode = c;
	  cnt = 1;
	}
      else if( c == mNode )
	++cnt;
    }
  else
   for( int i = 0; i < n; ++i )
     {
       p[i].push_back(v);
       dfs( v + 1 );
       p[i].pop_back();
     }
}
int main()
{
  // char a[] = "BAB";
  // char b[] = "B";
  // add( 0, a);
  // add( 0, b);
  // cout << qoi[0] << endl;
  // return 0;
  ios::sync_with_stdio(false);
  int T;
  scanf("%d", &T);
  for( int t = 0; t <T; ++t )
    {
      scanf("%d%d", &m, &n);
      for( int i = 0; i < m; ++i )
	scanf("%s", s[i]);
      mNode = 0;
      cnt = 0;
      dfs( 0 );
      printf("Case #%d: %d %d\n", t + 1, mNode, cnt);
    }
  return 0;
}
