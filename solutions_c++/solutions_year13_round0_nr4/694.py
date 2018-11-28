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

#define IMP "IMPOSSIBLE"

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


int K, N;
int myKeys[201];
int t[201];
int k[201][201];

string ret;

int v[201];
int retGen[201];

set<unsigned> visited;

void dfs(int x, int depth, unsigned mask) {
//  cout << x +1 << " " << depth << endl;
//  cout << "keys: ";
//  for(int i=0;i<201;++i) {
//    if (myKeys[i]>0) cout << i << " ";
//  }
//  cout << endl;
  if (ret!=IMP) return;
  if (depth==N+1) {
    for(int i=0;i<N;++i) {
      retGen[v[i]-1]=i+1;
    }
    ret="";
    for(int i=0;i<N;++i) {
      ret+=itos(retGen[i]);
      if (i<=N-1) ret+=" ";
    }
    return;    
  }
  if (v[x]) return;
  if (myKeys[t[x]]>0) {
    if (visited.find(mask)!=visited.end()) return;
    visited.insert(mask);
    v[x]=depth;
    myKeys[t[x]]--;
    for(int i=0;i<201;++i) {
      myKeys[i]+=k[x][i];
    }
    for(int i=0;i<N;i++) dfs(i, depth+1, mask | ((unsigned)1<<i));
    for(int i=0;i<201;++i) {
      myKeys[i]-=k[x][i];
    }
    myKeys[t[x]]++;
    v[x]=0;
  }

}

string solve() {

  cin >> K >> N;
  memset(myKeys, 0, sizeof(myKeys));  
  memset(t, 0, sizeof(t));
  memset(k, 0, sizeof(k));
  memset(v, 0, sizeof(v));
  visited.clear();
  int m, x;
  ret = IMP;
  for(int i=0;i<K;++i) {
    cin >> x;
    myKeys[x]++;
  }
  for (int i=0;i<N;i++) {
    cin >> t[i];
    cin >> m;
    for(int j=0;j<m;++j) {
      cin >> x;
      k[i][x]++;
    }      
  }
  
  for (int i=0;i<N && ret==IMP;i++) {
    dfs(i, 1, ((unsigned)1<<i));
  }
  
  return ret;
}

int main() {
  cin.sync_with_stdio(0);  
  int T;
  cin >> T;
  
  for(int i=0;i<T;++i) {
    string ret = solve();
    cout << "Case #" << i+1 << ": " << ret << endl;
  }

  return 0;

}