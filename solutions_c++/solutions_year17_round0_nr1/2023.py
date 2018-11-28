#include <cstdint>
#include <iostream>
#include <vector>

using std::cin;
using std::string;
using namespace std;

void flip(char& c) {
  switch(c) {
    case '+':
      c = '-';
      break;
    case '-':
      c = '+';
      break;
  }
}

void solve(int case_, string s, int n) {
  int count = 0;
  for(int i = 0; i < s.size() - n + 1; ++i) {
    if (s[i] == '-') {
      ++count;
      for(int j = i; j < i + n; ++j) {
        flip(s[j]);
      }
    }
  }
  bool solved = true;
  for(auto c : s) {
    if (c == '-') { solved = false; }
  }
  std::cout << "Case #" << case_ << ": ";
  if (solved) {
    cout << count << "\n";
  } else {
    cout << "IMPOSSIBLE" << "\n";
  }
}

int main() {
  int t_num;
  cin >> t_num;
  for (auto t = 1; t <= t_num; ++t) {
    std::string s;
    cin >> s;
    int n;
    cin >> n;
    solve(t, s, n);
  }
}
