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

bool is_pal(lli n)
{
  string s;
  stringstream ss;
  ss << n;
  s = ss.str();
  string t = s;
  reverse(t.begin(), t.end());
  for (int i = 0; i < t.size(); ++i) {
    if (t[i] != s[i]) return false;
  }
  return true;
}

int main(int argc, char *argv[])
{
  const lli N = 100000000000000LL;
  vector<lli> v;
  for (lli n = 1; n * n <= N; ++n) {
    if (is_pal(n) && is_pal(n * n)) v.push_back(n * n);
  }

  int tc;
  cin >> tc;
  while (tc--) {
    lli small, large;
    cin >> small >> large;
    int cnt = 0;
    for (int i = 0; i < v.size(); ++i) {
      cnt += (small <= v[i] && v[i] <= large);
    }
    static int TC = 0;
    cout << "Case #" << ++TC << ": " << cnt << endl;
  }
  return 0;
}
