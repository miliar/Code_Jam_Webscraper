#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
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
#define fi(n) fo(i, n)
#define fj(n) fo(j, n)
#define fk(n) fo(k, n)
#define fd(i,n) for(int i=(int)(n)-1;i>=0;--i)
#define fo(i,n) fr(i,0,n)
#define fr(i,a,b) for(int i=(int)a; i<(int)b; i++)
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define srt(x) sort(all(x))
#define foreach(it, a) for(typeof((a).begin()) it=(a).begin(); it != (a).end(); it++)
#define x first
#define y second
#define me (*this)
#define PQ(t) priority_queue< t, vector< t >, greater< t > >
#define CLR(a, v) memset(a, v, sizeof(a))
#define UNIQUE(a) srt(a), a.resize(unique(all(a))-a.begin())
#define RAND (((double)rand()/RAND_MAX) + ((double)rand()/RAND_MAX/RAND_MAX))
#define assert(cond,msg) if(!(cond)){ fprintf(stderr, "assert failed at line %d: %s\n", __LINE__, msg); exit(1); }

typedef long long ll;
typedef pair<int, int> ii;
typedef vector< ii > vii;
typedef vector< vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;
typedef vector< double > vd;
typedef vector< vd > vvd;
typedef vector< ll > vll;
typedef vector< string > vs;
typedef vector< bool > vb;
const int INF = 1000*1000*1000+7;
const double EPS = 1e-9;
const double PI = acos(-1.0);
template<class T> int chmin(T &t, T f){ return (t>f) ? (t=f, 1) : 0; }
template<class T> int chmax(T &t, T f){ return (t<f) ? (t=f, 1) : 0; }

inline int getint() {
  int a;
  return scanf("%d", &a) ? a : (fprintf(stderr, "trying to read\n"),-1);
}

inline double getdouble() {
  double a;
  return scanf("%lf", &a) ? a : (fprintf(stderr, "trying to read\n"),-1);
}




// sum of squares of digits in one half of the root but be less than 10, else overflows in base 10 and square
// can't be a palindrome

vvi roots; // roots of fair and square numbers

ll nextComb(ll x){ // x = xxx0 1111 0000
  ll smallest = x&-x;        // 0000 0001 0000
  ll ripple = x+smallest;    // xxx1 0000 0000
  ll ones = x^ripple;        // 0001 1111 0000
  ones = (ones>>2)/smallest;  // 0000 0000 0111
  return ripple|ones;         // xxx1 0000 0111
}

char buffer[100];
pair<int,string> makePair(vi &a){
  fk(2*sz(a)-1){
    buffer[k] = '0';
    fi(sz(a)){
      int j = k-i;
      if(j>=0 && j<sz(a))
        buffer[k] += a[i]*a[j];
    }
  }
  buffer[2*sz(a)-1] = 0;
  return mp(2*sz(a)-1, buffer);
}

vi build(ll bitset, int len){
  vi ret(len, 0);
  int upto = 0;
  for(int i=0; upto<len; ++i)
    if(bitset&(1LL<<i))
      ++upto;
    else
      ++ret[upto];
  return ret;
}

vi buildOdd(vi &a){
  vi ret;
  fi(sz(a))
    ret.pb(a[i]);
  fd(i,sz(a)-1)
    ret.pb(a[i]);
  return ret;
}

vi buildEven(vi &a){
  vi ret;
  fi(sz(a))
    ret.pb(a[i]);
  fd(i,sz(a))
    ret.pb(a[i]);
  return ret;
}

int works(vi &a){
  fk(2*sz(a)-1){
    int sum = 0;
    fi(sz(a)){
      int j = k-i;
      if(j>=0 && j<sz(a))
        sum += a[i]*a[j];
    }
    if(sum >= 10)
      return 0;
  }
  return 1;
}

void myCode() {

  vector< pair<int,string> > ret;
  for(ll len=1; len<=25; ++len)
    for(int sumDig=1; sumDig<=9; ++sumDig)
      for(ll combo=(1LL<<(len+sumDig-1))+(1LL<<(len-1))-1; combo<(1LL<<(len+sumDig)); combo=nextComb(combo)){

        vi a = build(combo, len);

        // prune search
        int ok = 1;
        if(a[0] == 0)
          ok = 0;
        if(ok)
          fi(sz(a))
            if(sz(a)!=1 && a[i] >= 3)
              ok = 0;
        if(ok){
          int sumSq = 0;
          fi(sz(a))
            sumSq += a[i]*a[i];
          if(sumSq >= 10)
            ok = 0;
        }
        if(!ok)
          continue;

        vi b = buildOdd(a);
        vi c = buildEven(a);
        if(works(b))
          ret.pb(makePair(b));
        if(works(c))
          ret.pb(makePair(c));

      }
  srt(ret);

  int ttt=getint();
  fo(tt,ttt){
    string aa, bb;
    cin >> aa >> bb;
    pair<int,string> a(sz(aa), aa), b(sz(bb), bb);
    printf("Case #%d: %d\n", tt+1, int(upper_bound(all(ret), b) - lower_bound(all(ret), a)));
  }

}

int main() {
/*
  // seed the random number generator with microseconds
  struct timeval tv;
  gettimeofday(&tv, NULL);
  srand(tv.tv_usec);
*/
  myCode();
  return 0;
}

