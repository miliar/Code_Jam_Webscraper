#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T, typename U> inline void relaxmax(T &res, const U &x) {
  if (x > res) {
    res = x;
  }
}
typedef long long int64;
#define foreach(i,c) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i )

int N;
vector<int> A, B;

bool rek(int x, vector<int> &pos, vector<int> &X) {
  if (x > N) {
    return 1;
  }
  
  for (int i=0; i<N; ++i) {
    if (X[i] != -1) {
      continue;
    }
    int a=1, b=1;
    for (int m=1; m<x; ++m) {
      if (pos[m] < i) {
        relaxmax(a, A[pos[m]] + 1);
      } else {
        relaxmax(b, B[pos[m]] + 1);
      }
    }
    if (a == A[i] && b == B[i]) {
      pos[x] = i;
      X[i] = x;
      if (rek(x+1, pos, X)) {
        return 1;
      }
      X[i] = -1;
      pos[x] = -1;
    }
  }
  return 0;
}

void solve1() {
  cin >> N;
  A.resize(N);
  B.resize(N);
  foreach (it, A) cin >> *it;
  foreach (it, B) cin >> *it;

  vector<int> pos(N+1, -1), out(N, -1);

  rek(1, pos, out);
  foreach (it, out) {
    cout << ' ' << *it;
  }
}

int main() {
  cin.sync_with_stdio(0);

  int64 T;
  cin >> T;
  for (int64 tt=1; tt<=T; ++tt) {
    cout << "Case #" << tt << ":";
    solve1();
    cout << '\n';
  }
  
  return 0;
}
