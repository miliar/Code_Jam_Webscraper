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

vector<pii> V;

int A[1010];
int te;

void test(){
  int n;
  scanf("%d", &n);
  V.clear();
  FOR(i,n){
    int a;
    A[i] = 0;
    scanf("%d",&a);
    V.pb(mp(a,i));
  }
  SORT(V);
  int ans = 0;
  FOR(i,SZ(V)){
    int x = V[i].se;
    int o1 = 0,o2=0;
    FOR(j,x) if(A[j] == 0) o1++;
    REP(j,x+1,n-1) if(A[j] == 0) o2++;
    DBG(V[i].fi)DBG(V[i].se)DBG(o1)DBG(o2)
    ans += min(o1,o2);
    A[x] = 1;
  }
  printf("Case #%d: %d\n", ++te,ans);
}

int main () {
  int t;
  scanf("%d",&t);
  while(t--) test();
}
