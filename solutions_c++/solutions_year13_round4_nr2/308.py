
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

//*********************** SOLUTION    ******************************

main ()
{
  cin.sync_with_stdio(false);
  //ifstream cin("0.in");
  cout.sync_with_stdio(false);
  int cTest; cin >> cTest;
  rep2(iTest, 1, cTest) {
    Int nRes = 0;
    Int n, p; cin >> n >> p;
    if (bDebug) cerr << deb(iTest) << deb(n) << deb(p) << deb(1<<n) << endl;
    Int cAll = (1LL << n);
    Int cMustBeBetterThan = (1LL << n) - p;
    Int cMustHavePlace = p - 1;

    Int cWins = 0;
    Int cRecord = (1LL<<n) - 1; // record == place, let's start with losing
                                // all
    Int nRoundBit = 1LL << (n-1);
    while (cRecord > cMustHavePlace) {
      cWins++;
      cRecord ^= nRoundBit;
      nRoundBit >>= 1;
    }
    Int n2 = cAll - 1;
    Int x = 1;
    while (cWins) {
      n2 -= x;
      x *= 2;
      cWins--;
    }

    Int cLoss = 0;
    cRecord = 0; // starting with winning all
    Int cLosses = 0;
    nRoundBit = 1LL << (n-1);
    while (cRecord <= cMustHavePlace) {
      cLosses++;
      cRecord ^= nRoundBit;
      if (!nRoundBit) break;
      nRoundBit >>= 1;
    }
    if (bDebug) cerr << deb(cMustBeBetterThan) << deb(cMustHavePlace)
      << deb(cWins) << deb(cLosses) << endl;
    // if we may force him to loose cLosses, then he can't always be winner
    // so he must be granted to lose max cLosses - 1 times
    Int n1 = 0;
    x = 2;
    while (cLosses-1) {
      n1 += x;
      x *= 2;
      cLosses--;
    }
    if (n1 >= cAll) n1 = cAll - 1;
    
    cout << "Case #" << iTest << ": " << n1 << " " << n2 << endl;
  }
}

// :collapseFolds=1:folding=explicit:

// :collapseFolds=1:folding=explicit:
