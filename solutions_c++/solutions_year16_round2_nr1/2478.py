#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string digits[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
pair<int, char> order[] = { {0, 'Z'}, {2, 'W'}, {6, 'X'}, {8, 'G'}, {7, 'S'}, {3, 'H'}, {4, 'R'}, {5, 'F'}, {1, 'O'}, {9, 'I'} };

int main() {
  ios::sync_with_stdio(false);
  freopen("test.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  
  int cnt_tests;
  cin >> cnt_tests;

  for (int test = 1; test <= cnt_tests; ++test) {
    string str;
    cin >> str;
    vector<int> cnt(26);
    for (int i = 0; i < str.size(); ++i) {
      ++cnt[str[i] - 'A'];
    }

    vector<int> ans;
    for (int i = 0; i < 10; ++i) {
      int dig = order[i].first;
      int ind = order[i].second - 'A';
      int cur = cnt[ind];
      for (int k = 0; k < cur; ++k) {
        ans.push_back(dig);
      }
      for (int k = 0; k < digits[dig].size(); ++k) {
        cnt[digits[dig][k] - 'A'] -= cur;
      }
    }

    sort(ans.begin(), ans.end());
    printf("Case #%d: ", test);
    for (int i = 0; i < ans.size(); ++i) {
      cout << ans[i];
    }
    cout << endl;
  }

  return 0;
}