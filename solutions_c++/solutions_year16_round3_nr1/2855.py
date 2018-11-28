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
#include <vector>

struct Party {
  uint64_t senators;
  std::string name;
  bool operator<(const Party &P) { return senators > P.senators; }
};

void solve(std::istream &Input) {
  std::string parties = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  uint64_t T, N;
  Input >> T;
  for (uint64_t C = 1; C <= T; C++) {
    Input >> N;
    std::vector<Party> P;
    for (auto i = 0; i < N; i++) {
      uint64_t p;
      Input >> p;
      P.push_back(Party{p, parties.substr(i, 1)});
    }

    std::cout << "Case #" << C << ":";

    while (!P.empty()) {
      std::sort(P.begin(), P.end());

      auto A = P.begin();
      auto B = std::next(P.begin());

      if (P.size() == 3 && B->senators == 1) {
        std::cout << " " << A->name;
        A->senators--;
      } else if (B == P.end() || B < A) {
        std::cout << " " << A->name;
        A->senators--;
      } else {
        std::cout << " " << B->name << A->name;
        B->senators--;
        A->senators--;
      }
      if (B->senators == 0)
        P.erase(A, std::next(B));
      else if (A->senators == 0)
        P.erase(A);
    }
    std::cout << "\n";
  }
}
