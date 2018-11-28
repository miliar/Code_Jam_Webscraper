/*
ID: ahri1
PROG: D
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

void solve(){
  int N;
  cin >> N;
  vector<double> A(N), B(N);
  for(int i=0;i<N;++i){
    cin >> A[i];
  }
  for(int i=0;i<N;++i){
    cin >> B[i];
  }
  sort(A.begin(), A.end());
  sort(B.begin(), B.end());
  
  // cout << endl;
  // for(int i=0;i<N;++i){
    // cout << A[i] << " ";
  // }
  // cout << endl;
  // for(int i=0;i<N;++i){
    // cout << B[i] << " ";
  // }
  // cout << endl;
  
  
  int ret1 = 0;
  for(int i=0, j=0;i<N;++i){    
    if (A[i]>B[j]) { 
      ret1++;
      j++;      
    }
  }
  
  
  
  int ret2 =0;
  for(int i=0;i<N;++i){
    vector<double>::iterator up = upper_bound(B.begin(), B.end(), A[i]);
    if (up==B.end()) {
      ret2++;
      B.erase(B.begin());
    } else {    
      B.erase(up);
    }
    

  }
  cout << ret1 << " " << ret2 << endl;

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
