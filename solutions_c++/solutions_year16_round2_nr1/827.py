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
  vector<pair<string, int>> nu = { {"ZERO", 0}, {"TWO", 2}, {"SIX", 6}, {"EIGHT", 8}, {"FOUR", 4}, {"FIVE", 5}, {"SEVEN", 7}, {"ONE", 1}, {"THREE", 3}, {"NINE", 9}};
  int tt;
  cin >> tt;
  for (int t = 0; t < tt; ++t) {
    string input;
    cin >> input;
    vector<int> pattern(26);
    for (const char ch : input) {
      ++pattern[ch - 'A'];
    }
    vector<int> res(10);
    for (const pair<string, int>& num : nu) {
      int mn = 1e9;
      for (const char ch: num.first) {
        mn = min(pattern[ch - 'A'], mn);
      }
      for (const char ch: num.first) {
        pattern[ch - 'A'] -= mn;
      }
      res[num.second] += mn;
    }
    cout << "Case #" << t + 1 << ": ";
    for (int j = 0; j < 10; ++j) {
      for (int i = 0; i < res[j]; ++i) {
        cout  << j;
      }
    }
    cout << "\n";
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
