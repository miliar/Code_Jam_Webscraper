#include <assert.h>
#include <memory.h>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define pb push_back
#define INF 1011111111
#define FOR(i, a, b) for (int _n(b), i(a); i < _n; i++)
#define rep(i, n) FOR(i, 0, n)
#define CL(a, v) memset((a), (v), sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> pii;

/*** TEMPLATE CODE ENDS HERE */

char looser(char x) {
  switch (x) {
    case 'R':
      return 'S';
    case 'S':
      return 'P';
    case 'P':
      return 'R';
  }
  throw int();
}

int id(char x) {
  switch (x) {
    case 'R':
      return 0;
    case 'S':
      return 1;
    case 'P':
      return 2;
  }
  throw int();
}

int N;
int cnt[256];
string mem[14][3];

string go(char winner, int at, int lvl) {
  if (at >= N) {
    return string(1, winner);
  }
  const int idx = id(winner);
  if (mem[lvl][idx].size()) {
    return mem[lvl][idx];
  }

  char need = looser(winner);
  string x = go(winner, at * 2, lvl + 1) + go(need, at * 2 + 1, lvl + 1);
  string y = go(need, at * 2, lvl + 1) + go(winner, at * 2 + 1, lvl + 1);
  return mem[lvl][idx] = min(x, y);
}

string solve() {
  int n, R, P, S;
  cin >> n >> R >> P >> S;
  N = R + S + P;
  string ans = "";
  rep(i, 14) rep(j, 3) mem[i][j] = "";
  for (char c : {'R', 'P', 'S'}) {
    CL(cnt, 0);
    string s = go(c, 1, 0);
    for (char c : s) cnt[c]++;
    if (cnt['R'] == R && cnt['S'] == S && cnt['P'] == P) {
      if (ans.size() == 0) {
        ans = s;
      } else {
        ans = min(ans, s);
      }
    }
  }
  if (ans.size()) return ans;
  return "IMPOSSIBLE";
}

int main() {
#ifdef LOCAL_HOST
  freopen("A-large.in", "r", stdin);
  //  freopen("A-small-attempt2.in", "r", stdin);
  //  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  cout.sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;
  FOR(tt, 1, T + 1) {
    cout << "Case #" << tt << ": ";
    cout << solve() << endl;
  }

  return 0;
}
