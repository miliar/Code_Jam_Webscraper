/*
ID: ahri1
PROG: B
LANG: C++
*/
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define sz(X) ((int)(X).size())
#define foreach(i,c) for(__typeof((c).begin()) i=((c).begin());i!=(c).end();++i)
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
#define junik(X) {sort( (X).begin(), (X).end() ); (X).erase( unique( (X).begin(), (X).end() ), (X).end() ); }
template<typename T> string v_2_s(vector<T> &a) { stringstream sb; __typeof(a.begin()) i = a.begin(); if (i!=a.end()) { sb << *i; ++i; } for (; i!=a.end();++i) { sb << " " << *i; } return sb.str(); }

template<typename T, typename U> inline void relaxmax(T &res, const U &x) {
  if (x > res) {
    res = x;
  }
}


template<typename T, typename U> inline void relaxmin(T &res, const U &x) {
  if (x < res) {
    res = x;
  }
}

void solve(){
  int D;
  cin >> D;
  vector<int> P;
  int x;
  int max_x = 0;
  for (int i = 0; i < D; ++i){
    cin >> x;
    relaxmax(max_x, x);
    P.push_back(x);
  }

  int ret = max_x;

  for (int i = 1; i < max_x; ++i) {
    int t = 0;
    for (int j = 0; j < D; ++j) {
      t += (P[j] - 1) / i;
    }
    //~ cerr << i << " " << ret << endl;
    relaxmin(ret, i + t);
  }
  cout << ret << endl;
}

int main() {

  cin.sync_with_stdio(0);
  int T;
  cin >> T;
  for (int i=0;i<T;i++) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }

  return 0;
}
