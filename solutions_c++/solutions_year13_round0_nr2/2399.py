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

int a[100][100];
int b[100][100];

bool solve() {
  int N, M;
  cin >> N >> M;
  memset(a, 0, sizeof(a));
  for(int i=0;i<N;++i) for(int j=0;j<M;++j) {
    cin >> a[i][j];
    b[i][j]=100;
  }
  for(int k=100;k>=1;--k) {
    for (int i =0;i<N;i++) {
      bool good = true;
      for (int j=0;j<M;j++) {
        if (a[i][j]>k) { good=false; break;}
      }
      if (good) {
        for(int j=0;j<M;++j) {
          b[i][j]=k;
        }
      }
    }
    for(int j=0;j<M;++j) {
      bool good=true;
      for(int i=0;i<N;++i) {
        if (a[i][j]>k) {good=false; break;}
      }
      if (good){
        for(int i=0;i<N;++i){
          b[i][j]=k;
        }
      }    
    }
  }
  for(int i=0;i<N;++i) for(int j=0;j<M;++j) {
    if (a[i][j]!=b[i][j]) return false;
  }
  return true;
  
}


int main() {
  cin.sync_with_stdio(0);  

  int T=0;
  cin >> T;
  for(int i=0;i<T;++i) {
    bool ret = solve();
    cout << "Case #" << i+1 << ": " << (ret?"YES":"NO") << endl;
  }
  
  

  return 0;

}