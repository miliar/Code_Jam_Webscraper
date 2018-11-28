#if defined(__clang__)
#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <complex>
#include <deque>
#include <forward_list>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#endif

#define inf(T) (numeric_limits<T>::min())
#define sup(T) (numeric_limits<T>::max())
#define rep(i,n) for (int i = 0; i < (n); i++)
#define asc(c) begin(c), end(c)
#define desc(c) reverse_iterator<decltype(c)::iterator>(c.end()), reverse_iterator<decltype(c)::iterator>(c.begin())
#define ascend(l,r) l = max(l, r)
#define descend(l,r) l = min(l, r)
#define mp(...) make_pair(__VA_ARGS__)
#define mt(...) make_tuple(__VA_ARGS__)

using namespace std;

using ll = long long;
using ld = long double;

template <class Key>          using uset = unordered_set<Key>;
template <class Key, class T> using umap = unordered_map<Key, T>;

int main()
{
  cin.tie(0);
  ios::sync_with_stdio(false);

  int T;
  cin >> T;

  rep(t,T) {
    int S_max;
    cin >> S_max;
    string s;
    cin >> s;

    int ans = 0;
    int acc = 0;
    rep(i,S_max+1) {
      if (s[i] == '0') continue;
      if (acc < i) {
        ans += i - acc;
        acc = i;
      }
      acc += s[i] - '0';
    }

    cout << "Case #" << t + 1 << ": " << ans << endl;
  }

  return 0;
}
