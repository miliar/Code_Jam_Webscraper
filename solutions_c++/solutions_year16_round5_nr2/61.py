// Author: Chi-Kit (George) LAM
#include <bits/stdc++.h>
using namespace std;
#define DEBUG_ENABLED 0
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

int N, M;
deque<int> children[101];
string names;
deque<string> words;
double sum;
deque<double> cnt;
auto RAND = default_random_engine(0);

string R(int u);

string RR(int u, int k) {
  DEBUG(u,k);
  if (k == 0) {
    return "";
  } else {
    string A = R(children[u][k-1]);
    string B = RR(u,k-1);
    string result = string(A.length(), '0') + string(B.length(), '1');
    shuffle(result.begin(), result.end(), RAND);
    int p = 0, q = 0;
    for (char& c : result) {
      if (c == '0') {
        c = A[p]; ++p;
      } else {
        c = B[q]; ++q;
      }
    }
    return result;
  }
}

string R(int u) {
  DEBUG(u);
  return string(1, names[u]) + RR(u, children[u].size());
}


void f(string s) {
  DEBUG(s);
  for (int i=0; i<M; ++i) {
    if (s.find(words[i]) != string::npos) {
      cnt[i] += 1;
    }
     DEBUG(cnt[i]);
  }
  sum += 1;
}

void solve(int T) {
  cin >> N;
  for (int i=0; i<=N; ++i) {
    children[i].clear();
  }
  for (int i=1; i<=N; ++i) {
    int x;
    cin >> x;
    children[x].push_back(i);
  }
  getline(cin, names);DEBUG(names);getline(cin, names);DEBUG(names);
  names = "0" + names;
  cin >> M;
  sum = 0;
  words = deque<string>(M);
  cnt = deque<double>(M, 0);
  for (int i=0; i<M; ++i) {
    cin >> words[i];
  }
  
  for (int i=0; i<10000; ++i) {
    f(RR(0, children[0].size()));
  }
  
  cout << "Case #" << T << ":" ;
  for (int i=0; i<M; ++i) {
    cout << " " << cnt[i] / sum;
  }
  cout << endl;
}
int main(){
  int T;
  cin >> T;
  for (int i=0; i<T; ++i) {
    cerr << i;
    solve(i+1);
  }
  return 0;
}
