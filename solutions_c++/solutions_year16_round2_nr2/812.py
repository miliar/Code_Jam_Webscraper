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

bool match(const string& argc, int value) {
  string arg = argc;
  reverse(arg.begin(), arg.end());
  string res = "";
  while (value) {
    res.push_back(value % 10 + '0');
    value /= 10;
  }
  if (res.size() > arg.size()) {
    return false;
  }
  for (int i = 0; i < (int) min(res.size(), arg.size()); ++i) {
    if (arg[i] != '?' && arg[i] != res[i]) {
      return false;
    }
  }

  for (int i = (int) min(res.size(), arg.size()); i < (int) max(res.size(), arg.size()); ++i) {
    if (arg[i] != '?' && arg[i] != '0') {
      return false;
    }
  }
  return true;
}

string canon(const string& arg, int value) {
  string res = "";
  while (value) {
    res.push_back(value % 10 + '0');
    value /= 10;
  }
  for (int i = res.size(); i < (int) arg.size(); ++i) {
    res.push_back('0');
  }
  reverse(res.begin(), res.end());
  return res;
}

int Solve() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    string a, b;
    cin >> a >> b;
    int mx = 1e9;
    int an = 0;
    int bn = 0;
    for (int i = 0; i < 1000; ++i) {
      for (int j = 0; j < 1000; ++j) {
        if (match(a, i) && match(b, j)) {
          if (mx > abs(i - j)) {
            mx = abs(i - j);
            an = i;
            bn = j;
          }
        }
      }
    }
    cout << "Case #" << t << ": ";
    cout << canon(a, an) << ' ' << canon(b, bn) << '\n';
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
