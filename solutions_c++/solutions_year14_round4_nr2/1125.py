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

bool check(const vector<int>& v){
  bool flg = false;
  REP(i,1,v.size()){
    if(v[i-1] > v[i]){
      if(!flg) flg = true;
    }else{
      if(flg) return false;
    }
  }
  return true;
}

int mergecount(vector<int> &a) {
  int count = 0;
  int n = a.size();
  if (n > 1) {
    vector<int> b(a.begin(), a.begin() + n/2);
    vector<int> c(a.begin() + n/2, a.end());
    count += mergecount(b);
    count += mergecount(c);
    for (int i = 0, j = 0, k = 0; i < n; ++i)
      if (k == c.size())       a[i] = b[j++];
      else if (j == b.size())  a[i] = c[k++];
      else if (b[j] <= c[k])   a[i] = b[j++];
      else                   { a[i] = c[k++]; count += n/2 - j; }
  }
  return count;
}

int dist(const vector<int>& v, const vector<int>& w){
  int ret = 0;
  vector<int> cnt;
  rep(i,v.size()){
    rep(j,w.size()){
      if(v[i] == w[j]){
        cnt.push_back(j);
      }
    }
  }
  return mergecount(cnt);
}


int solve_small(vector<int>& v){
  vector<int> w = v; 
  sort(ALLOF(w));

  int ret = 9999999;
  do{
    if(check(w)){
      int res = dist(v, w);
      ret = min(ret, res);
    }
  }while(next_permutation(ALLOF(w)));
  
  return ret;
}

int main(){
  int T;
  cin >> T;

  for(int t=0; t<T; t++){
    int N, tmp;
    vector<int> v;
    cin >> N;
    rep(i,N){
      cin >> tmp;
      v.push_back(tmp);
    }
    cout << "Case #" << t+1 << ": " << solve_small(v) << endl;
  }
  
  return 0;
}
