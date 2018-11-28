#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
const int kMAX = 1000;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string s;
    cin >> s;
    unordered_map<char, int> m;
    for (int i = 0; i < s.size(); ++i) {
      if (m.count(s[i]) == 0) {
        m[s[i]] = 0;
      }
      m[s[i]]++;
    }
    vector<string> digits = {"ZERO", "TWO", "FOUR", "FIVE", "THREE", "SIX", "SEVEN", "EIGHT", "NINE", "ONE"};
    vector <int> vals = {0, 2, 4, 5, 3, 6, 7, 8, 9, 1};
    vector<int> numbers;
    vector<int> inds;
    for (int i = 0; i < digits.size(); ++i) {
      int mc = kMAX;
      for (int j = 0; j < digits[i].size(); ++j) {
        char c = digits[i][j];
        if (m.count(digits[i][j]) > 0) {
          if (m[c] > 0) {
            if (((vals[i] == 3) || (vals[i] == 7)) && c == 'E') {
              if (m[c] < 2) {
                mc = kMAX;
                break;
              }
            }
            if ((vals[i] == 9) && c == 'N') {
              if (m[c] < 2) {
                mc = kMAX;
                break;
              }
            }
            if (m[digits[i][j]] < mc) {
              mc = m[digits[i][j]];
            }
          } else {
            mc = kMAX;
            break;
          }
        } else {
          mc = kMAX;
          break;
        }
      }
      if (mc != kMAX) {
        /*
        cout << i << " " << mc << endl;
        for (auto it = m.begin(); it != m.end(); ++it) {
          cout << it->first << " " << it->second << endl;
        }
        cout << endl;
        */
        for (int j = 0; j < mc; ++j) {
          inds.push_back(i);
          numbers.push_back(vals[i]);
        }
        for (int j = 0; j < digits[i].size(); ++j) {
          /*
          char c = digits[i][j];
          if (((i == 3) || (i == 7)) && c == 'E') {
            m[digits[i][j]] -= mc;
          }
          if ((i == 9) && (c == 'N')) {
            m[digits[i][j]] -= mc;
          }
          */
          m[digits[i][j]] -= mc;

        }
      }
    }
    sort(numbers.begin(), numbers.end());
    string ans;
    int l = 0;
    for (int j = 0; j < numbers.size(); ++j) {
      ans.push_back('0' + numbers[j]);
    }
    for (int j = 0; j < inds.size(); ++j) {
      l += digits[inds[j]].size();
    }
    cout << "Case #" << t << ": " << ans << endl;
    if (l != s.size()) {
      cout << "Error " << s << endl;
    }
  }
}
