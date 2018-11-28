#include <iomanip>
#include <algorithm>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

template<class T>
ostream& operator<< (ostream& fout, const vector<T>& vec) {
  for (const auto& el : vec) {
    fout << el << ' ';
  }
  return fout;
}

template <class T>
istream& operator>> (istream& fin, vector<T>& vec) {
  for (size_t i = 0; i < vec.size(); ++i) {
    cin >> vec[i];
  }
  return fin;
}

vector<int> bts(int m) {
  vector<int> res;
  while (m) {
    res.push_back(m % 2);
    m /= 2;
  }
  return res;
}
int Solve() {
  int tt = 0;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int64_t b, m;
    cin >> b >> m;
    if (1 << (b - 2) < m) {
      cout << "Case #" << t << ": IMPOSSIBLE\n";
      continue;
    }
    vector<string> res(b, string(b, '0'));
    for (int i = 1; i < b; ++i) {
      res[i - 1][i] = '1';
    }

    auto bits = bts(m);

    int mxb = bits.size() - 1;

    if (bits.size()) {
      bits.pop_back();
    }

    // 2 ^ mxb = b - 1 - mxb
    for (int i = b - mxb - 2; i + 1 < b; ++i) {
      for (int j = i + 1; j < b; ++j) {
        res[i][j] = '1';
      }
    }

    while (bits.size()) {
      // 2 ^ mxb = b - 1 - mxb
      if (bits.back()) {
        int pos = bits.size() - 1;
        cerr << "POS: " << pos << endl;
        cerr << b - 2 - pos << '\n';
        res[0][b - 2 - pos] = '1';
      }
      bits.pop_back();
    }

    cout << "Case #" << t << ": POSSIBLE\n";
    for (auto& str : res) {
      cout << str << '\n';
    }
  }
  return 0;
}


int main() {
#ifndef LOCAL
  //freopen("input.txt", "rt", stdin);
  //freopen("output.txt", "wt", stdout);
#endif
#ifdef LOCAL
  freopen("input.txt", "rt", stdin);
#endif

  ios_base::sync_with_stdio(0);
  cin.tie(0);
  Solve();
  return 0;
}
