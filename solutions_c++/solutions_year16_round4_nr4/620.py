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

bool dfs_check(const vector<int> &permutation, vector<bool> &used, int bitmask,
               int pos) {
  if (pos == permutation.size()) return true;
  int N = permutation.size();
  int come = permutation[pos];
  bool workable = false;
  for (int i = 0; i < used.size(); ++i) {
    if (used[i]) continue;
    if (bitmask & (1 << (come * N + i))) {
      used[i] = true;
      if (!dfs_check(permutation, used, bitmask, pos + 1)) return false;
      used[i] = false;
      workable = true;
    }
  }
  if (!workable) return false;
  return true;
}

bool check(int bitmask, int N) {
  vector<int> permutation(N);
  iota(permutation.begin(), permutation.end(), 0);
  do {
    vector<bool> used(N, false);
    if (!dfs_check(permutation, used, bitmask, 0)) return false;
  } while (next_permutation(permutation.begin(), permutation.end()));
  return true;
}

int solve_small(const vector<vector<bool>> &know) {
  int N = know.size();
  int know_mask = 0;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      if (know[i][j]) know_mask |= (1 << (i * N + j));
  int ans = N * N;
  for (int bitmask = 0; bitmask < (1 << (N * N)); ++bitmask) {
    if ((bitmask & know_mask) != know_mask) continue;
    if (check(bitmask, N)) {
      int cost = bitCount(bitmask - know_mask);
      chmin(ans, cost);
    }
  }
  return ans;
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    int N;
    cin >> N;
    vector<string> input(N);
    for (int i = 0; i < N; ++i) cin >> input[i];
    vector<vector<bool>> know(N, vector<bool>(N));
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < N; ++j) know[i][j] = (input[i][j] == '1');

    cout << "Case #" << testcase << ": ";
    cout << solve_small(know) << endl;
  }
}
