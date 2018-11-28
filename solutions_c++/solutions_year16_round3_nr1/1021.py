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
    set<pair<int, char>> hp;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
      int buf;
      cin >> buf;
      hp.insert({buf, i + 'A'});
      sum += buf;
    }

    cout << "Case #" << t << ": ";
    while (true) {
      string res = "";
      if (sum % 2) {
        auto mx = std::prev(hp.end());
        auto val = *mx;
        hp.erase(mx);
        res.push_back(val.second);
        if (--val.first) {
          hp.insert(val);
        }
        --sum;
      } else {
        for (int i = 0; i < 2; ++i) {
          if (hp.empty()) {
            break;
          }
          auto mx = std::prev(hp.end());
          auto val = *mx;
          hp.erase(mx);
          res.push_back(val.second);
          --sum;
          if (--val.first) {
            hp.insert(val);
          }
        }
      }
      if (res != "") {
        cout << res << ' ';
      }
      if (hp.empty()) {
        break;
      }
    }
    cout << endl;

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
