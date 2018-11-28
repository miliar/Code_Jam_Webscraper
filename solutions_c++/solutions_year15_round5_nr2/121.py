// -*- compile-command: "g++ -Wall -Wextra x.cpp -o x && ./x <test.in" -*-
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long in;
#define PB push_back
#define MP make_pair
#define sz(v) (in)(((v).size()))
#define forn(i,n) for(int i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
typedef vector<in> VI;


void test() {
  in N; cin >> N;
  in K; cin >> K;

  VI S(N-K+1);
  forn(i,N-K+1) {
    cin >> S[i];
  }

  VI Low(K,0);
  VI High(K,0);
  VI X(N,0);
  for(in i=K; i<N; i++) {
    X[i] = X[i-K] + S[i-K+1] - S[i-K];
    // cout << "X[" << i << "] = " << X[i] << endl;
    Low[i%K] = min(X[i],Low[i%K]);
    High[i%K] = max(X[i],High[i%K]);
  }

  in opt = 0;

  forn(i,K) {
    opt = max(opt, High[i]-Low[i]);
  }

  in is = 0;
  in flex = 0;
  forn(i,K) {
    is += -Low[i];
    is %= K;
    flex += opt - (High[i]-Low[i]);
  }
  in dist = S[0]%K - is;
  if(dist < 0) dist += K;
  bool add_one = false;
  if(flex < dist) add_one=true;
  cout << opt + add_one << endl;
  //cout << opt << endl;
}
int main(){
  std::ios::sync_with_stdio(false); // remove this if you use printf/scanf
  std::cin.tie(0);

  in T; cin >> T;
  forn(t,T) {
    cout << "Case #" << t+1 << ": ";
    test();
  }

  return 0;  
}
