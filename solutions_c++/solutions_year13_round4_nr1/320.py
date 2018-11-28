
//(C) Jarek Czekalski 2012-13

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <algorithm>
#include <bitset>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <vector>

using namespace std;

// debugging stuff {{{
#ifdef DEBUG
  #define bDebug 1
  #define bDebug2 1
#else
  #define bDebug 0
  #define bDebug2 0
#endif
#define deb(a) #a << "=" << (a) << " "
#ifndef HOME
  #define assert(a) {}
#endif

template<class T> ostream& operator<<(ostream& os, vector<T> v) //{{{
{
  for(int i=0; i<v.size(); i++)
    os << v[i] << " ";
  os << endl;
  return os;
}  //}}}
// }}} end of debugging stuff

#define array(a, type, count) type *a = (type*)calloc(sizeof(type), count)
#define eps 1e-9
#define eq(a, b) ( (a) > (b) - eps && (a) < (b) + eps )
#define eraseAll(v) v.erase(v.begin(), v.end())
#define fi first
#define rep(i,n) for(long i=0; i<(n); i++)
#define rep2(i,a,b) for(long i=(a); i<=(b); i++)
#define rep2d(i,a,b) for(long i=(a); i>=(b); i--)
#define zeroMem(a) memset(a, 0, sizeof(a))
#define zeroMem2(a, n) memset(a, 0, sizeof(*a) * n)
#define fore(it,L) for(typeof(L.begin()) it=L.begin(); it!=L.end(); it++)
#define eraseAll(v) v.erase(v.begin(), v.end())
#define se second
#define setMin(a,b) { typeof(a) rv = (b); if (rv < a) a = rv; }
#define setMinP(a,b) { typeof(a) rv = (b); \
                       if (rv >= 0 && (a < 0 || rv < a)) a = rv; }
#define setMax(a,b) { typeof(a) rv = (b); if (rv > a) a = rv; } 
#define swap(a,b) { typeof(a) swapVar = a; a = b; b = swapVar; }
#define Int long long
#define D 1000002013
#define sumD(x,y) { x = ((x) + (y)) % D; if ((x) < 0) x += D; }
#define mulD(x,y) { x = ((x) * (y)) % D; if ((x) < 0) x += D; }
#define pii pair<Int, Int>

//*********************** SOLUTION    ******************************
Int cost(Int n, Int c)
{
  if (c == 0)
    return 0;
  Int d = c - 1;
  return ((d+1) * (2 * n - d) / 2) % D;
}

main ()
{
  cin.sync_with_stdio(false);
  //ifstream cin("0.in");
  cout.sync_with_stdio(false);
  int cTest; cin >> cTest;
  rep2(iTest, 1, cTest) {
    if (bDebug) cerr << deb(iTest) << endl;
    Int nRes = 0;
    Int n, m; cin >> n >> m;
    vector<pii> ve;
    rep(i, m) {
      Int nIn, nOut, c; cin >> nIn >> nOut >> c;
      Int nCost = c * cost(n, nOut - nIn) % D;
      sumD(nRes, nCost);
      ve.push_back(make_pair(nIn, c));
      ve.push_back(make_pair(nOut, (1LL<<32) + c));
    }
    sort(ve.begin(), ve.end());
    
    list<pii> vTick;
    fore(it, ve) {
      bool bIn = (it->se < (1LL<<32));
      Int a = it->fi;
      Int c = (it->se & ((1LL<<32)-1));
      // cerr << deb(bIn) << deb(a) << deb(c) << endl;
      if (bIn) {
        vTick.push_back(make_pair(a, c));
      } else {
        // time to pay
        while (c) {
          pii &pa = vTick.back();
          Int c2 = min(c, pa.se);
          c -= c2;
          pa.se -= c2;
          assert(a >= pa.fi);
          sumD(nRes, - ((c2 * cost(n, a - pa.fi)) % D));
          if (pa.se == 0) vTick.pop_back();
          // cerr << deb(c) << deb(c2) << deb(pa.fi) << deb(pa.se) << endl;
        }
      }
    }
    // cerr << deb(vTick.size()) << endl;
    // if (vTick.size()) cerr << deb(vTick.front().fi) << deb(vTick.front().se)
      // << endl;
    assert(vTick.size() == 0);
    
    cout << "Case #" << iTest << ": " << nRes << endl;
  }
}

// :collapseFolds=1:folding=explicit:
