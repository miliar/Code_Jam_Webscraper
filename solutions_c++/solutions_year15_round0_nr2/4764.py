#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <limits>
#include <string>
#include <cstring>
#include <cassert>
#include <climits>
#include <cfloat>
#include <tr1/unordered_map>

using namespace std;

typedef std::tr1::unordered_map<int,int> un_mapii;
 
#define GI ({int t;scanf("%d",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define GF ({float t;scanf("%f",&t);t;})
#define GLL ({long long t;scanf("%lld",&t);t;})
#define GLD ({long double t;scanf("%Lf",&t);t;})
#define SET(c) memset(c,-1,sizeof(c))
// #define s(n) scanf("%d",&n)
#define sl(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
 
#define sstr(str) scanf ("%s", str); 
 
#define p(n) printf("%d ",n)
 
#define pc(char) printf("%c ",char)
#define pl(n) printf("%ld ",n)
#define pll(n) printf("%lld ",n)
 
#define pf(n) printf("%f\n",n)
#define pd(n) printf("%lf\n",n)
 
#define pnl(n) printf("%d\n",n)
#define plnl(n) printf("%ld\n",n)
#define pllnl(n) printf("%lld\n",n)
 
#define ll long long
#define MAX(a,b) a>b?a:b
#define all(c) c.begin(), c.end()
#define rall(c) c.rbegin(), c.rend()    // reverse all 
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
 
#define rep(i, n) for(int i = 0; i < (n); ++i)
#define forn(i, a, b) for(int i = (a); i < (b); ++i)
#define ford(i, a, b) for(int i = (a); i >= (b); --i)
#define fore(i, a, b) forn(i, a, b + 1)
#define MALLOC(n,T) (T*)malloc(n*sizeof(T))
 
#define tr(c,it) for(typeof(c.begin()) it = c.begin(); it !=c.end(); it++)
#define cpresent(c,x) ((c).find(x) != (c).end()) 
#define present(c,x) (find(all(c),x) != (c).end()) 

typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<long long> vll;
typedef vector< vector<int> > vvi;
typedef vector< vector<char> > vvc;
typedef vector<string> vstr;
typedef map<int,int> mapii;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<char,int> pci;
typedef pair<string,string> pss;
typedef std::vector<pii> vpii;
typedef std::vector<pdd > vpdd;
typedef std::vector<pci> vpci;
typedef std::vector<vpii> vvpii;
typedef std::vector<pss> vpss;
typedef map<string,pss> mapspss;

#define sz(a) int((a).size()) 
#define szar(ar) int(sizeof(ar)/sizeof(ar[0]))
#define mod 1000000000LL 

//-------------------------------------------------------------------------------------



int getans(vi& v) {
  int maxelem = *max_element(all(v));

  int ans = INT_MAX;
  for (int high = 1; high <= maxelem; ++high)
  {
    int extra = 0, divides = 0;
    rep(i,sz(v)) {
      extra = max(v[i] - high,0);
      divides += (int)ceil((double)extra/high);
    }

    // printf("divides = %d\n", divides);

    ans = min(ans, divides + high);
    // printf("high = %d\n", high);
    // printf("ans = %d\n", ans);
  }
  return ans;
}




int main(int argc, char const *argv[])
{
  int t=GI;
  for (int tc = 1; tc <= t; ++tc)
  {
    int n = GI;
    vi v;
    for (int i = 0; i < n; ++i)
    {
      int temp = GI;
      v.push_back(temp);
      // printf("%d : %d,%d\n",temp,cd[temp].ff, cd[temp].ss );
    }

    
    int ans = getans(v);

    printf("Case #%d: %d\n",tc,ans);
    // printf("%d\n", (int)ceil(4/2.0));
  }

  

  return 0;
}
