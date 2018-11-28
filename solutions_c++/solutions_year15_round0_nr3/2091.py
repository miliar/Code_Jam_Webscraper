/*
ID: ahri1
PROG: C
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

const string YES = "YES";
const string NO = "NO";


int get(char c) {
  switch (c) {
    case 'i':
      return 1;
    case 'j':
      return 2;
    case 'k':
      return 3;
  }
  return -1;
}

int t[][4] = {
// 1  i  j  k
  {0, 1, 2, 3}, //  1
  {1, 4, 3, 6}, //  i
  {2, 7, 4, 1}, //  j
  {3, 2, 5, 4}, //  k
  {4, 5, 6, 7}, // -1
  {5, 0, 7, 2}, // -i
  {6, 3, 0, 5}, // -j
  {7, 6, 1, 0}, // -k
};

string calc(int64 L, int64 X, string chunk) {
  int N = L * X;
  if (N < 3) return NO;
  string S = "";
  for (int i = 0; i < X; ++i) {
    S += chunk;
  }
  int state = 0;
  int target_state = 1;
  for (int i = 0; i < N; ++i) {
    state = t[state][get(S[i])];
    if (state == target_state) {
      state = 0;
      target_state++;
      if (target_state > 3) target_state = 100;
    }
//    cerr << state << endl;
  }
  if (target_state == 100 && state == 0) return YES;
  return NO;
}

void solve(){
  int64 L, X;
  string S;
  cin >> L >> X;
  cin >> S;
  cout << calc(L, X, S) << '\n';
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
