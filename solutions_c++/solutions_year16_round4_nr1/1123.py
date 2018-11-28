#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;


int v[13][3];
string PAT = "RPS";
string PP[] = {"RS", "PR", "PS"};

string print(int N, int s) {
  // cerr << N << ", " << s << endl;
  if (N == 1) {
    return PP[s];
  }

  string s1 = print(N-1, s);
  string s2 = print(N-1, (s+2) % 3);
  if (s1 < s2) return s1 + s2;
  return s2 + s1;
}

void go(int N, int R, int P, int S) {
  if (R == v[N][0] && P == v[N][1] && S == v[N][2]) {
    cout << print(N, 0) << endl;
    return;
  }
  if (P == v[N][0] && S == v[N][1] && R == v[N][2]) {

    cout << print(N, 1) << endl;
    return;
  }
  if (S == v[N][0] && R == v[N][1] && P == v[N][2]) {
    cout << print(N, 2) << endl;
    return;
  }
  cout << "IMPOSSIBLE" << endl;
}


int main() {
  v[1][0] = 1;
  v[1][1] = 0;
  v[1][2] = 1;
  for (int n = 2; n <= 12; n++) {
    v[n][0] = v[n-1][0] + v[n-1][1];
    v[n][1] = v[n-1][1] + v[n-1][2];
    v[n][2] = v[n-1][2] + v[n-1][0];
  }

  int T;
  cin>>T;
  for (int t = 1; t <= T; t++) {
    int N, R, P, S;

    cin >> N >> R >> P >> S;
    cout << "Case #" << t << ": ";
    go(N, R, P, S);
  }
}
