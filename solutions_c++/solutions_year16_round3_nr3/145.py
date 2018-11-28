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
  int J, P, S, K;
  string res;

  void read() {
    cin >> J >> P >> S >> K;
  }

  void run(void) {
    vector<tuple<int, int, int>> T;
    REP(i, J)
      REP(j, P)
        REP(k, S)
          T.PB(MT(i, j, k));
    int N = T.size();

    int F[J+1][P+1][S+1];
    int res = -1, ress = 0;
    REP(s, 1<<N) {
      int cres = 0;
      bool ok = true;
      int a, b, c;
      CLR(F, 0);
      REP(bit, N) {
        if (s & (1 << bit)) {
          tie(a, b, c) = T[bit];
          F[a][b][S]++;
          F[a][P][c]++;
          F[J][b][c]++;
          cres++;
          if (F[a][b][S] > K || F[a][P][c] > K || F[J][b][c] > K) {
            ok = false;
            break;
          }
        }
      }
      if (ok && (res == -1 || cres > res))
        res = cres, ress = s;
    }

    ostringstream oss;
    oss << res;
    REP(b, N) {
      if (ress & (1 << b)) {
        auto &t = T[b];
        oss << endl << (get<0>(t)+1) << " " << (get<1>(t)+1) << " " << (get<2>(t)+1);
      }
    }
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
