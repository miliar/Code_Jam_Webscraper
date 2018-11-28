#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

using namespace std;

int solve(vector<bool> b, int k) {
  int count = 0;
  int len = b.size();
  for (int i = 0; i < len - k + 1; ++i) {
    if (!b[i]) {
      for (int j = 0; j < k; ++j) {
        b[j + i] = !b[j + i];
      }
      ++count;
    }
  }
  bool s = true;
  for (int i = 0; i < k; ++i) {
    s = s && b[len - i - 1];
  }
  return (s? count: -1);
}

int main() {
  int n = 0;
  scanf("%d\n", &n);
  string line;
  for (int i = 0; i < n; ++i) {
    getline(cin, line);
    string a;
    int pos = line.find(' ');
    string p = line.substr(0, pos);
    vector<bool> b;
    for (auto c: p) {
      b.push_back(c == '+');
    }
    int k = stoul(line.substr(pos));
    int ans = solve(b, k);
    cout << "Case #" << i + 1 << ": " << (ans >= 0? to_string(ans): "IMPOSSIBLE") << endl;
  }
}
