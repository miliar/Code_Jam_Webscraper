#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

int E,R,N;
vector<int> v;

int sub(int e, int ix) {
  if (ix == N) return 0;

  int gi = v[ix];
  int gmax = 0;
  for (int i=0; i<=e; ++i) {
    int e_ = e-i+R; if (e_>E) e_=E;
    int mg = gi*i + sub(e_, ix+1);
    if (mg > gmax) gmax = mg;
  }
  return gmax;
}

main(){
  int _T; cin>>_T;
  rep(_t,_T){
    cin >> E >> R >> N;
    v.resize(N); rep(i,N) cin >> v[i];

    int ans = sub(E,0);
    printf("Case #%d: %d\n", 1+_t, ans);
  }
}
