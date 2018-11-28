#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;

int N;

inline int bit(int i, int j) {
  return 1 << (i * N + j);
}

static int const T = 4;
#define bs(x) bitset<T>(x)

bool can(int n, int mask, int mach, int work) {
  //cerr << n << " " << bs(mask) << " " << bs(mach) << " " << bs(work) << endl;
  if (mach == 0) {
    return true;
  }
  if (n == 0) {
    return false;
  }
  FOR(i, 0, N) {
    if (work>>i&1) continue;
    bool ok = false;
    FOR(j, 0, N) {
      if ((mask & bit(i, j)) && (mach>>j&1)) {
        ok = true;
        if (!can(n - 1, mask, mach^(1<<j), work^(1<<i))) return false;
      }
    }
    if (!ok) return false;
  }
  return true;
}

void solve(int testcase) {
  cout << "Case #" << testcase << ": ";
  int n;
  cin >> n;
  N = n;
  int mask = 0;
  FOR(i, 0, n) {
    string s;
    cin >> s;
    FOR(j, 0, n) {
      if (s[j]=='1') mask |= bit(i, j);
    }
  }
  //cerr<<bitset<T>(mask)<<endl;
  int res = n*n;
  FOR(i, 0, 1<<(n*n)) {
    if ((i & mask) != mask) continue;
    if (can(n, i, (1<<n)-1, 0)) {
      //cerr << endl;
      //cerr << bitset<T>(i) << endl;
      //cerr << bitset<T>(i^mask) << endl;
      res = min(res, __builtin_popcount(i ^ mask));
    }
  }
  cout << res << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve(testcase);
  }

  return 0;
}
