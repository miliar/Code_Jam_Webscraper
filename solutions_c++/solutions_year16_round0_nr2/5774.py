#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>

using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FORIT(it,c) for(auto it=(c).begin(); it!=(c).end(); ++it)
#define sz(x) ((int)(x).size())
#define all(c) begin(c),end(c)
#define mp make_pair
#define pb push_back

typedef long long LL;
typedef unsigned long long ULL;
int rint() { int x; if(scanf("%d",&x)!=1) return -1; return x; }
LL rLL() { LL x; if(scanf("%lld",&x)!=1) return -1; return x; }
string rstring() { static char buf[100000]; if(scanf("%s",buf)!=1) return ""; return buf; }
string caseStr(int i) { stringstream ss; ss << "Case #" << i << ": "; return ss.str(); }

int main(int argc, const char * argv[]) {
   freopen("B-large.in", "rt", stdin);
   freopen("B-large.out", "wt", stdout);
   
   int notc=rint();
   FOR(tc,1,notc) {
      string p=rstring(); int r=0;
      for(int i=0;i<sz(p)-1;++i)
         if (p[i]!=p[i+1])
            ++r;
      if (p[sz(p)-1] == '-')
         ++r;
      cout << caseStr(tc) << r << endl;
   }
   
   return 0;
}