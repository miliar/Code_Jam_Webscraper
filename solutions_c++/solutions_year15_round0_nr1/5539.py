#include <iostream>
#include <string>

int main() {
  int t = 1, T;
  std::cin >> T;

  while(t <= T) {
    int Smax;
    std::string S;

    std::cin >> Smax;
    std::cin >> S;

    int standing = 0;
    int add_friends = 0;
    for (int shy_lvl = 0; shy_lvl < S.size(); ++shy_lvl) {
      if (standing >= Smax)
        break;
      int peps = S[shy_lvl] - '0';
      if (peps > 0 && standing < shy_lvl) {
        add_friends += shy_lvl - standing;
        standing = shy_lvl;
      }
      standing += peps;
    }
    std::cout << "Case #" << t << ": " << add_friends << '\n';
    ++t;
  }
}
