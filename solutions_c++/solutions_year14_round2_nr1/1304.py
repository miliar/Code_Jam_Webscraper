#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int m = 1; m <=T; ++m) {
    int N;
    cin >> N;
    vector<string> s;
    for (int i = 0; i < N; ++i) {
      string tmp;
      cin >> tmp;
      s.push_back(tmp);
    }
    int p[N];  // pointers
    for (int i = 0; i < N; ++i) {
      p[i] = 0;
    }
    int final_cnt = 0;
    bool flag = true;
    bool failed_case = false;
    while (flag) {
      int count[N];
      if (p[0] >= s[0].length()) {
        cout << "Case #" << m << ": Fegla Won" << endl;
        flag = false;
        failed_case = true;
        break;
      }
      char first_c = s[0].at(p[0]);
      for (int i = 0; i < N; ++i) {
        string str = s[i];
        if (p[i] >= str.length()) {
          cout << "Case #" << m << ": Fegla Won" << endl;
          flag = false;
          failed_case = true;
          break;
        }
        char c = str.at(p[i]);
        if (c != first_c) {
          cout << "Case #" << m << ": Fegla Won" << endl;
          flag = false;
          failed_case = true;
          break;
        }
        int start_pos = p[i];
        int str_cnt = 0;
        for (int j = start_pos; j < str.length(); ++j) {
          if (c == str[j]) {
            p[i]++;
            str_cnt++;
          } else {
            break;
          }
        }
        count[i] = str_cnt;
      }
      if (flag) {
        vector<int> tmp_count(count, count+N);
        sort(tmp_count.begin(), tmp_count.end());
        int median;
        if (N % 2 == 0) {
          median = (tmp_count[N / 2 - 1] + tmp_count[N / 2]) / 2;
        } else {
          median = tmp_count[(N - 1) / 2];
        }
        for (int i = 0; i < N; ++i) {
          final_cnt += abs(count[i] - median);
        }
        bool all_full = true;
        for (int i = 0; i < N; ++i) {
          if (p[i] < s[i].length()) {
            all_full = false;
          }
        }
        flag = !all_full;
      }
    }
    if (!failed_case) {
      cout << "Case #" << m << ": " << final_cnt << endl;
    }
  }
  return 0;
}
