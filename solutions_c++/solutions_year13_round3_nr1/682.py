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

bool f(char c)
{
  if ('a' == c) return false;
  if ('i' == c) return false;
  if ('u' == c) return false;
  if ('e' == c) return false;
  if ('o' == c) return false;
  return true;
}

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    string s;
    int n;
    cin >> s >> n;

    const int N = s.size() + 10;
    int m[N];
    fill(m, m + N, 0);
    for (int i = 0; i < s.size(); ++i) {
      if (f(s[i])) m[i + 1] += m[i] + 1;
      else m[i + 1] = 0;
    }

    // cout << "m: " ;
    // for (int i = 0; i < s.size() + 1; ++i) {
    //   cout << m[i] << ", ";
    // }
    // cout << endl;

    vector<int> v;
    for (int i = 0; i < N; ++i) {
      if (n <= m[i]) v.push_back(i);
    }

    // cout << "v: ";
    // for (int i = 0; i < v.size(); ++i) {
    //   cout << v[i] <<  ' ';
    // }
    // cout << endl;

    lli sum = 0;
    for (int i = 0; i + n <= s.size(); ++i) {
      vector<int>::iterator itr = lower_bound(v.begin(), v.end(), i + n);
      if (itr == v.end()) continue;
      int j = itr - v.begin();
      sum += s.size() - v[j] + 1;


      // cout<< i << ' ' << v[j] << endl;
      // for (int k = i; k < v[j]; ++k) {
      //   cout << s[k];
      // }
      // for (int k = v[j]; k < s.size(); ++k) {
      //   cout << ".";
      // }
      // cout << endl;

    }

    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << sum << endl;
  }
  return 0;
}
