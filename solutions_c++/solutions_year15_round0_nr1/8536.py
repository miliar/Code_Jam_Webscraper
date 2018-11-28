#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0;i<(n);++i)
#define loop for(;;)
#define trace(var) cerr<<">>> "<<#var<<" = "<<var<<endl;
#define inf (1e9)
#define eps (1e-9)
using Integer = long long;
using Real = long double;
const Real PI = acos(-1);

template<class S, class T> inline
ostream& operator<<(ostream&os, pair<S,T> p) {
  os << '(' << p.first << ", " << p.second << ')';
  return os;
}

template<class T> inline
ostream& operator<<(ostream&os, vector<T> v) {
  if (v.size() == 0) {
    os << "(empty)";
    return os;
  }
  os << v[0];
  for (int i=1, len=v.size(); i<len; ++i) os << ' ' << v[i];
  return os;
}

template<class T> inline
istream& operator>>(istream&is, vector<T>&v) {
  rep (i, v.size()) is >> v[i];
  return is;
}

int dx[] = { -1, 0, 1, 0 };
int dy[] = {  0, -1, 0, 1 };

using vi = vector<int>;
using vvi = vector<vi>;

void solve (int t)
{
  int m; cin >> m;
  string s; cin >> s;

  vi xs(m+1, 0);
  vi ys(m+1, 0);

  rep (i, m + 1) {
    int x = s[i] - '0';
    xs[i] = x;
  }

  int f = 0;
  rep (_, m + 1) {
    bool succ = true;

    rep (i, m + 1) ys[i] = xs[i];
    ys[0] = xs[0] + f;

    for (int i = 1; i <= m; ++i) {
      if (ys[i - 1] < i) {
        succ = false;
        break;
      }
      ys[i] += ys[i - 1];
    }

    if (succ) break;
    ++f;
  }

  cout << "Case #" << (t + 1) << ": " << f << endl;
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(0);
  cout.setf(ios::fixed);
  cout.precision(10);

  int t; cin >> t;
  rep (_, t) solve(_);

  return 0;
}
