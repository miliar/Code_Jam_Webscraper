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

int doit(string S) {
    int res = 0;
    while (true) {
	bool ok = true;
	for (int i = 0; i + 1 < S.size(); i++) {
	    if (S[i] != S[i+1]) {
		ok = false;
		res++;
		for (int j = 0; j <= i; j++) {
		    S[j] = (int)'+' + '-' - S[j];
		}
		break;
	    }
	}
	if (ok) break;
    }
    if (S[0] == '-') res++;
    return res;
}

int doCase()
{
  //
  // DOIT!
  //
  string S = readOne<string>();
  return doit(S);
}

int main()
{
  int cases = readOne<int>();
  for (int caseno = 1; caseno <= cases; caseno++)
    cout << "Case #" << caseno << ": " << doCase() << endl;
  return 0;
}

