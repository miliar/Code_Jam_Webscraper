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

typedef __int128_t int128;
typedef long long int64;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<double> vd;
typedef vector<long double> vld;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<pii> vii;
typedef vector<vector<int>> vvi;
typedef vector<vector<int64>> vvl;

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

template<class T>
bool isprime(T n) {
  if (n == 2 || n == 3) return true;
  if (n < 2 || n%2 == 0 || n%3 == 0) return false;
  T lim = sqrt(n);
  for (T i = 5; i <= lim; i += 6)
    if (n%i == 0 || n%(i+2) == 0)
      return false;
  return true;
}

class runner {
public:
  int N, J;
  string res;

  void read() {
    cin >> N >> J;
  }

  void run(void) {
    vi P;
    FOR(i, 2, 1000)
      if (isprime(i))
        P.PB(i);

    ostringstream oss;
    int c = 0;
    int mx = 1 << (N-2);
    for (int s = 0; s < mx && c < J; s++) {
      bool ok = true;
      for (int b = 2; b <= 10 && ok; b++) {
        int128 v = 1;
        REP (i, N-2)
          v = v*b + (s & (1 << i) ? 1 : 0);
        v = v*b + 1;

        bool hasdiv = false;
        for (int i = 0; i < P.size() && !hasdiv; i++)
          if (v % P[i] == 0)
            hasdiv = true;

        if (!hasdiv)
          ok = false;
      }
      if (ok) {
        string S = "1";
        REP(i, N-2)
          S.append(1, (s & (1 << i)) ? '1' : '0');
        S.append(1, '1');
        oss << endl;
        oss << S;
        FOR (b, 2, 10) {
          int128 v = 1;
          REP (i, N-2)
            v = v*b + (s & (1 << i) ? 1 : 0);
          v = v*b + 1;
          int64 mx = sqrt(v);
          for (int64 i = 2; i <= mx; i++)
            if (v % i == 0) {
              oss << " " << i;
              break;
            }
        }
        c++;
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
  if (argc == 2) {
    from = atoi(argv[0])-1;
    to = min(to, atoi(argv[1])-1);
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
