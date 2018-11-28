// Author: Chi-Kit (George) LAM
#include <bits/stdc++.h>
using namespace std;
#define DEBUG_ENABLED 1
namespace jam{
  typedef long long LL;
  struct Jam {
    Jam(unsigned int seed) {
      srand(seed);
      cout.precision(9);
    }
  };
#if DEBUG_ENABLED
  #define DEBUG(...) \
    (cout << "DEBUG:" << __LINE__ << ": (" << #__VA_ARGS__ \
          << ") = " << make_tuple(__VA_ARGS__) << endl)
  template <size_t I, class... Types> struct TuplePrinter {
    void print(ostream& out, const tuple<Types...>& x) const {
      TuplePrinter<I-1, Types...>().print(out, x);
      out << ", " << get<I-1>(x);
    }
  };
  template <class... Types> struct TuplePrinter<1, Types...> {
    void print(ostream& out, const tuple<Types...>& x) const {
      out << get<0>(x);
    }
  };
  template <class... Types>
  ostream& operator<<(ostream& out, const tuple<Types...>& x) {
    out << "(";
    TuplePrinter<sizeof...(Types), Types...>().print(out, x);
    return out << ")";
  }
  template <class T1, class T2>
  ostream& operator<<(ostream& out, pair<T1, T2> x) {
    return out << tuple<T1, T2>(x);
  }
  template <class T, class Alloc>
  ostream& operator<<(ostream& out, const deque<T, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& v : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << v;
    }
    return out << "}";
  }
  template <class T, class Compare, class Alloc>
  ostream& operator<<(ostream& out, const set<T, Compare, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& v : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << v;
    }
    return out << "}";

  }
  template <class Key, class T, class Compare, class Alloc>
  ostream& operator<<(ostream& out, const map<Key, T, Compare, Alloc>& x) {
    out << "{";
    bool flag = true;
    for (auto& kv : x) {
      if (flag) {
        flag = false;
      } else {
        out << ", ";
      }
      out << kv->first << ": " << kv->second;
    }
    return out << "}";
  }
#else
  #define DEBUG(...)
#endif
} // namespace jam
using namespace jam;
Jam JAM(/*seed*/ 0);

int N;
double S;
int X[1000][3];
int V[1000][3];

int sq(int x) {
  return x*x;
}

int d(int i, int j) {
  return sq(X[i][0]-X[j][0]) + sq(X[i][1]-X[j][1]) + sq(X[i][2]-X[j][2]);
}

bool f(double t) {
  //DEBUG(t);
  queue<int> Q;
  deque<int> visited(N, 0);
  Q.push(1);
  visited[1] = 1;
  while (!Q.empty()) {
    int u = Q.front(); Q.pop();
    for (int i=0; i<N; ++i) {
      if (visited[i] == 0 && d(u,i) <= t*t) {
        Q.push(i);
        visited[i] = 1;
      }
    }
  }
  return visited[0];
}

void solve(int T) {
  cin >> N >> S;
  for (int i=0; i<N; ++i) {
    cin >> X[i][0] >> X[i][1] >> X[i][2];
    cin >> V[i][0] >> V[i][1] >> V[i][2];
  }
  
  double a = 0, b = 3000;
  while (b-a > 1e-5) {
    double m = (a+b)/2;
    if (f(m)) {
      b = m;
    } else {
      a = m;
    }
  }
  
  cout << "Case #" << T << ": " << a << endl;
}
int main(){
  int T;
  cin >> T;
  for (int i=0; i<T; ++i) {
    solve(i+1);
  }
  return 0;
}
