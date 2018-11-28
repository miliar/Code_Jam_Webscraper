#include <stdio.h>
#include <set>
#include <algorithm>
#pragma warning(disable : 4996)
using namespace std;

set<int> intersect(set<int> &s1, set<int> &s2) {
  set<int> ret;
  for (auto it = s2.begin(); it != s2.end(); it++) {
    if (s1.find(*it) != s1.end()) {
      ret.insert(*it);
    }
  }
  return ret;
}

int main(void) {
  int T;
  scanf("%d", &T);
  for (int case_n = 1; case_n <= T; case_n++) {
    set<int> rest_nums;
    for (int i = 1; i <= 16; i++) {
      rest_nums.insert(i);
    }
    for (int i = 0; i < 2; i++) {
      int answer_row;
      set<int> selected_nums;
      scanf("%d", &answer_row);
      for (int r = 1; r <= 4; r++) {
        for (int c = 1; c <= 4; c++) {
          int n;
          scanf("%d", &n);
          if (r == answer_row) {
            selected_nums.insert(n);
          }
        }
      }
      rest_nums = intersect(rest_nums, selected_nums);
    }
    if (rest_nums.size() == 0) {
      printf("Case #%d: Volunteer cheated!\n", case_n);
    }
    else if (rest_nums.size() == 1) {
      printf("Case #%d: %d\n", case_n, *rest_nums.begin());
    }
    else {
      printf("Case #%d: Bad magician!\n", case_n);
    }
  }
}