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
    lli n;
    cin >> n;
    lli last = -1;
    set<int> vis;
    for (int i = 1; i <= 10000100; ++i) {
      lli m = n * i;
      while (m) {
        vis.insert(m % 10);
        m /= 10;
      }
      if (vis.size() == 10) {
        last = n * i;
        break;
      }
    }

    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << flush;
    if (last == -1) cout << "INSOMNIA" << endl;
    else cout << last << endl;
  }
  return 0;
}
