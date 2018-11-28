#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<algorithm>
using namespace std;

map<vector<int>,int> dp;

int calc(vector<int> P){
  int n = P.size();
  /*
  for(int i=0; i<n; i++) cout << P[i] << " ";
  cout << endl;
  */
  if(dp.find(P) != dp.end()) return dp[P];

  bool allone = true;
  for(int i=0; i<n; i++){
    if(P[i] != 1) allone = false;
  }
  if(allone) return dp[P] = 1;

  int pmax = 0;
  int a = 1000;
  for(int i=0; i<n; i++){
    pmax = max(pmax, P[i]);
    for(int j=1; j<P[i]/2+1; j++){
      vector<int> Q = P;
      Q[i] = P[i] - j;
      Q.push_back(j);
      sort(Q.begin(), Q.end());
      a = min(a, 1+calc(Q));
    }
  }

  return dp[P] = min(a, pmax);
}

int main(){
  int T;
  cin >> T;
  for(int t=0; t<T; t++){
    int D;
    vector<int> P;
    cin >> D;
    int n;
    for(int i=0; i<D; i++){
      cin >> n;
      P.push_back(n);
    }
    sort(P.begin(), P.end());
    cout << "Case #" << t+1 << ": " << calc(P) << endl;
  }
}

