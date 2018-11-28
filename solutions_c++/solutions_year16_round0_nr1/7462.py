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


in sum(VI &V) { 
  in s = 0;
  forv(i,V) s+=V[i];
  return s;
}
void test() {
  in N; cin >> N;
  in X = 0;
  VI seen(10,false);
  in i = 0;
  while(sum(seen)<10 && i < 200) {
    X += N;
    i++;
    in b = 1;
    while(b<=X) {
      in d = (X%(10*b))/b;
      // cout << d << " ";
      seen[d] = true;
      b*=10;
    }
    // cout << endl;
  }
  if(sum(seen)==10) {
    cout << X << endl;
  } else {
    cout << "INSOMNIA" << endl;
  }
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
