#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

template<typename P, typename Q>
ostream& operator << (ostream& os, pair<P, Q> p)
{
  os << "(" << p.first << "," << p.second << ")";
  return os;
}

const int N = 1000 + 10;
int memo[N];

int rec(int n, const int lim)
{
  int& ret = memo[n];
  if (ret != -1) return ret;
  if (n <= lim) return 0;

  int mn = 1 << 29;
  for (int i = 1; i < n; ++i) {
    mn = min(mn, rec(i, lim) + rec(n - i, lim) + 1);
  }

  return ret = mn;
}

int f(vector<int> v, int lim)
{
  fill(memo, memo + N, -1);
  int sum = 0;
  each (i, v) sum += rec(i, lim);
  return sum;
}

int main(int argc, char *argv[])
{
  int tc;
  for (cin >> tc; tc--; ) {
    int d;
    cin >> d;
    vector<int> v(d);
    for (int i = 0; i < d; ++i) {
      cin >> v[i];
    }

    const int mx = *max_element(v.begin(), v.end());
    int mn = mx;
    for (int i = 1; i <= mx; ++i) {
      int tmp = f(v, i);
      mn = min(mn, tmp + i);
    }

    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << mn << endl;
  }
  return 0;
}
