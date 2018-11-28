#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <ctime>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
#define sz(X) ((int)(X).size())
#define FOREACH(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define IN(_lower,_variable,_higher) (((_lower)<=(_variable)) && ((_variable)<=(_higher)))
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORU(v,p,k) for(int v=p;v<k;++v)
#define FORD(v,p,k) for(int v=(p)-1;v>=k;--v)
#define FORLLU(v,p,k) for(LL v=p;v<k;++v)
#define FORLLD(v,p,k) for(LL v=(p)-1;v>=k;--v)
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
#define junik(X) {sort( (X).begin(), (X).end() ); (X).erase( unique( (X).begin(), (X).end() ), (X).end() ); }

int ispalindrome(string x) { for (int i=0;i<sz(x)>>1;i++) if (x[i]!=x[sz(x)-1-i]) return 0; return 1; }


string itos(long long x) {
  if (x==0) return "0";
  string ret="";
  if (x>0) {
    while (x) {
      ret=(char)((x%10)+'0') + ret;
      x/=10;
    }
    return ret;
  } else {
    while (x) {
      ret=(char)((x%10)+'0') + ret;
      x/=10;
    }
    return "-"+ret;
    
  }
}

int solve() {
  LL A, B;
  cin >> A >> B;
  int ret=0;
  LL i=(LL) sqrt(A);
  if (i*i<A) i++;
  for (;i*i<=B;i++) {    
    if (ispalindrome(itos(i)) && ispalindrome(itos(i*i))) {
      ret++;
//      cout << i << " " <<  i*i << endl;
    }
  }
  return ret;
  
}


int main() {
  cin.sync_with_stdio(0);  
  
  int T=0;
  cin >> T;
  for(int i=0;i<T;++i) {
    int ret = solve();
    cout << "Case #" << i+1 << ": " << ret << endl;
  }
  
  return 0;

}