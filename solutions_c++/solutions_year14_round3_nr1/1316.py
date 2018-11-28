#include <cstring>
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

LL nwd(LL a, LL b) {
  return b == 0 ? a : nwd(b, a%b);
}

int main(){
  int testy;
  scanf("%d",&testy);
  int numer=0;
  while (testy--){
    printf("Case #%d: ",++numer);
    char txt[200];
    scanf("%s",txt);
    REP(i,(int)strlen(txt)) if (txt[i] == '/') txt[i] = ' ';
    LL p, q;
    sscanf(txt,"%lld %lld", &p, &q);
    int ok = 1;
    //cout << p << " " << q << endl;
    LL x = nwd(p,q);
    p /= x; q /= x;
    //cout << p << " " << q << endl;
    REP(foo,40) {
      if (q > 1) {
        if (q % 2) {
          ok = 0;
        } else {
          q /= 2;
        }
      } else {
        p *= 2;
      }
    }
    //cout << p << " " << q << endl;
    if (!ok) cout << "impossible" << endl;
    else {
      int res = 1;
      LL acc = 1LL << 39;
      while (acc > p) {
        res++; acc /= 2;
      }
      cout << res << endl;
    }
  }
  return 0;
}
