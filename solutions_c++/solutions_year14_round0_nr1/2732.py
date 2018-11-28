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

const string BAD="Bad magician!";
const string CHEAT="Volunteer cheated!";


void solve(){
  int X, Y;
  set<int> S;
  for(int k=0;k<2;++k){
    cin >> X;
    for(int i=1;i<5;++i){    
      for(int j=0;j<4;++j){
        cin >> Y;
        if (i!=X) {
          S.insert(Y);
        }
      }
    } 
  }
  if (sz(S)==16) {
    cout << CHEAT << endl;
    return;
  }
  if (sz(S)<15) {
    cout << BAD << endl;
    return;
  }
  for(int i=0;i<16;++i){
    if (S.find(i+1)==S.end()) {
      cout << i+1 << endl;
      return;
    }
  }
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
