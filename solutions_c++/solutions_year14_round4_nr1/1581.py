/*
ID: ahri1
PROG: A
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


void solve(){
  int N, S, X;
  cin >> N >> S;
  vector<int> A;
  for(int i=0;i<N;++i){
    cin >> X;
    A.push_back(X);
  }
  sort(A.begin(), A.end());
  reverse(A.begin(), A.end());
  // cerr << v_2_s(A) << endl;
  int sol = 0;
  for(int i=0, j=N-1;i<=j;++i){
    // cerr << i << " " << j << endl;
    if (i==j) {
      sol++;
      i++;
      continue;
    }
    if (A[i]+A[i+1]<=S) {
      i++;
      sol++;
      continue;
    }
    if (A[i]+A[j]<=S) {
      sol++;
      j--;    
      continue;
    }
    sol++;
  }
  cout << sol << endl;
  // cerr << sol << endl;
  

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
