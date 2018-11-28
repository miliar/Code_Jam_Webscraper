#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define x first
#define y second
#define fi(n) fo(i,n)
#define fj(n) fo(j,n)
#define fk(n) fo(k,n)
#define fd(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define fo(i,n) fr(i,0,n)
#define fr(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x)*(x))
#define srt(x) sort(all(x))

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

const int INF = 1000*1000*1000+7;
const double EPS = 1e-9;
const double PI = acos(-1.0);
template<class T> int chmin(T &t, T f) { return (t>f) ? (t=f,1) : 0; }
template<class T> int chmax(T &t, T f) { return (t<f) ? (t=f,1) : 0; }

inline int getint() {
  int a;
  return scanf("%d",&a) ? a : (fprintf(stderr,"trying to read\n"),-1);
}

inline double getdouble() {
  double a;
  return scanf("%lf",&a) ? a : (fprintf(stderr,"trying to read\n"),-1);
}

const int N = 110;
double r[N];
double c[N];

void myCode() {
  int ttt = getint();
  fo(tt,ttt) {
    int n = getint();
    double v = getdouble(), x = getdouble();
    fi(n) {
      r[i] = getdouble();
      c[i] = getdouble();
    }
    if (n == 1) {
      if (fabs(c[0]-x) < EPS) {
        printf("Case #%d: %.9lf\n",tt+1,v/r[0]);
      } else {
        printf("Case #%d: IMPOSSIBLE\n",tt+1);
      }
    } else if (n == 2) {
      if (c[0] > c[1]) {
        swap(c[0],c[1]);
        swap(r[0],r[1]);
      }
      if (c[0] < x-EPS && c[1] < x-EPS)
        printf("Case #%d: IMPOSSIBLE\n",tt+1);
      else if (c[0] > x+EPS && c[1] > x+EPS)
        printf("Case #%d: IMPOSSIBLE\n",tt+1);
      else if (fabs(c[0]-x) < EPS && fabs(c[1]-x) < EPS)
        printf("Case #%d: %.9lf\n",tt+1,v/(r[0]+r[1]));
      else {
        double tmp = (r[0]*c[0] + r[1]*c[1])/(r[0] + r[1]);
        bool tog = tmp > x;
        double lo = 0, hi = 1e9;
        fk(70) {
          double mid = (lo+hi)/2;
          double vol = r[!tog]*mid*(1+(c[!tog]-x)/(x-c[tog]));
          if (vol <= v)
            lo = mid;
          else
            hi = mid;
        }
        printf("Case #%d: %.9lf\n",tt+1,(lo+hi)/2);
      }
    }
  }
}

int main () {
  srand(time(NULL));
  myCode();
  return 0;
}
