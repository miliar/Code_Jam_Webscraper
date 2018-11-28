/*
#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif
*/
// #include<bits/stdc++.h>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
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



void merge(map<int,int>& ret, const map<int,int>& other) {
  for (const auto& pr : other)
    ret[pr.x] += pr.y;
}

// map contains min acceptable
void add(map<int,int>& m, int salary, int d) {
  int frontDrop = 0, backDrop = 0;
  while (!m.empty() && m.begin()->x < salary - d) {
    frontDrop += m.begin()->y;
    m.erase(m.begin());
  }
  while (!m.empty() && m.rbegin()->x > salary) {
    backDrop += m.rbegin()->y;
    m.erase(--m.end());
  }
  m[salary - d] += frontDrop + 1;
  m[salary + 1] += backDrop - 1;
}

map<int,int> dfs(int i, const vector<ll>& salary, const vvi& children, int d) {
  map<int,int> ret;
  // fprintf(stderr, "dfs(%d)\n", i);
  if (!children[i].empty()) {
    int bigChild = -1;
    for (int j : children[i])
      if (bigChild == -1 || sz(children[j]) > sz(children[bigChild]))
        bigChild = j;
    ret = dfs(bigChild, salary, children, d);
    for (int k : children[i])
      if (k != bigChild)
        merge(ret, dfs(k, salary, children, d));
  }
  add(ret, salary[i], d);
/*
  fprintf(stderr, "%d: ", i);
  for (auto& pr : ret)
    fprintf(stderr, "<%d, %d> ", pr.x, pr.y);
  fprintf(stderr, "\n");
*/
  return ret;
}

void myCode() {

  int ttt = getint();
  fo (tt, ttt) {
    int n = getint(), d = getint();
    ll s0 = getint(), as = getint(), cs = getint(), rs = getint();
    ll m0 = getint(), am = getint(), cm = getint(), rm = getint();
    vector<ll> s(1, s0), m(1, m0);
    fi(n-1) {
      s.pb((s.back() * as + cs) % rs);
      m.pb((m.back() * am + cm) % rm);
    }
/*
    fi(n)
      fprintf(stderr, "%d: s = %d, m = %d\n", i, s[i], m[i]);
      */
/*
    n = 5;
    d = 2;
    s = {10, 9, 12, 11, 12};
    m = {-1, 0, 1, 0, 3};
*/
    vector<int> z(n);
    vvi children(n);
    fr(i,1,n) {
      children[m[i]%i].pb(i);
      // fprintf(stderr, "child(%d).pb(%d) -- m[i] = %d\n", m[i]%i, i, m[i]);
    }
/*
    fi(sz(children)) {
      fprintf(stderr, "children %d:", i);
      fj(sz(children[i]))
        fprintf(stderr, " %d", children[i][j]);
      fprintf(stderr, "\n");
    }
*/
    for(int i = n-1; i > 0; --i) {
      z[m[i]%i] += ++z[i];
    }
    map<int,int> ret = dfs(0, s, children, d);
    int peak = 0, sum = 0;
    for(auto& pr : ret) {
      sum += pr.y;
      peak = max(peak, sum);
    }
    printf("Case #%d: %d\n", tt + 1, peak);
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










