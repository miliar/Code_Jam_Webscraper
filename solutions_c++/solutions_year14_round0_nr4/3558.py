#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,pocz,koniec) for (int var=(pocz); var<=(koniec); ++var)
#define FORD(var,pocz,koniec) for (int var=(pocz); var>=(koniec); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

const int N =1100;
double naomi[N], ken[N];

int main(){
  int testy;
  scanf("%d",&testy);
  int numer=0;
  while (testy--){
    printf("Case #%d: ",++numer);
    int n;
    scanf("%d",&n);
    REP(i,n) scanf("%lf",naomi+i);
    REP(i,n) scanf("%lf",ken+i);
    sort(naomi, naomi+n);
    sort(ken, ken+n);

    REP(foo, 2) {
      int l = 0, r = n;
      while (l < r) {
        int m = (l+r+1) / 2;
        int ok = 1;
        REP(i,m) if (naomi[n-m+i] < ken[i]) ok = 0;
        if (ok) l = m;
        else r = m-1;
      }
      if (foo) printf(" ");
      printf("%d",(foo ? n - l: l));
      REP(i,n) swap(naomi[i],ken[i]);
    }
    puts("");
  }
  return 0;
}
