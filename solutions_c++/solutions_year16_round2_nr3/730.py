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

int Solve() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int n;
    cin >> n;
    vector<pair<string, string>> input;
    for (int i = 0; i < n; ++i) {
      string a, b;
      cin >> a >> b;
      input.push_back({a, b});
    }

    int mx = 0;
    for (int i = 0; i <= (1 << n); ++i) {
      set<string> fs;
      set<string> sc;
      vector<pair<string, string>> fake;
      for (int j = 0; j < n; ++j) {
        if ((i >> j) & 1) {
          fs.insert(input[j].first);
          sc.insert(input[j].second);
        } else {
          fake.push_back(input[j]);
        }

        bool invalid = false;
        for (const auto& el : fake) {
          if (fs.find(el.first) == fs.end() || sc.find(el.second) == sc.end()) {
            invalid = true;
          }
        }
        if (!invalid) {
          mx = max((int) fake.size(), mx);
        }
      }
    }
    cout << "Case #" << t << ": ";
    cout << mx << "\n";
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
