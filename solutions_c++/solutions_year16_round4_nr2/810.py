/*
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            pass System Test!
*/
#include <bits/stdc++.h>
using namespace std;
template <typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<T> &v) {
  if (!v.empty()) {
    out << '[';
    std::copy(v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
    out << "\b\b]";
  }
  return out;
}
template <typename T1, typename T2>
std::ostream &operator<<(std::ostream &out, const std::pair<T1, T2> &p) {
  out << "[" << p.first << ", " << p.second << "]";
  return out;
}
template <class T, class U>
void chmin(T &t, U f) {
  if (t > f) t = f;
}
template <class T, class U>
void chmax(T &t, U f) {
  if (t < f) t = f;
}
template <typename T>
void uniq(vector<T> &v) {
  v.erase(unique(v.begin(), v.end()), v.end());
}
template <class BidirectionalIterator>
bool next_combination(BidirectionalIterator first1, BidirectionalIterator last1,
                      BidirectionalIterator first2,
                      BidirectionalIterator last2) {
  if ((first1 == last1) || (first2 == last2)) {
    return false;
  }
  BidirectionalIterator m1 = last1;
  BidirectionalIterator m2 = last2;
  --m2;
  while (--m1 != first1 && !(*m1 < *m2)) {
  }
  bool result = (m1 == first1) && !(*first1 < *m2);
  if (!result) {
    while (first2 != m2 && !(*m1 < *first2)) {
      ++first2;
    }
    first1 = m1;
    std::iter_swap(first1, first2);
    ++first1;
    ++first2;
  }
  if ((first1 != last1) && (first2 != last2)) {
    m1 = last1;
    m2 = first2;
    while ((m1 != first1) && (m2 != last2)) {
      std::iter_swap(--m1, m2);
      ++m2;
    }
    std::reverse(first1, m1);
    std::reverse(first1, last1);
    std::reverse(m2, last2);
    std::reverse(first2, last2);
  }
  return !result;
}

template <class BidirectionalIterator>
bool next_combination(BidirectionalIterator first, BidirectionalIterator middle,
                      BidirectionalIterator last) {
  return next_combination(first, middle, middle, last);
}

int bitCount(int64_t x) {
  x = (x & 0x55555555) + (x >> 1 & 0x55555555);
  x = (x & 0x33333333) + (x >> 2 & 0x33333333);
  x = (x & 0x0f0f0f0f) + (x >> 4 & 0x0f0f0f0f);
  x = (x & 0x00ff00ff) + (x >> 8 & 0x00ff00ff);
  return (x & 0x0000ffff) + (x >> 16 & 0x0000ffff);
}

double solve_small(const vector<double> &P, int K) {
  int N = P.size();
  vector<int> data(N);
  iota(data.begin(), data.end(), 0);

  double ans = 0.0;
  do {
    vector<double> tmp(K);
    for (int i = 0; i < K; ++i) tmp[i] = P[data[i]];
    double q = 0.0;
    for (int bitmask = 0; bitmask < (1 << K); ++bitmask) {
      if (bitCount(bitmask) != K / 2) continue;
      double p = 1.0;
      for (int i = 0; i < K; ++i) {
        if (bitmask & (1 << i)) {
          p *= tmp[i];
        } else {
          p *= (1 - tmp[i]);
        }
      }
      q += p;
    }
    chmax(ans, q);
  } while (next_combination(data.begin(), data.begin() + K, data.end()));
  return ans;
}

int main() {
  // cin.tie(0);
  // ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    int N, K;
    cin >> N >> K;
    vector<double> P(N);
    for (int i = 0; i < N; ++i) cin >> P[i];

    // cout << "Case #" << testcase << ": ";
    printf("Case #%d: %.15f\n", testcase, solve_small(P, K));
    // cout << ans << endl;
  }
}
