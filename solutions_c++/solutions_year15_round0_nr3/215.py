#include <iostream>

int main() {
  int forward[9][9] = {
      {3, 2, 7, 8, 4, 0, 1, 6, 5},
      {6, 3, 0, 7, 4, 1, 8, 5, 2},
      {1, 8, 3, 6, 4, 2, 5, 0, 7},
      {8, 7, 6, 5, 4, 3, 2, 1, 0},
      {4, 4, 4, 4, 4, 4, 4, 4, 4},
      {0, 1, 2, 3, 4, 5, 6, 7, 8},
      {7, 0, 5, 2, 4, 6, 3, 8, 1},
      {2, 5, 8, 1, 4, 7, 0, 3, 6},
      {5, 6, 1, 0, 4, 8, 7, 2, 3}};
  int backward[9][9] = {
      {5, 6, 1, 8, 4, 0, 7, 2, 3},
      {2, 5, 8, 7, 4, 1, 0, 3, 6},
      {7, 0, 5, 6, 4, 2, 3, 8, 1},
      {0, 1, 2, 5, 4, 3, 6, 7, 8},
      {4, 4, 4, 4, 4, 4, 4, 4, 4},
      {8, 7, 6, 3, 4, 5, 2, 1, 0},
      {1, 8, 3, 2, 4, 6, 5, 0, 7},
      {6, 3, 0, 1, 4, 7, 8, 5, 2},
      {3, 2, 7, 0, 4, 8, 1, 6, 5}};
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    bool okay = false;
    int L, X;
    std::cin >> L >> X;
    std::string s;
    std::cin >> s;
    int array[10000], single = 5;
    for (int i = 0; i < L; ++i) {
      array[i] = s[i] == 'i' ? 6 : s[i] == 'j' ? 7 : 8;
      single = forward[single][array[i]];
    }
    int final = 5;
    for (int i = X % 4; i > 0; --i) {
      final = forward[final][single];
    }
    if (final == 3 && L * X >= 3) {  // (L >= 3 || X >= 3 || (L == 2 && X == 2))) {
      int start = 0, stop = L * X, p = 5, q = 8;
      for (; start < stop; ++start) {
        p = forward[p][array[start % L]];
        if (p == 6) break;
      }
      for (; stop > start;) {
        q = backward[q][array[--stop % L]];
        if (q == 5) break;
      }
      okay = start + 1 < stop;
    }
    std::cout << "Case #" << t << ": " << (okay ? "YES" : "NO") << "\n";
  }
  return 0;
}
