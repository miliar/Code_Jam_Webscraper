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
  fo(tt, ttt) {
    int n = getint();
    double tgtVol = getdouble(), tgtTemp = getdouble();
    double tgtEnergy = tgtVol * tgtTemp;
    vector< pair<double,double> > a;
    fi(n) {
      double x = getdouble(), y = getdouble();
      a.pb(mp(x, y));
    }
    sort(a.begin(), a.end(), [](const pair<double,double>& a, const pair<double,double>& b) {
        return a.y < b.y;
    });
/*
    fi(sz(a))
      fprintf(stderr, "a[%d] = (%.3lf, %.3lf)\n", i, a[i].x, a[i].y);
*/
    if (a[0].y > tgtTemp || a.back().y < tgtTemp) {
      printf("Case #%d: IMPOSSIBLE\n", tt + 1);
      continue;
    }

    double minRate = a[0].x, sumRate = a[0].x;
    fr(i,1,n) {
      minRate = min(minRate, a[i].x);
      sumRate += a[i].x;
    }
    double tlo = tgtVol / sumRate, thi = tgtVol / minRate;
    // fprintf(stderr, "tlo = %.3lf, thi = %.3lf\n", tlo, thi);
    fo(t_it, 100) {
      double time = (tlo + thi) / 2;

      // check can be colder / hotter
      double minSumEnergy = 0, blahVol = 0;
      fi(sz(a)) {
        double use = min(time, (tgtVol - blahVol) / a[i].x);
        blahVol += use * a[i].x;
        minSumEnergy += use * a[i].x * a[i].y;
      }
      double maxSumEnergy = 0; blahVol = 0;
      fd(i,sz(a)) {
        double use = min(time, (tgtVol - blahVol) / a[i].x);
        blahVol += use * a[i].x;
        maxSumEnergy += use * a[i].x * a[i].y;
      }
      if (minSumEnergy * (1 - 1e-15) > tgtEnergy || maxSumEnergy * (1 + 1e-15) < tgtEnergy) {
        tlo = time;
        continue;
      }
      thi = time;
/*
      double botlo = -0.5, bothi = time * a.size() + 0.5;
      fo(bot_it, 100) {
        double bot = (botlo + bothi) / 2;
        double togo = bot, curVol = 0, curEnergy = 0;
        fi(sz(a))
          if (togo > 0) {
            double use = min(togo, time);
            curVol += use * a[i].x;
            curEnergy += use * a[i].x * a[i].y;
            togo -= use;
          }
        if (curVol > tgtVol) {
          bothi = bot;
          continue;
        }
        fd(i,sz(a))
          if (curVol < tgtVol) {
            double use = min(time, (tgtVol - curVol) / a[i].x);
            curVol += use * a[i].x;
            curEnergy += use * a[i].x * a[i].y;
          }
        if (curEnergy < tgtEnergy) {
          bothi = bot;
        } else {
          botlo = bot;
        }
      }
      if (botlo < 0 || bothi > time * a.size()) {
        tlo = time;
      } else {
        thi = time;
      }
*/
    }
    printf("Case #%d: %.12lf\n", tt + 1, tlo);
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










