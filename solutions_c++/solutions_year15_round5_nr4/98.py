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
  in P; cin >> P;
  map<in,in> M;
  VI V(P);
  in sum = 0;
  forn(i,P) cin >> V[i];
  forn(i,P) {
    in a; cin >> a;
    M[V[i]] = a;
    sum += a;
  }

  in N = 1;
  while((1<<N) < sum) N++;

  VI S(N,-1);
  forn(x,1<<N) {
    in has_all = -1;
    in sum = 0;
    forn(i,N) {
      if(x&(1<<i)) {
        if(S[i]==-1) has_all = i;
        else {
          sum += S[i];
        }
      }
    }
    if(has_all!=-1) {
      S[has_all] = M.begin()->first - sum;
      sum += S[has_all];
    }
    M[sum]--;
    if(M[sum]==0) M.erase(sum);
  }

  forv(i,S) {
    cout << S[i];
    if(i<sz(S)-1) cout << " ";
  }
  cout << endl;



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
