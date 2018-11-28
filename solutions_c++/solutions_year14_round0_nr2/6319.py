#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <climits>
#include <cassert>
#include <ctime>
#include <cstring>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
#define MS(v,i) memset(v,i,sizeof(v))
#define S(x) scanf("%d",&x)
#define S1(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define co(x) cout << x << endl;
#define gc getchar_unlocked
typedef long long ll;
typedef pair<int,int> pii;

/*void si(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}*/

int main() {
    int t;
    S(t);
    double c,f,x;
    int u = 1;
    while(u < t+1) {
      double sec = 2;
      double tim = 0;
      cin >> c >> f >> x;
      while((x/(sec+f)) + (c/sec) < (x/sec)){
        tim = tim + c/sec;
        sec = sec + f;
      }
      tim = tim + x/sec;

      cout << "Case #" << u <<": ";
      printf("%0.7f\n",tim);
      u++;
    }

    return 0;

}

