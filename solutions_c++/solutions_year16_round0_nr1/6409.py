#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>
#include <cstring>

using namespace std;

#define ll          long long
#define VI          vector<int>
#define ALL(a)      (a).begin(), (a).end()
#define SORT(a)     sort( ALL(a) )
#define PB          push_back
#define FOR(i,a,b)  for( int i = (a); i < (int)(b); i++ )
#define dump_(x)     cerr << #x << " = " << (x) << " ";
#define dump(x)     cerr << #x << " = " << (x) << endl
#define dump_vec(x) FOR(zZz,0,x.size()) cout << x[zZz] << " "; cout << endl


template< typename type > type readOne()
{
  type res;
  char inp[5000];
  char* dum = fgets( inp, sizeof( inp ), stdin );
  stringstream ss( dum );
  ss >> res;
  return res;
}

template< typename type > vector<type> readMulti()
{
  vector<type> res;
  char inp[5000];
  char* dum = fgets( inp, sizeof( inp ), stdin );
  stringstream ss( dum );
  for ( type t; ss >> t; )
    res.push_back( t );
  return res;
}

//
//
// LET'S START
//
//

string doit(ll N) {
  if (N == 0) return "INSOMNIA";
  ll ans = 0;
  int mask = 0;
  for (int i = 1; ; i++) {
    ll k = N * i;
    //printf("k = %lld, mask=0x%x(%d)\n", k, mask, mask);
    while (k) {
      int t = k % 10;
      mask |= 1 << t;
      if (mask == 1023) {
	ans = N * i;
	break;
      }
      k /= 10;
    }
    if (ans > 0)
      break;
  }
  
  stringstream ss;
  ss << ans;
  return ss.str();
}

string doCase()
{
  //
  // DOIT!
  //
  ll N = readOne<ll>();
  return doit(N);
}

int main()
{
#if 0
  for (int i = 0; i <= 1000000; i++) {
    cout << i << " " << doit(i) << endl;
  }
#endif
  
  int cases = readOne<int>();
  for (int caseno = 1; caseno <= cases; caseno++)
    cout << "Case #" << caseno << ": " << doCase() << endl;
  return 0;
}

