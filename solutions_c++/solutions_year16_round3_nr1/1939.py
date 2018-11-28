#include <cassert>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solver {
 public:
  void Solve() {
    std::string out;
    while (true) {
      auto p = GetOne();
      if (p == "") break;
      if (not IsValid()) p += GetOne();
      if (out != "") out += " ";
      out += p;
      if (not IsValid()) {
        cerr << "Failed." << endl;
      }
    }
    cout << out << endl;
  }

  string GetOne() {
    std::sort(freq.begin(), freq.end());
    if (freq.back().first == 0) { return ""; }
    char c = freq.back().second;
    freq.back().first--;
    string s;
    s.push_back(c);
    return s;
  }

  bool IsValid() {
    int total = 0;
    for (int i = 0; i < freq.size(); ++i) {
      total += freq[i].first;
    }
    for (int i = 0; i < freq.size(); ++i) {
      if (2 * freq[i].first > total) return false;
    }
    return true;
  }

  int N;
  vector<pair<int, char>> freq;
};

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    Solver solver;
    cout << "Case #" << t + 1 << ": ";
    cin >> solver.N;
    char c = 'A';
    for (int i = 0; i < solver.N; ++i) {
      int a;
      cin >> a;
      solver.freq.push_back({ a, c + i });
    }
    solver.Solve();
  }
}
