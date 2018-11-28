#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <sstream>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cctype>
#include <cassert>
#include <cstring>
// #include <bits/stdc++.h>
using namespace std;

#define REP(i, x, n) for(int i = x; i < (int)(n); i++)
#define rep(i, n) REP(i, 0, n)
#define all(x) (x).begin(), (x).end()
#define F first
#define S second
#define mp make_pair
#define pb push_back

typedef pair<int,int> P;
typedef long long int lli;

// const int INF = (1 << 29);
const double EPS = 1e-9;
const double PI = acos(-1.0);

int A, B, K;

void solve() {
  int ans = 0;
  rep(i, A) rep(j, B) {
    if((i & j) < K) ans++;
  }
  cout << ans << endl;
}

void input() {
  cin >> A >>  B >> K;
}

int main() {
  // ios_base::sync_with_stdio(false);
  
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; tc++) {
    input();
    cout << "Case #" << tc << ": ";
    solve();
  }

  return 0;
}
