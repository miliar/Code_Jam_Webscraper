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
  in C, D, V; cin >> C >> D >> V;
  VI A(D); forn(i,D) cin >> A[i];
  in sum = 0;
  in res = 0;
  in i = 0;
  while(sum*C < V) {
    if(i>=sz(A) || sum*C+1 < A[i]) { // Add new number
      res++;
      sum += sum*C + 1;
    } else {
      sum += A[i];
      i++;
    }
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
