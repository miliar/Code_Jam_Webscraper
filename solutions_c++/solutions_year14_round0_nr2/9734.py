
//(C) Jarek Czekalski 2012-14

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

Int matches(string s, string t)
{
  Int bOk = 1;
  Int it = 0;
  rep(is, s.size()) {
    if (t[it] == '(') {
      int bOk2 = 0;
      while(t[it] != ')') {
        if (s[is] == t[it]) bOk2 = 1;
        it++;
      }
      if (!bOk2) bOk = 0;
    } else {
      if (s[is] != t[it]) bOk = 0;
    }
    it++;
  }
  if (bDebug) cerr << "matching " << s << " in " << t << endl;
  return bOk;
}

main ()
{
  cin.sync_with_stdio(false);
  //ifstream cin("0.in");
  cout.sync_with_stdio(false);
  Int cTest; cin >> cTest;
  rep2(iTest, 1, cTest) {
    if (bDebug) cerr << deb(iTest) << endl;
    double c, f, x; cin >> c >> f >> x;
    double rb = x / 2;
    double s = 0;
    double fc = 2;
    rep(i, 1000000) {
      s += c / fc;
      fc += f;
      double r = s + x / fc;
      setMin(rb, r);
    }

    
    cout << "Case #" << iTest << ": ";
    cout.precision(7);
    cout << fixed;
    cout << rb << endl;
  }
}

// :collapseFolds=1:folding=explicit:
