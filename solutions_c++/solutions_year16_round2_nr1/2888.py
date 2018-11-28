#include <cstdint>
#include <fstream>
#include <iostream>

void solve(std::istream &Input);

int main(int argc, const char **argv) {
  if (argc == 2) {
    std::fstream Input(argv[1]);
    solve(Input);
  } else if (argc == 1) {
    solve(std::cin);
  } else {
    std::cout << "Usage: " << argv[0] << " [InputFile]\n";
  }
}
#include <algorithm>
#include <cassert>
#include <vector>

void remove(std::vector<char> &letters, std::string number, int occurances) {
  for (auto letter : number) {
    for (int i = 0; i < occurances; i++) {
      // std::cerr << letter << " " << occurances << "\n";
      auto P = std::find(letters.begin(), letters.end(), letter);
      assert(P != letters.end());
      letters.erase(P);
    }
  }
}

struct Digit {
  char key;
  std::string name;
  int digit;
};

void solve(std::istream &Input) {
  uint64_t T;
  Input >> T;

  Digit Digits[] = {{'Z', "ZERO", 0}, {'W', "TWO", 2},   {'U', "FOUR", 4},
                    {'X', "SIX", 6},  {'G', "EIGHT", 8}, {'H', "THREE", 3},
                    {'F', "FIVE", 5}, {'S', "SEVEN", 7}, {'O', "ONE", 1},
                    {'I', "NINE", 9}};

  for (uint64_t C = 1; C <= T; C++) {
    std::string S;
    Input >> S;
    std::vector<char> letters(S.begin(), S.end());
    std::vector<int> result;

    for (auto D : Digits) {
      int n = std::count(letters.begin(), letters.end(), D.key);
      if (n > 0) {
        // std::cerr << n << ": " << D.key << " " << D.digit << "\n";
        remove(letters, D.name, n);
        for (int i = 0; i < n; i++)
          result.push_back(D.digit);
      }
    }

    std::sort(result.begin(), result.end());
    std::cout << "Case #" << C << ": ";
    for (auto d : result)
      std::cout << d;
    std::cout << "\n";
  }
}
