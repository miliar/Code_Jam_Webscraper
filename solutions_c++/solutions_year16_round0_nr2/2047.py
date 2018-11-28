#include <iostream>

using namespace std;

int moves_to_make_all_neg(char* s, int len, bool inverted) {
  if (len == 0) {
    return 0;
  }
  bool neg_in_last_position = inverted ? s[len-1] == '+' : s[len-1] == '-';
  if (neg_in_last_position) {
    return moves_to_make_all_neg(s, len-1, inverted);
  } else {
    return 1 + moves_to_make_all_neg(s, len-1, !inverted);
  }
}

int moves_to_make_all_pos(char* s, int len, bool inverted) {
  if (len == 0) {
    return 0;
  }
  bool pos_in_last_position = inverted ? s[len-1] == '-' : s[len-1] == '+';
  if (pos_in_last_position) {
    return moves_to_make_all_pos(s, len-1, inverted);
  } else {
    return 1 + moves_to_make_all_pos(s, len-1, !inverted);
  }
}

int solve(char* s, int len) {
  int solution1 = moves_to_make_all_neg(s, len, false) + 1;
  int solution2 = moves_to_make_all_pos(s, len, false);
  return solution2 < solution1 ? solution2 : solution1;
}

int main() {
  int num_cases;
  cin >> num_cases;
  char s[101];
  for (int i = 0; i < num_cases; i++) {
    cin >> s;
    int solution = solve(s, strlen(s));
    cout << "Case #" << i+1 << ": " << solution << endl;
  }
}

/*
--+-

+-+-

+++-
----
++++

-++-

+-++


*/