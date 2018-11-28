#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <utility>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    string s;
    queue<string> q;
    unordered_map<string, int> count;
    cin >> s;
    q.push(s);
    count[s] = 0;
    while (not q.empty()) {
      string a = q.front();
      int x = count[a];
      q.pop();
      if (a.find('-') == string::npos) {
        cout << "Case #" << case_num << ": " << x << endl;
        q = queue<string>();
      } else {
        for (size_t i = 1; i <= a.size(); ++i) {
          string b = a;
          for (size_t j = 0; j < i; ++j) {
            b[j] = (b[j] == '+'? '-': '+');
          }
          for (size_t j = 0; j < i / 2; ++j) {
            swap(b[j], b[i - 1 - j]);
          }
          if (count.count(b) == 0) {
            count[b] = x + 1;
            q.push(b);
          }
        }
      }
    }
  }
  return 0;
}
