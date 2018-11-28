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

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    int n;
    cin >> n;
    vector<pair<string, string>> v;
    for (int i = 0; i < n; ++i) {
      string a, b;
      cin >> a >> b;
      v.push_back(make_pair(a, b));
    }

    set<string> x, y;
    each (i, v) { x.insert(i.first); y.insert(i.second); }

    int mn = n;
    for (int bit = 0; bit < (1 << n); ++bit) {
      set<string> a, b;
      for (int i = 0; i < n; ++i) {
        if (bit & (1 << i)) {
          a.insert(v[i].first);
          b.insert(v[i].second);
        }
      }
      if (x == a && y == b) mn = min(mn, __builtin_popcount(bit));
    }
    static int t = 0;
    cout << "Case #" << ++t << ": " << n - mn << endl;
  }
  return 0;
}
