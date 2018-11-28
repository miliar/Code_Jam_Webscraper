#include <bits/stdc++.h>

using namespace std;

struct Initializer {
  Initializer() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    cout << fixed << setprecision(15);
  }
} initializer;

template<typename T> int least_bit(T n) {
  static_assert(sizeof(T) == 4 || sizeof(T) == 8, "unsupported size");
  if (sizeof(T) == 4) return __builtin_ffs(n) - 1;
  if (sizeof(T) == 8) return __builtin_ffsll(n) - 1;
}

template<typename T> int most_bit(T n) {
  static_assert(sizeof(T) == 4 || sizeof(T) == 8, "unsupported size");
  if (sizeof(T) == 4) return n ? 31 - __builtin_clz(n) : -1;
  if (sizeof(T) == 8) return n ? 63 - __builtin_clzll(n) : -1;
}

template<typename T> int count_bit(T n) {
  static_assert(sizeof(T) == 4 || sizeof(T) == 8, "unsupported size");
  if (sizeof(T) == 4) return __builtin_popcount(n);
  if (sizeof(T) == 8) return __builtin_popcountll(n);
}

template <typename T> inline istream& operator>>(istream &s, vector<T> &v) {
  for (T &t : v) s >> t;
  return s;
}

template <typename T> inline ostream& operator<<(ostream &s, const vector<T> &v) {
  for (const T &t : v) s << t << endl;
  return s;
}

template<typename T> inline T min(vector<T>& v) {return *min_element(v.begin(), v.end());}

template<typename T> inline T max(vector<T>& v) {return *max_element(v.begin(), v.end());}

template<typename T> inline void sort(vector<T>& v) {sort(v.begin(), v.end());}

template<typename T, typename Function> inline void sort(vector<T>& v, Function func) {sort(v.begin(), v.end(), func);}

template<typename T> inline void rsort(vector<T>& v) {sort(v.rbegin(), v.rend());}

template<typename T> inline void reverse(vector<T>& v) {reverse(v.begin(), v.end());}

template<typename T> inline void unique(vector<T>& v) {v.erase(unique(v.begin(), v.end()), v.end());}

template<typename T> inline void nth_element(vector<T>& v, int n) {nth_element(v.begin(), v.begin() + n, v.end());}

template<typename T> inline bool next_permutation(vector<T>& v) {return next_permutation(v.begin(), v.end());}

template<typename T> inline int find(vector<T>& v, T t) {return find(v.begin(), v.end(), t) - v.begin();}

template<typename T> inline int in(vector<T> v, T t) {return find(v, t) != (int)v.size();}

template<typename T> inline int lower_bound(vector<T>& v, T t) {return lower_bound(v.begin(), v.end(), t) - v.begin();}

template<typename T> inline int upper_bound(vector<T>& v, T t) {return upper_bound(v.begin(), v.end(), t) - v.begin();}

template<typename T> inline T accumulate(const vector<T>& v) {return accumulate(v.begin(), v.end(), T(0));}

template<typename T> inline void adjacent_difference(vector<T>& v, vector<T>& u) {adjacent_difference(v.begin(), v.end(), u.begin());}

template<typename T> inline void partial_sum(vector<T>& v, vector<T>& u) {partial_sum(v.begin(), v.end(), u.begin());}

template<typename T> inline T inner_product(vector<T>& v, vector<T>& u) {return inner_product(v.begin(), v.end(), u.begin(), T(0));}

template<typename T, typename Function> inline int count_if(vector<T> v, Function func) {return count_if(v.begin(), v.end(), func);}

template<typename T, typename Function> inline void remove_if(vector<T>& v, Function func) {v.erase(remove_if(v.begin(), v.end(), func), v.end());}

template<typename T, typename Function> inline bool any_of(vector<T> v, Function func) {return any_of(v.begin(), v.end(), func);}

void solve() {
  int n;
  cin >> n;
  vector<string> v(n);
  cin >> v;
  int res = 1e9;
  for (int bit = 0; bit < (1 << n * n); ++bit) {
    int r = count_bit(bit);
    if (res <= r) continue;
    bool ok = true;
    auto u = v;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (bit & (1 << (i * n + j))) {
          if (v[i][j] == '1') ok = false;
          u[i][j] = '1';
        }
      }
    }
    if (!ok) continue;
    vector<int> per;
    for (int i = 0; i < n; ++i) per.emplace_back(i);
    do {
      vector<int> p;
      for (int i = 0; i < n; ++i) p.emplace_back(i);
      do {
        int used = 0;
        for (int ii = 0; ii < n; ++ii) {
          int i = per[ii];
          if (u[i][p[i]] == '0') {
            bool ok = false;
            for (int j = 0; j < n; ++j) {
              if (u[i][j] == '1' && !(used & 1 << j)) ok = true;
            }
            if (!ok) goto next;
            break;
          }
          used |= 1 << p[i];
        }
      } while (next_permutation(p.begin(), p.end()));
    } while (next_permutation(per.begin(), per.end()));
    res = r;
  next:;
  }
  cout << res;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
}
