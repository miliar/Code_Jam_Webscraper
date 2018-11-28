#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int test_case_number_ = 0;
#define gout printf("Case #%d: ", ++test_case_number_),cout

void solution() {
  string s;
  cin >> s;
  char last = s[0];
  int answer = 0;
  for (int i = 1; i < s.size(); ++i) {
    if (s[i] != last) {
      ++answer;
    }
    last = s[i];
  }
  if (last != '+') {
    ++answer;
  }
  gout << answer << endl;
}

int main() {
  int test_cases;
  cin >> test_cases;
  for (int t_case = 0; t_case < test_cases; ++t_case) {
    solution();
  }

  return 0;
}
