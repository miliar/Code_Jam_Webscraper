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

LL isPrime(LL n) {
   if(n==1 || n==2)
      return 0;
   if(n%2==0)
      return 2;
   for(LL i=2,s=sqrt(n);i<=s;i++)
      if(n%i==0)
         return i;
   return 0;
}

LL toBase(LL n, LL b) {
   LL i=0,r=0;
   while (n!=0) {
      if (n&1) r+=(LL)pow(b,i);
      ++i; n=(n>>1);
   }
   return r;
}

string toBin(LL n) {
   string r("");
   while (n!=0) {
      if (n&1) r += "1";
      else r += "0";
      n=(n>>1);
   }
   return string(r.rbegin(), r.rend());
}

int main(int argc, const char * argv[]) {
   //freopen("B-large.in", "rt", stdin);
   freopen("C-small.out", "wt", stdout);
   
   LL n=32769;
   LL o=n;
   cout << caseStr(1) << endl;
   int sh=14;
   int sho=sh;
   int sb=1;
   int nr=0;
   while (n!=65535) {
      stringstream ss;
      bool ok=true;
      FOR(b, 2, 10) {
         LL m = toBase(n, b);
         LL d = isPrime(m);
         if (d!=0) {
            ss << " " << d;
         }
         else {
            ok=false;
            break;
         }
      }
      if (ok) {
         cout << toBin(n) << ss.str() << endl;
         if (++nr == 50) {
            break;
         }
      }
      if (sh==0) {
         sh = --sho;
         sb=((sb<<1)|1);
      }
      n=o|(sb<<sh--);
   }
   
   /*LL n=33;
   cout << caseStr(1) << endl;
   int sh=1;
   int sb=1;
   int nr=0;
   while (n!=63) {
      stringstream ss;
      bool ok=true;
      FOR(b, 2, 11) {
         LL m = toBase(n, b);
         LL d = isPrime(m);
         if (d!=0) {
            ss << " " << d;
         }
         else {
            ok=false;
            break;
         }
      }
      if (ok) {
         cout << toBin(n) << ss.str() << endl;
         if (++nr == 3) {
            break;
         }
      }
      if (sh==5) {
         sh = 1;
         sb=(sb<<1);
      }
      n=(n|(sb<<sh++));
   }*/

   return 0;
}