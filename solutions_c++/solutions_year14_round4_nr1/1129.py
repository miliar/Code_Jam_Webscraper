#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;

int solve(int X, vector<int>& v){
  sort(ALLOF(v));
  reverse(ALLOF(v));
  int ret = 0;
  rep(i,v.size()) if(v[i]>=0){
    REP(j,i+1,v.size()){
      if(v[j]>=0 && v[i]+v[j]<=X){
        v[j]=-1;
        break;
      }
    }
    v[i]=-1;
    ret++;
  }
  return ret;
}

int main(){
  int T;
  cin >> T;

  for(int t=0; t<T; t++){
    int N, X, tmp;
    vector<int> v;
    cin >> N >> X;
    rep(i,N){
      cin >> tmp;
      v.push_back(tmp);
    }
    cout << "Case #" << t+1 << ": " << solve(X, v) << endl;
  }
  
  return 0;
}
