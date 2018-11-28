/*
 Catalin-Stefan Tiseanu
 
 Pre-written code is assembled from various sources found online.
 Big thanks to the community for that !
*/

// Pre-written code below

using namespace std;

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

//#define DEBUG

#ifdef DEBUG
#define debug(args...)            {dbg,args; cerr<<endl;}
#else
#define debug(args...)              // Just strip off all debug tokens
#endif

struct debugger
{
  template<typename T> debugger& operator , (const T& v)
  {
  cerr<<v<<" ";
  return *this;
  }
} dbg;

// templates
template<typename T> int size(const T& c) { return int(c.size()); }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T> bool remin(T& x, T y) { if (x <= y) return false; x = y; return true; }
template<typename T> bool remax(T& x, T y) { if (x >= y) return false; x = y; return true; }

// misc
#define EPSILON              1e-7

// types
typedef long long            int64;
typedef unsigned long long   uint64;

// shortcuts
#define all(_xx)             _xx.begin(), _xx.end()

#define pb                   push_back
#define vi                   vector<int>
#define vpii                 vector<pair<int,int> >
#define vpdd                 vector<paid<double,double> >

#define pii                  pair<int,int>
#define pdd                  pair<double, double>
#define mp(XX, YY)           make_pair(XX, YY)
#define fi                   first
#define se                   second

#define ll                   long long
#define SS                   stringstream

// for loops
#define re(II, NN)           for (int II(0), _NN(NN); (II) < (NN); ++(II))
#define fod(II, XX, YY)      for (int II(XX), _YY(YY); (II) >= (_YY); --(II))
#define fo(II, XX, YY)       for (int II(XX), _YY(YY); (II) <= (_YY); ++(II))
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

// Useful hardware instructions
#define bitcount             __builtin_popcount
#define gcd                  __gcd

// Useful all around
#define checkbit(n,b)        ( (n >> b) & 1)
#define DREP(a)              sort(all(a));a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)       (lower_bound(all(arr),ind)-arr.begin())

// Code written during the competition below

int will_always_win(int64 mid, int64 N, int64 P) {
  int64 can_beat2 = (mid + 1);
  int64 can_beat = 0;
  while(can_beat2)
    can_beat2 >>= 1, ++can_beat;
  --can_beat;
 
  int64 res = 0;
  re (i, can_beat)
    res += (1LL<<(N-i-1));

  debug("mid = ", mid, "res1 = ", res, can_beat);

  return res < P;
}

int can_win(int64 mid, int64 N, int64 P) {
  int64 can_beat2 = ((1LL<<N)-1) - mid + 1;
  int64 can_beat = 0;
  while(can_beat2)
    can_beat2 >>= 1, ++can_beat;
  --can_beat;
  
  int64 res = 0;
  re (i, N - can_beat)
    res += (1LL<<i);
  
  debug("res2 = ", res);
  
  return res < P;
}

void solve_testcase(int64 N, int64 P) {
  // 1st bs
  
  int64 l = 0, r = (1LL<<N) - 1, mid;
  
  while(l + 1 < r) {
    mid = (l + r) >> 1;
    
    debug(l, mid, r);
    
    if (will_always_win(mid, N, P)) {
      l = mid;
    } else {
      r = mid - 1;
    }
  }
  
  if (will_always_win(l + 1, N, P))
    ++l;
  
  cout << l << " ";
  
  l = 0, r = (1LL<<N) - 1;
  
  while(l + 1 < r) {
    mid = (l + r) >> 1;
    
    debug(l, mid, r);
    
    if (can_win(mid, N, P)) {
      l = mid;
    } else {
      r = mid - 1;
    }
  }
  
  if (can_win(l + 1, N, P))
    ++l;
  
  cout << l;
}

int main() {
  int64 N, P;

  int T; scanf("%d", &T);
  fo (testcase, 1, T) {
    printf("Case #%d: ", testcase);
    
    cin >> N >> P;
    solve_testcase(N, P);
    
    printf("\n");
  }
  return 0;
}
