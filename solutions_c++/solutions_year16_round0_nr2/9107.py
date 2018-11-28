#include <bits/stdc++.h>
using namespace std;

int num_flips(string pancakes) {
  int i = 0;
  int len = pancakes.length();

  // If pancakes starts with a # of +s, flip them all to -s.
  // Unless they're *all* +s, in which case the pile is sorted.
  if (pancakes[i] == '+') {
    while (pancakes[i] == '+' && i < len) {
      pancakes[i] = '-';
      i++;
    }
    if (i == len) return 0;
    else return num_flips(pancakes) + 1;
  }

  // Otherwise, find the last - and flip stack at that point.
  i = len - 1;
  if (pancakes[i] == '+') {
    while (pancakes[i] == '+') i--;
    pancakes.resize(i + 2);
  }
  // pancakes[i] = '-'
  string new_pancakes;
  while (i >= 0) {
    new_pancakes += (pancakes[i] == '+') ? '-' : '+';
    i--;
  }
  return num_flips(new_pancakes) + 1;
}

int main() {
  int num_cases;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; case_num++) {
    string pancakes;
    cin >> pancakes;
    int ans = num_flips(pancakes);
    printf("Case #%d: %d\n", case_num, ans);
  }
}
