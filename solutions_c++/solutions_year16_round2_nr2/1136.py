#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<double> vd;
typedef vector<long double> vld;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<pii> vii;
typedef vector<vector<int>> vvi;
typedef vector<vector<ll>> vvl;

#define VAR(a, b) __typeof(b) a=(b)
#define DEBUG(x) cerr << #x " = " << (x) << endl
#define CLR(a, val) memset(a, val, sizeof(a))
#define REP(i, n) for (int i = 0, _n = (n); i < _n; i++)
#define FOR(i, a, b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i, a, b) for (int i = (a), _b = (b); i >= _b; i--)
#define PB push_back
#define MP make_pair
#define MT make_tuple

template<class T1, class T2>
ostream& operator << (ostream &o, const pair<T1, T2> &p) {
  return o << "(" << p.first << ", " << p.second << ")";
}

template<class T1, class T2, class T3>
ostream& operator << (ostream &o, const tuple<T1, T2, T3> &t) {
  return o << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ")";
}

template<class T1, class T2, class T3, class T4>
ostream& operator << (ostream &o, const tuple<T1, T2, T3, T4> &t) {
  return o << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ", " << get<3>(t) << ")";
}

template<class T>
ostream& operator << (ostream &o, const vector<T> &v) {
  o << '{';
  for (auto it = v.begin(); it != v.end(); ++it)
    o << (it == v.begin() ? "" : ", ") << *it;
  return o << '}';
}

template<class T>
ostream& operator<<(ostream &o, const set<T> &s) {
  o << '{';
  for (auto it = s.begin(); it != s.end(); ++it)
    o << (it == s.begin() ? "" : ", ") << *it;
  return o << '}';
}

template<class K, class V>
ostream& operator<<(ostream &o, const map<K, V> &m) {
  o << '{';
  for (auto it = m.begin(); it != m.end(); ++it)
    o << (it == m.begin() ? "" : ", ") << it->first << ": " << it->second;
  return o << '}';
}

class runner {
public:
  string C, J;
  string res;

  void read() {
    cin >> C >> J;
  }

  void run(void) {
    int n = C.size();
    auto res = MT(-1, -1, -1);
    char cres[100];
    REP(i, 1000)
      REP(j, 1000) {
        int c0 = i % 10;
        int c1 = (i/10) % 10;
        int c2 = (i/100) % 10;
        int j0 = j % 10;
        int j1 = (j/10) % 10;
        int j2 = (j/100) % 10;
        if (n == 1) {
          int c = c0;
          int j = j0;
          int d = abs(c - j);
          auto tres = MT(d, c, j);
          if (C[0] == '?' || C[0]-'0' == c0)
          if (J[0] == '?' || J[0]-'0' == j0)
            if (get<0>(res) == -1 || tres < res) {
              res = tres;
              sprintf(cres, "%01d %01d", c, j);
            }
        } else if (n == 2) {
          int c = 10*c1 + c0;
          int j = 10*j1 + j0;
          int d = abs(c - j);
          auto tres = MT(d, c, j);
          if (C[0] == '?' || C[0]-'0' == c1)
          if (C[1] == '?' || C[1]-'0' == c0)
          if (J[0] == '?' || J[0]-'0' == j1)
          if (J[1] == '?' || J[1]-'0' == j0)
            if (get<0>(res) == -1 || tres < res) {
              res = tres;
              sprintf(cres, "%02d %02d", c, j);
            }
        } else {
          int c = 100*c2 + 10*c1 + c0;
          int j = 100*j2 + 10*j1 + j0;
          int d = abs(c - j);
          auto tres = MT(d, c, j);
          if (C[0] == '?' || C[0]-'0' == c2)
          if (C[1] == '?' || C[1]-'0' == c1)
          if (C[2] == '?' || C[2]-'0' == c0)
          if (J[0] == '?' || J[0]-'0' == j2)
          if (J[1] == '?' || J[1]-'0' == j1)
          if (J[2] == '?' || J[2]-'0' == j0)
            if (get<0>(res) == -1 || tres < res) {
              res = tres;
              sprintf(cres, "%03d %03d", c, j);
            }
        }
      }
    ostringstream oss;
    oss << cres;
    this->res = oss.str();
  }

  static void *run_helper(void *context) {
    ((runner *)context)->run();
    return 0;
  }
};

int main(int argc, char *argv[]) {
  int T = 0;
  cin >> T; //cin.getline(NULL, 0);

  int from = 0, to = T-1;
  if (argc == 3) {
    from = atoi(argv[1])-1;
    to = min(to, atoi(argv[2])-1);
  }

  vector<runner> runners(T);
  for (int t = 0; t < T; t++)
    runners[t].read();

  #ifdef _MT_
    pthread_attr_t attrs;
    pthread_attr_init(&attrs);
    pthread_attr_setstacksize(&attrs, 256*1024*1024);

    vector<pthread_t> threads(T);
    for (int t = from; t <= to; t++)
      pthread_create(&threads[t], &attrs, &runner::run_helper, &runners[t]);
    for (int t = from; t <= to; t++)
      pthread_join(threads[t], NULL);
  #else
    for (int t = from; t <= to; t++)
      runners[t].run();
  #endif

  for (int t = from; t <= to; t++)
    cout << "Case #" << (t + 1) << ": " << runners[t].res << endl;

  return 0;
}
