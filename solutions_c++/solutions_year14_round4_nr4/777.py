#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define SORT(X) sort(X.begin(),X.end())
#define fi first
#define se second

vector<string> V[7];
vector<string> T;
int node(int x){
  T.clear();
  FOR(i,SZ(V[x])) T.pb(V[x][i]);
  sort(T.begin(),T.end());
  int ans = T[0].size();
  FOR(i,SZ(T)-1){
    int g = 0;
    FOR(j,SZ(T[i])){
      if(j == SZ(T[i+1])) break;
      if(T[i][j] != T[i+1][j]) break;
      g++;
    }
    ans += SZ(T[i+1]) - g;
  }
  return ans;
}

int n,m;
int ANS;
int CT;
void rek(int a){
  if(a == m){
    int ans = 0;
    FORI(i,n){
      if(SZ(V[i]) == 0) return;
      int x = node(i);
      ans += x;
    }
    if(ANS < ans){
      ANS = ans;
      CT = 0;
    }
    if(ANS == ans) CT++;
    return;
  }
  FORI(i,n){
    V[i].pb(V[0][a]);
    rek(a+1);
    V[i].pop_back();
  }
}
int te;
void test(){
  cin>>m>>n;
  V[0].clear();
  FOR(i,m){
    string a;
    cin>>a;
    V[0].pb(a);
  }
  ANS = 0;
  CT = 0;
  rek(0);
  printf("Case #%d: %d %d\n",++te, ANS+n,CT);
}

int main () {
  int t;
  cin>>t;
  FOR(i,t) test();
}
