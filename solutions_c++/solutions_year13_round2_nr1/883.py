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

const int N = 100 + 5;
const int M = 1000000 + 5;
int memo[N][M];
int mote[N];

int rec(int nth, int size, const int lim)
{
  if (nth == lim) return 0;
  if (memo[nth][size] != -1) return memo[nth][size];

  // cout << nth << ' ' << size << endl;

  int best = 1 << 28;

  { // remove
    best = min(best, rec(nth + 1, size, lim) + 1);
  }
  if (1 < size && size < M - 2) { // insert
    int next_size = min(M - 1, size + size - 1);
    best = min(best, rec(nth, next_size, lim) + 1);
  }
  if (mote[nth] < size) { // take
    int next_size = min(M - 1, size + mote[nth]);
    best = min(best, rec(nth + 1, next_size, lim));
  }

  return memo[nth][size] = best;
}

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    int a;
    int n;
    cin >> a >> n;
    for (int i = 0; i < n; ++i) {
      cin >> mote[i];
    }
    sort(mote, mote + n);
    fill(&memo[0][0], &memo[N - 1][M - 1] + 1, -1);
    int best = rec(0, a, n);
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << best << endl;
  }
  return 0;
}
