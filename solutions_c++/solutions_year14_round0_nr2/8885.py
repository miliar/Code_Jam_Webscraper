#include<iostream>
#include<complex>
#include<vector>
#include<string>

#include<cstdio>
#include<cctype>
#include<cstring>
#include<cstdlib>
#include<cmath>

#include<sstream>
#include<unistd.h>
#include<valarray>
#include<numeric>
#include<algorithm>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>
#include <iomanip>
#include<fstream>
#include<time.h>
using namespace std;

#define NDEBUG
#include<assert.h>
#define SZ(X) ((int)X.size())
#define CLR(X) memset(X,0,sizeof(X))
#define MAX(A,B) (((A)>(B))?(A):(B))
#define MIN(A,B) (((A)<(B))?(A):(B))
#define MOD(A,B) (((A)%(B)+(B))%(B))
#define MP make_pair
#define FI first
#define SE second
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define RFOREACH(I,C) for(VAR(I,(C).rbegin());I!=(C).rend();I++)
#define ALL(X) (X).begin(),(X).end()
#define SRT(X) sort((X).begin(),(X).end())
#define PB push_back

typedef vector<int> VI;
typedef long double ld;
typedef set<int> SETI;
typedef vector<string> VS;

template<class T> inline string stringify(T x,int p=9){ostringstream o;o.precision(p);o<<x;o.flush();return o.str();}
inline VI parsei(string s,char ch=' '){string a="";VI wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(atoi(a.c_str()));a="";} if(!a.empty()) wyn.PB(atoi(a.c_str()));return wyn;}
inline VS parse(string s,char ch=' '){string a;VS wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(a);a="";} if(!a.empty()) wyn.PB(a);return wyn;}
inline double toDouble(string &s){double x=0;istringstream i(s);i.precision(9);i>>x;return x;}

int main(){
  int T;
  cin>>T;
  //string line;
  //getline(cin, line);
  string line;
  getline(cin, line);
  FOR(i,1,T){
    getline(cin, line);
    VS ps=parse(line);
    double _c=toDouble(ps[0]), _f=toDouble(ps[1]), _x=toDouble(ps[2]);
    ld c, f, x;
    c=(ld)_c;
    f=(ld)_f;
    x=(ld)_x;
    ld t=0;
    int n=0;
    ld curc=0;
    ld nextft=(c-curc)/(f*n+2);
    ld nextt=x/(f*(n+1)+2);
    ld curt=(x-curc)/(f*n+2);
    //printf("c f x nextft nextt curt: %f %f %f %f %f %f\n", (double)c, (double)f, (double)x, (double)nextft, (double)nextt, (double)curt);
    while(nextft+nextt<curt){
      n++;
      t+=nextft;
      curc=0;
      nextft=(c-curc)/(f*n+2);
      nextt=x/(f*(n+1)+2);
      curt=(x-curc)/(f*n+2);
      //printf("n t nextft nextt curt: %d %f %f %f %f\n", n, (double)t, (double)nextft, (double)nextt, (double)curt);
    }
    t+=curt;
    printf("Case #%d: %.7f\n", i, (double)t);
  }

  return 0;
}
