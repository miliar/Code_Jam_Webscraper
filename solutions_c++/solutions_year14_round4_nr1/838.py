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

vector<int> V;

int te;
void test(){
  int n,Ma;
  scanf("%d%d",&n,&Ma);
  V.clear();
  FOR(i,n){
    int a;
    scanf("%d",&a);
    V.pb(a);
  }
  SORT(V);
  int p = 0;
  int k = SZ(V)-1;
  int ans = 0;
  while(p < k){
    if(V[p] + V[k] <= Ma)
      p++;
    k--;
    ans++;
  }
  if(p == k) ans++;
  printf("Case #%d: %d\n", ++te, ans);
}

int main () {
  int t;
  scanf("%d",&t);
  FOR(i,t) test();
}
