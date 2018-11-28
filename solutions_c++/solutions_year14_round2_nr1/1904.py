#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

struct letter {
  char chr = 0;
  int cnt = 0;
};

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    letter words[101][101];
    int N;
    cin >> N;
    string str;
    int max_cur = 0;
    for (int n = 0; n < N; ++n) {
      cin >> str;
      words[n][0].chr = str[0];
      words[n][0].cnt = 1;
      int cur = 0;
      for (int i = 1; i < str.size(); ++i) {
        if (str[i] != words[n][cur].chr) {
          ++cur;
          words[n][cur].chr = str[i];
          words[n][cur].cnt = 1;
        }
        else {
          ++words[n][cur].cnt;
        }
      }
      if (cur > max_cur) max_cur = cur;
    }
    int moves = 0;
    // cout << "max_cur = " << max_cur << endl;
    for (int i = 0; i <= max_cur; ++i) {
      char cur_letter = words[0][i].chr;
      int cur_cnt = 0;
      for (int n = 0; n < N; ++n) {
        if (words[n][i].chr == 0 || words[n][i].chr != cur_letter) {
          moves = -1;
          break;
        }
        cur_cnt += words[n][i].cnt;
      }
      if (moves == -1) break;
      int avg = (int)round((double)cur_cnt / N);
      // cout << cur_letter << " avg = " << avg << endl;
      for (int n = 0; n < N; ++n) {
        moves += abs(words[n][i].cnt - avg);
      }
    }
    cout << "Case #" << (t+1) << ": ";
    if (moves == -1) cout << "Fegla Won";
    else cout << moves;
    cout << endl;
  }
  return 1;
}
