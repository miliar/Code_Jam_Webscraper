#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define DEBUG(x) cerr << #x << " = " << (x) << endl

#define FR first
#define SC second

using namespace std;

typedef long long ll;
typedef long double ld;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

int hire(const vector<vector<int> >& ch, const vector<int>& s, const vector<int>& m, vector<bool>& active, int lo, int hi, int node) {
  if (node != 0 && !active[m[node]]) return 0;
  if (active[node]) return 0;
  if (s[node] < lo || s[node] >= hi) return 0;
  active[node] = true;
  int ret = 1;
  for (int i = 0; i < int(ch[node].size()); ++i) {
    ret += hire(ch, s, m, active, lo, hi, ch[node][i]);
  }
  return ret;
}

int fire(const vector<vector<int> >& ch, vector<bool>& active, int node) {
  if (node == 0) return 0;
  if (!active[node]) return 0;
  active[node] = false;
  int ret = -1;
  for (int i = 0; i < int(ch[node].size()); ++i) {
    ret += fire(ch, active, ch[node][i]);
  }
  return ret;
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int n, d;
    cin >> n >> d;

    vector<int> s(n);
    int as, cs, rs;
    cin >> s[0] >> as >> cs >> rs;
    for (int i = 0; i < n - 1; ++i) {
      s[i + 1] = (s[i] * as + cs) % rs;
    }

    vector<int> m(n);
    int am, cm, rm;
    cin >> m[0] >> am >> cm >> rm;
    for (int i = 0; i < n - 1; ++i) {
      m[i + 1] = (m[i] * am + cm) % rm;
    }
    m[0] = -1;
    for (int i = 1; i < n; ++i) {
      m[i] %= i;
    }

    vector<vector<int> > cla(rs);
    vector<vector<int> > ch(n);
    for (int i = 0; i < n; ++i) {
      cla[s[i]].push_back(i);
      if (m[i] != -1) {
        ch[m[i]].push_back(i);
      }
    }

    int mx_num_active = 0;
    vector<bool> active(n, false);
    int num_active = 0;
    for (int lo = s[0] - d, hi = s[0] - d; lo <= s[0]; ++lo) {
      if (lo - 1 >= 0 && lo - 1 < int(cla.size())) {
        for (int i = 0; i < int(cla[lo - 1].size()); ++i) {
          num_active += fire(ch, active, cla[lo - 1][i]);
        }
      }
      for (; hi <= lo + d; ++hi) {
        if (hi >= 0 && hi < int(cla.size())) {
          for (int i = 0; i < int(cla[hi].size()); ++i) {
            num_active += hire(ch, s, m, active, lo, hi + 1, cla[hi][i]);
          }
        }
      }
      if (num_active > mx_num_active) {
        mx_num_active = num_active;
      }
    }
    cout << "Case #" << ca << ": " << mx_num_active << endl;
  }
}

