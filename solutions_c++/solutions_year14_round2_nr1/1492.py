#pragma GCC diagnostic ignored "-Wwrite-strings"
//#pragma GCC diagnostic ignored "-Wc++11-extensions"

#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <climits>
#include "stdarg.h"
#include <bitset> //http://stackoverflow.com/questions/4048749/bitwise-operations-on-vectorbool //http://www.drdobbs.com/the-standard-librarian-bitsets-and-bit-v/184401382
#include <numeric> //http://stackoverflow.com/questions/6743003/how-calculate-sum-of-values-in-stdvectorint
#include <iomanip> // cout << fixed << setprecision(8);

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef vector<PII> VPII;
typedef vector<PDD> VPDD;
typedef vector <VI> VVI;
typedef vector<VD> VVD;
typedef vector <string> VS;
typedef vector <bool> VB;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

#define CE cout << endl;
#define CL cout << "--------------------------------------" << endl;
#define ASF assert(false);
#define V vector
#define DQ deque
#define PQ priority_queue

template <class T, class U>
ostream & operator << (ostream &out, const pair<T,U> &A) {
  out << A.ST << "_" << A.ND; return out;
}

template<template<typename, typename> class ContainerT, typename ValueT> //http://cboard.cprogramming.com/cplusplus-programming/145441-stl-container-template-argument.html
ostream & operator << (ostream &out, const ContainerT<ValueT, std::allocator<ValueT> > &A) {
  FORE(i, A) out << *i << " "; return out;
}

template<template<typename, typename> class ContainerT, typename ValueT, typename ValueU> 
ostream & operator << (ostream &out, const ContainerT<pair<ValueT, ValueU>, std::allocator<pair<ValueT, ValueU> > > &A) {
  FORE(i, A) out << *i << " "; return out;
}


#define VA_NARGS_IMPL(_1,_2,_3,_4,_5,_6,_7,_8,N,...) N
#define VA_NARGS(...) VA_NARGS_IMPL(__VA_ARGS__, 8, 7, 6, 5, 4, 3, 2, 1)

#define P_(a)                       #a << ": " << a
#define P__(a)                      " | " << P_(a)
#define P1(a)                       cout << P_(a) << endl;
#define P2(a, b)                    cout << P_(a) << P__(b) << endl;
#define P3(a, b, c)                 cout << P_(a) << P__(b) << P__(c) << endl;
#define P4(a, b, c, d)              cout << P_(a) << P__(b) << P__(c) << P__(d) << endl;
#define P5(a, b, c, d, e)           cout << P_(a) << P__(b) << P__(c) << P__(d) << P__(e) << endl;
#define P6(a, b, c, d, e, f)        cout << P_(a) << P__(b) << P__(c) << P__(d) << P__(e) << P__(f) << endl;
#define P7(a, b, c, d, e, f, g)     cout << P_(a) << P__(b) << P__(c) << P__(d) << P__(e) << P__(f) << P__(g) << endl;
#define P8(a, b, c, d, e, f, g, h)  cout << P_(a) << P__(b) << P__(c) << P__(d) << P__(e) << P__(f) << P__(g) << P__(h) << endl;

#define P_IMPL2(count, ...) P ## count (__VA_ARGS__)
#define P_IMPL(count, ...) P_IMPL2(count, __VA_ARGS__) 
#define P(...) P_IMPL(VA_NARGS(__VA_ARGS__), __VA_ARGS__)

template<class T> void mini(T &a, const T &b) {if(b<a)a=b;}
template<class T> void maxi(T &a, const T &b) {if(b>a)a=b;}

typedef V<pair<char, int> > VPCI;
int N;
VS A;
V<VPCI> B;
VPCI digest(string x) {
  VPCI ret;
  char cur = 0;
  int stk = 0;
  REP(i, x.size()) {
    if(cur != x[i]) {
      if(stk) ret.PB(MP(cur, stk));
      cur = x[i]; 
      stk = 1;
    }
    else if(cur == x[i]) stk++;
  }
  ret.PB(MP(cur, stk));
  return ret;
}

int calc(int idx) {
  VI list;
  REP(i, N) list.PB(B[i][idx].ND);
  sort(ALL(list));
  int cand[2] = {list.size()/2, list.size()/2-1};
  int ret = INT_MAX;
  REP(i, 2) {
    int cur = 0;
    FORE(j, list) cur += abs(*j - list[cand[i]]);
    mini(ret, cur);
  }
  return ret;
}

string solve() {
  cin >> N;
  int ans = 0;
  A = VS(N); REP(i, N) cin >> A[i];
  B.clear();
  FORE(i, A) B.PB(digest(*i));
  REP(i, N) {
    if(B[0].size() != B[i].size()) return "Fegla Won";
    REP(j, B[0].size())
      if(B[0][j].ST != B[i][j].ST) return "Fegla Won";
  }
  REP(i, B[0].size())
    ans += calc(i);
  return to_string(ans);
}

int main() {
  int T; cin >> T; REP(i, T)
  cout << "Case #" << i+1 << ": " << solve() << endl;
  return 0;
}















