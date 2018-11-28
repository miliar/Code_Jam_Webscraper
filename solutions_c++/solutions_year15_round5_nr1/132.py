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
typedef pair<in,in> PII;
typedef vector<PII> VPII;


void test() {
  in N; cin >> N;
  in D; cin >> D;

  in Sn, As, Cs, Rs;
  cin >> Sn >> As >> Cs >> Rs;

  VI S(N);
  forn(i,N) {
    if(i==0) S[i] = Sn;
    else {
      S[i] = (S[i-1] * As  + Cs) % Rs;
      // cout << S[i] << " ";
    }
  }
  // cout << endl;

  in Mn, Am, Cm, Rm;
  cin >> Mn >> Am >> Cm >> Rm;

  VI M(N);
  forn(i,N) {
    if(i==0) M[i] = Mn;
    else {
      M[i] = (M[i-1] * Am  + Cm) % Rm;
      // cout << M[i] << " ";
    }
  }
  // cout << endl;

  forn(i,N) {
    if(i==0) continue;
    M[i] = M[i] % i;
    // cout << M[i] << " ";
  }
  // cout << endl;

  VI Low(N,S[0]);
  VI High(N,S[0]);

  forn(i,N) {
    if(i==0) continue;
    Low[i] = min(S[i],Low[M[i]]);
    High[i] = max(S[i],High[M[i]]);
  }
  
  VPII E;

  forn(i,N) {
    // cout << "Person with range " << Low[i] << " " << High[i] << endl;
    if(High[i]-Low[i] <= D) {
      // cout << " -> create events at " << High[i]-D << " and " << Low[i] << endl;
      E.PB(MP(High[i]-D,-1));
      E.PB(MP(Low[i],1));
    }
  }
  sort(E.begin(),E.end());

  in opt = 0;
  in cnt = 0;
  forv(i,E) {
    // cout << "E[" << i << "]: " << E[i].first << " = " << E[i].second << endl;
    cnt += -E[i].second;
    opt = max(opt,cnt);
  }
  cout << opt << endl;
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
