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
#include <unordered_set>
#include <sstream>
using namespace std;
typedef long long in;
#define PB push_back
#define MP make_pair
#define sz(v) (in)(((v).size()))
#define forn(i,n) for(int i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
typedef vector<in> VI;

  in N;
  vector<vector<in> > M;

void test() {
  cin >> N;
  M = vector<vector<in> >(N);
  map<string,in> Comp;
    string line;
    getline(cin, line);
  forn(i,N) {
    getline(cin, line);
    stringstream ss(line);
    string word;
    while(ss >> word) {
      if(Comp.find(word) == Comp.end()) {
        Comp[word] = sz(Comp);
      }
      M[i].PB(Comp[word]);
      // cout << "word " << word << endl;
    }
    // cout << "next line" << endl;
  }

  in res = 1999*N;
  VI A(sz(Comp),0);
  VI B(sz(Comp),0);
  VI LA(sz(Comp),0);
  VI LB(sz(Comp),0);

  forv(i,M[0]) A[M[0][i]]=1;
  forv(i,M[1]) B[M[1][i]]=1;
  forn(x,1<<(N-2)) {
    in l = (x<<2) + 1;
    LA = A;
    LB = B;
    forn(i,N) {
      if(i<2) continue;
      forv(j, M[i]) {
        if((l&(1<<i))>0) {
          LA[M[i][j]] = 1;
        } else {
          LB[M[i][j]] = 1;
        }
      }
    }
    in cnt = 0;
    forv(i,LA) {
      if(LA[i] && LB[i]) cnt++;
    }
    res = min(cnt,res);
  }
  cout << res << endl;

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
