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
  for (cin >> tc; tc--; ) {
    int n;
    string s;
    cin >> n >> s;
    for (int i = 0; i < s.size(); ++i) {
      s[i] -= '0';
    }
    int sum = 0;
    int mx = 0;
    for (int i = 0; i < s.size(); ++i) {
      mx = max(mx, i - sum);
      sum += s[i];
    }
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << mx << endl;
  }
  return 0;
}
