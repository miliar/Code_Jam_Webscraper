#include <algorithm>
#include <bitset>
#include <cassert>
#include <cinttypes>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

void Solve() {
  string S;
  cin >> S;

  int result = 0;
  for (;;) {
    string st;
    for (char ch : S) {
      if (!st.empty() && st.back() == ch) {
        result += 10;
        st.pop_back();
      } else {
        st.push_back(ch);
      }
    }

    if (st.empty()) {
      break;
    }
    if (st == S) {
      assert(st.size() % 2 == 0);
      result += 5 * st.size() / 2;
      break;
    }

    S.swap(st);
  }

  cout << result << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/A-large.in", "rb", stdin);
  freopen("../Console/A-large.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
  }

  return 0;
}
