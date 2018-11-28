/*
#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif
*/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <unordered_set>
#include <utility>
#include <time.h>
#include <vector>
// #include <sys/time.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define x first
#define y second
#define fi(n) fo(i, n)
#define fj(n) fo(j, n)
#define fk(n) fo(k, n)
#define fd(i,n) for(int i=(int)(n)-1;i>=0;--i)
#define fo(i,n) fr(i,0,n)
#define fr(i,a,b) for(int i=(int)(a); i<(int)(b); i++)
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define srt(x) sort(all(x))
//#define lgLowestBit(x) __builtin_ctz(x)
//#define bitCount(x) __builtin_popcount(x)
//#define foreach(it, a) for(__typeof((a).begin()) it=(a).begin(); it != (a).end(); it++)
//#define me (*this)
//#define PQ(t) priority_queue< t, vector< t >, greater< t > >
//#define CLR(a, v) memset(a, v, sizeof(a))
//#define UNIQUE(a) srt(a), a.resize(unique(all(a))-a.begin())
//#define RAND (((double)rand()/RAND_MAX) + ((double)rand()/RAND_MAX/RAND_MAX))
//#define assert(cond,msg) if(!(cond)){ fprintf(stderr, "assert failed at line %d: %s\n", __LINE__, msg); exit(1); }
/*
char systemBuffer[1<<10];
#define execute(...) {\
  sprintf(systemBuffer, __VA_ARGS__); \
  system(systemBuffer); \
}

#ifdef LOCAL
  #define debug(msg, ...) fprintf(stderr, msg, __VA_ARGS__)
#else
  #define debug(msg, ...)
#endif
*/

typedef long long ll;
typedef pair<int, int> ii;
typedef vector< ii > vii;
typedef vector< vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;
typedef vector< string > vs;
typedef vector< double > vd;
typedef vector< vd > vvd;
typedef vector< ll > vll;
typedef vector< bool > vb;

const int INF = 1000*1000*1000+7;
const double EPS = 1e-9;
const double PI = acos(-1.0);
template<class T> int chmin(T &t, T f){ return (t>f) ? (t=f, 1) : 0; }
template<class T> int chmax(T &t, T f){ return (t<f) ? (t=f, 1) : 0; }

/* 
struct timeval startTime, finishTime;
double timeElapsed(){
  gettimeofday(&finishTime, NULL);
  int top = finishTime.tv_sec-startTime.tv_sec-(startTime.tv_usec > finishTime.tv_usec);
  int bot = finishTime.tv_usec-startTime.tv_usec;
  if(bot < 0)
    bot += 1e6;
  return top+bot/1e6;
}
*/
inline int getint() {
  int a;
  return scanf("%d", &a) ? a : (fprintf(stderr, "trying to read\n"),-1);
}

inline double getdouble() {
  double a;
  return scanf("%lf", &a) ? a : (fprintf(stderr, "trying to read\n"),-1);
}






void myCode() {
  cout.precision(20);
  int ttt = getint();
  fo (tt, ttt) {
    int n = getint();
    string s;
    getline(cin, s);
    vector< string > dict;
    vector< vector< string > > a(n);
    vvi b(n);
    fi(n) {
      getline(cin, s);
      stringstream ss(s);
      while(ss >> s)
        a[i].pb(s);
    }
    fi(n)
      fj(sz(a[i]))
        dict.pb(a[i][j]);
    sort(dict.begin(), dict.end());
    dict.resize(unique(dict.begin(), dict.end()) - dict.begin());
    fi(n) {
      fj(sz(a[i]))
        b[i].pb(lower_bound(dict.begin(), dict.end(), a[i][j]) - dict.begin());
      sort(b[i].begin(), b[i].end());
      b[i].resize(unique(b[i].begin(), b[i].end()) - b[i].begin());
    }

    fprintf(stderr, "here\n");

    int ret = INF;
    int mcost = 0;
    unordered_set<int> mzero, mone;
    fj(sz(b[0]))
      mzero.insert(b[0][j]);
    fj(sz(b[1]))
      mone.insert(b[1][j]);
    for (const int t : mzero)
      if (mone.count(t))
        ++mcost;
    fi(1<<n) if((i&3) == 1) {
      unordered_set<int> zero, one;
      fr(j,2,n)
        if (i&(1<<j)) {
          fk(sz(b[j]))
            if (!mone.count(b[j][k]))
              one.insert(b[j][k]);
        } else {
          fk(sz(b[j]))
            if (!mzero.count(b[j][k]))
              zero.insert(b[j][k]);
        }
      int cost = 0;
      for (const int t : zero)
        if (one.count(t) || mone.count(t))
          ++cost;
      for (const int t : one)
        if (mzero.count(t))
          ++cost;
      ret = min(ret, cost);
    }
    printf("Case #%d: %d\n", tt + 1, ret + mcost);
  }
}

int main() {
/*
  // seed the random number generator with microseconds
  gettimeofday(&startTime, NULL);
  srand(startTime.tv_usec);
*/
  myCode();
  return 0;
}










