#include <iostream>
#include <iomanip>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <limits>
using namespace std;
#define ll long long
#define ld long double
#define pii pair<int,int>
#define x first
#define y second
#define sf scanf
#define pf printf
#define vec vector
#define pb push_back
#define mp make_pair
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()
#define clr(a,b) memset(a,b,sizeof(a))
#define bin_cnt(x) __builtin_popcount(x)
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define rrep(i,b,a) for(int i=b;i>=a;i--)
#define srep(sub,s) for(int sub=s&(s-1);sub;sub=(sub-1)&s)
#define irep(i,a) for(__typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define irrep(i,a) for(__typeof(a.rbegin()) i=a.rbegin();i!=a.rend();i++)
#define inf numeric_limits<int>::max()
#define finf numeric_limits<double>::infinity()
#define eps 1e-9
#pragma GCC optimize ("O3")
#define o3 __attribute__((optimize("O3")))
#pragma comment(linker, "/STACK:32505856")

template<class T> inline T sqr(T a) {return a*a;}
template<class T> inline void gmin(T&a,T b) {if(a>b)a=b;}
template<class T> inline void gmax(T&a,T b) {if(a<b)a=b;}
inline int dcmp(const double &a) {return a>eps?1:(a<-eps?-1:0);}
struct Initializer{Initializer(){ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);}}initializer;

int main() {
  // freopen("in.txt","r",stdin);
  // freopen("B-small-attempt0.in","r",stdin);
  // freopen("B-small-attempt0.ou","w",stdout);
  freopen("B-large.in","r",stdin);
  freopen("B-large.ou","w",stdout);

  int cas;
  sf("%d",&cas);
  rep(t,1,cas) {
    pf("Case #%d: ",t);

    double C,F,X;
    sf("%lf%lf%lf",&C,&F,&X);

    double cst=0,per=2,get=0;
    while (get+eps<X) {
      if (X>=C) {
        if (get>=C) {
          if (X*per < (X-get)*(per+F)) {
            get=0;
            per+=F;
          } else {
            cst+=(X-get)/per;
            get=X;
          }

        } else {
          cst+=(C-get)/per;
          get=C;
        }
      } else {
        cst+=(X-get)/per;
        get=X;
      }
    }
    pf("%.20f\n",cst);
  }

  return 0;
}