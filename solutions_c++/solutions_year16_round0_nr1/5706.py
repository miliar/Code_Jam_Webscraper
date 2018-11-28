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
   freopen("A-large.in", "rt", stdin);
   freopen("A-large.out", "wt", stdout);
   
   int notc = rint();
   REP(i, notc) {
      int n = rint();
      int a = 0;
      if (n == 0) {
         cout << caseStr(i+1) << "INSOMNIA" << endl;
         continue;
      }
      else {
         int j=2;
         int m=n,o=n;
         while (a!=1023) {
            if (m==0) {
               o=n*j++;
               m=o;
            }
            a |= (1<<(m%10));
            m=m/10;
         }
         cout << caseStr(i+1) << o << endl;
      }
   }
   
   return 0;
}