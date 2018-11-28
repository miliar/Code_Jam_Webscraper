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

void solve() {
  int k, n;
  cin >> n >> k;
  vector<double> p(n);
  cin >> p;
  sort(p);
  double res = 0;
  for (int i = 0; i <= k; ++i) {
    vector<double> q;
    for (int j = 0; j < i; ++j) q.emplace_back(p[j]);
    for (int j = 0; j < k - i; ++j) q.emplace_back(p[n - 1 - j]);
    vector<double> dp1(n + 1), dp2(n + 1);
    dp1[0] = 1;
    for (auto p : q) {
      for (int j = 0; j < n; ++j) {
        dp2[j] += dp1[j] * (1 - p);
        dp2[j + 1] += dp1[j] * p;
      }
      dp1 = move(dp2);
      dp2.clear();
      dp2.resize(n + 1);
      //for (auto p : dp1) cerr << p << " ";
      //cerr << endl;
    }
    res = max(res, dp1[k / 2]);
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
