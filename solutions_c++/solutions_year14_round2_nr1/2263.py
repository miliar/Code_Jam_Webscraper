#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int average_of_char(vector<string> strings, char c);
int char_count_of_first(string str, char c);

int average_of_char(vector<string> strings, char c) {
  int average = 0;
  for (int i = 0; i < strings.size(); i++) {
    int count = char_count_of_first(strings[i], c);
    if (count == 0) return -1;
    average += count;
  }
  return average / strings.size();
}
int char_count_of_first(string str, char c) {
  int count = 0;
  for (int i = 0; i < str.size(); i++) {
    if (c == str[i]) {
      count++;
    } else {
      return count;
    }
  }
  return count;
}

int action_for_str(string& str, char c, int num) {
  int actual_num = char_count_of_first(str, c);
  int diff = actual_num - num;
  str.erase(0, actual_num);
  //  printf("str %s\n", str.c_str());
  //  printf("actual_num %d num %d\n", actual_num, num);
  return diff >= 0 ? diff : -diff;
}

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;

    vector<string> strings;

    for (int i = 0; i < N; i++) {
      string str;
      cin >> str;
      strings.push_back(str);
      //      printf("%d [%d]=%s\n", t, i, str.c_str());
    }

    int base_str_index = 0;
    for (int i = 0; i < N; i++) {
      if (strings[i].size() > strings[base_str_index].size()) {
        base_str_index = i;
      }
    }

    bool impossible = false;
    int action_num = 0;
    while (!strings[base_str_index].empty()) {
      //        printf("%d %s\n", 0, strings[0].c_str());
      char c = strings[base_str_index][0];
      int c_length = average_of_char(strings, c);
      if (c_length == -1) {
        //        printf("impossible \n");
        impossible = true;
        break;
      }
      for (int i = 0; i < strings.size(); i++) {
        action_num += action_for_str(strings[i], c, c_length);
      }
      //      printf("%c length %d %s\n", c, c_length, strings[0].c_str());
    }
    if (impossible) {
      printf("Case #%d: Fegla Won\n", t);
    } else {
      printf("Case #%d: %d\n", t, action_num);
    }
  }
}
