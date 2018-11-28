#include <algorithm>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define each(i, c) FOR(i, c)

#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

const int N = 2000;

struct S {
  int i, j, k;
  S() { i = j = k = -1; }
  S(int i_, int j_, int k_) : i(i_), j(j_), k(k_) {}
};
pair<int, int> path[N][N];

void f(void)
{
  const int di[] = {-1, +1, 0, 0};
  const int dj[] = {0, 0, -1, +1};

  pair<int, int> nil = make_pair(-1, -1);
  fill(&path[0][0], &path[N - 1][N - 1] + 1, nil);

  queue<S> q;
  for (q.push(S(N / 2, N / 2, 1)); q.size(); q.pop()) {
    S curr = q.front();
    for (int d = 0; d < 4; ++d) {
      int ni = curr.i + di[d] * curr.k;
      int nj = curr.j + dj[d] * curr.k;
      unless (0 <= ni && ni < N) continue;
      unless (0 <= nj && nj < N) continue;
      if (path[ni][nj] == nil) {
        path[ni][nj] = make_pair(curr.i, curr.j);
        q.push(S(ni, nj, curr.k + 1));
      }
    }
  }
  return ;
}

int main(int argc, char *argv[])
{
  f();

  int tc;
  cin >> tc;
  while (tc--) {
    int j, i;
    cin >> j >> i;
    j += N / 2;
    i += N / 2;

    string s;
    while (true) {
      if (i == N / 2 && j == N / 2) break;
      int pi = path[i][j].first;
      int pj = path[i][j].second;
      if (pi == i) {
        if (pj < j) s += 'E';
        else s += 'W';
      }
      if (pj == j) {
        if (pi < i) s += 'N';
        else s += 'S';
      }
      i = pi;
      j = pj;
    }
    reverse(s.begin(), s.end());

    if (0) {
      int x = 0, y = 0;
      for (int i = 0; i < s.size(); ++i) {
        if (s[i] == 'N') y += (i + 1);
        if (s[i] == 'S') y -= (i + 1);
        if (s[i] == 'E') x += (i + 1);
        if (s[i] == 'W') x -= (i + 1);
      }
      cout << x << ' ' << y << endl;
    }

    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << s << endl;
  }
  return 0;
}
