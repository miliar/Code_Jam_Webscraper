#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iterator>
#define FOR(i,a,n) for(int i = (a); i < (int)(n); ++i)
#define foreach(itr,c) for(decltype((c).begin()) itr=(c).begin(); itr != (c).end(); itr++)
#define mp(a,b) make_pair(a,b)

using namespace std;

//typedef __int64 ll;
//typedef unsigned __int64 ull;
typedef long long ll;
typedef unsigned long long ull;


template<typename T>
inline T ABS(T a) { return a > 0 ? a : -a; }
template<typename T>
inline T MIN(T a, T b) { return a < b ? a : b; }
template<typename T>
inline T MAX(T a, T b) { return a > b ? a : b; }
template<typename T>
inline T CHKMIN(T &a, T b) { if(a > b) a = b; return a; }
template<typename T>
inline T CHKMAX(T &a, T b) { if(a < b) a = b; return a; }
template<typename T>
inline void SWAP(T &a, T &b) { static T c; c = a; a = b; b = c; }

template<typename T, typename... T0>
T MAX(T a, T b, T0... c) { return a > b ? MAX(a, c...) : MAX(b, c...); }
template<typename T, typename... T0>
T MIN(T a, T b, T0... c) { return a < b ? MIN(a, c...) : MIN(b, c...); }

template<typename T, int n>
void myin(T a[]) { FOR(i, 0, n) cin >> a[i]; }
template<typename T>
void myin(T &a) { cin >> a; }

template<typename T>
void print(T a) { cout << a << ' '; }
template<typename T, typename... T0>
void print(T a, T0... b) { print(a); print(b...); }
template<typename T>
void println(T a) {cout << a << endl;}
template<typename T, typename... T0>
void println(T a, T0... b) { print(a); println(b...); }



#define FILEIO 
#define FILENAME "B-large"

void iofunc() {
#ifdef FILEIO
  freopen( FILENAME ".in", "r", stdin);
  freopen( FILENAME ".out", "w", stdout);
#endif
}

int n, in[2000], ind[1010];

int f(int t) {
  int ret = 0;
  memset(ind, 0, sizeof(ind));
  FOR(i, 0, n) ind[in[i]]++;
  FOR(i, t + 1, 1010) {
    if(!ind[i]) continue;
    int tmp = (i + t - 1) / t - 1;
    ret += tmp * ind[i];
  }
  return ret;
}

int main() {
  iofunc();
  int t;
  cin >> t;
  FOR(tt, 1, t + 1) {
    memset(ind, 0, sizeof(ind));
    cin >> n;
    FOR(i, 0, n) {
      cin >> in[i];
      ind[in[i]]++;
    }
    
    int ans = 1000;
    for(int i = 1000; i > 0; --i) {
      ans = MIN(ans, i + f(i));
    }
    
    printf("Case #%d: %d\n", tt, ans);
  }

}
