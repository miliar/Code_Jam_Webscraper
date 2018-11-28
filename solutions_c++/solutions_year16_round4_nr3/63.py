#include <bits/stdc++.h>

using namespace std;

struct Initializer {
  Initializer() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    cout << fixed << setprecision(15);
  }
} initializer;

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

class UnionFind {
private:
  int n;
  vector<int> a;
public:
  UnionFind(int n) : n(n), a(n, -1) {}
  int find(int x) {return a[x] < 0 ? x : (a[x] = find(a[x]));}
  bool equal(int x, int y) {return find(x) == find(y);}
  void unite(int x, int y) {
    x = find(x), y = find(y);
    if (x == y) return;
    if (a[x] > a[y]) swap(x, y);
    a[x] += a[y];
    a[y] = x;
    --n;
  }
  int size() {return n;}
  int size(int x) {return -a[find(x)];}
};

void solve() {
  int r, c;
  cin >> r >> c;
  vector<int> v(2 * r + 2 * c);
  cin >> v;
  for (int& i : v) {
    if (1 <= i && i <= c) {
      --i;
    } else if (r + c < i && i <= r + 2 * c) {
      i -= r + c + 1;
      i = c - i - 1;
      i += r * c;
    } else if (c < i && i <= r + c) {
      i -= c + 1;
      i = r * c + 2 * c + i * (c + 1);
    } else {
      i -= r + 2 * c + 1;
      i = r - i - 1;
      i = r * c + c + i * (c + 1);
    }
  }
  //for (int i : v) cerr << i << " ";
  //cerr << endl;
  vector<vector<int>> g(r, vector<int>(c));
  for (int bit = 0; bit < (1 << (r * c)); ++bit) {
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (bit & (1 << (i * c + j))) g[i][j] = 1;
        else g[i][j] = 0;
      }
    }
    UnionFind uf(2 * r * c + r + c);
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (g[i][j]) {
          uf.unite(i * c + j, r * c + c + i * (c + 1) + j);
          uf.unite(i * c + j + c, r * c + c + i * (c + 1) + j + 1);
        } else {
          uf.unite(i * c + j, r * c + c + i * (c + 1) + j + 1);
          uf.unite(i * c + j + c, r * c + c + i * (c + 1) + j);
        }
      }
    }
    for (int i = 0; i < 2 * r + 2 * c; i += 2) {
      if (!uf.equal(v[i], v[i + 1])) goto next;
      for (int j = 0; j < 2 * r + 2 * c; ++j) {
        if (i == j || i + 1 == j) continue;
        if (uf.equal(v[i], v[j])) goto next;
      }
    }
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (g[i][j]) cout << "/";
        else cout << "\\";
      }
      cout << endl;
    }
    return;
  next:;
  }
  cout << "IMPOSSIBLE" << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ":" << endl;
    solve();
  }
}
