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

#define BIT_CHECK(X,N) ((X)&(1<<(N)))
#define BIT_SET(X,N) ((X)|=(1<<(N)))
#define BIT_CLEAR(X,N) ((X)&=~(1<<(N)))

typedef vector<int> VI;
typedef vector<string> VS;

template<class T> inline string stringify(T x,int p=9){ostringstream o;o.precision(p);o<<x;o.flush();return o.str();}
inline VS parse(string s,char ch=' '){string a;VS wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(a);a="";} if(!a.empty()) wyn.PB(a);return wyn;}
inline VI parsei(string s,char ch=' '){string a="";VI wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(atoi(a.c_str()));a="";} if(!a.empty()) wyn.PB(atoi(a.c_str()));return wyn;}
template<class T> inline void wypisz(const T& x){FOREACH(I,x)cout<<*I<<" ";cout<<endl<<flush;}

int N;
int m;
VI v;
VI b;

inline int check(){
  int f=b[v[0]-1];
  if(v[1]!=f&&v[m-1]!=f) return 0;
  f=b[v[m-1]-1];
  if(v[0]!=f&&v[m-2]!=f) return 0;
  FOR(i,1,m-2){
    f=b[v[i]-1];
    if(v[i-1]!=f&&v[i+1]!=f) return 0;
  }
  return 1;
}

int main(){
  int T;
  cin>>T;
  string line;
  getline(cin, line);
  FOR(tt,1,T){
    cin>>N;
    getline(cin, line);
    getline(cin, line);
    b=parsei(line);
    int p=0;
    int ret=0;
    while(p<(1<<N)-1){
      v.clear();
      FOR(i,1,N){
        if(!BIT_CHECK(p,i-1)) v.PB(i);
      }
      m=SZ(v);
      //wypisz(v);
      do{
        if(check()){
          //wypisz(v);
          if(SZ(v)>ret) ret=SZ(v);
          break;
        }
      } while(next_permutation(ALL(v)));
      p++;
    }
    cout<<"Case #"<<stringify(tt)<<": "<<stringify(ret)<<"\n";
  }

  return 0;
}
