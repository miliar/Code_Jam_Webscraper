#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <algorithm>
#include "print_routines.h"

template<typename Type>
std::string Str(const Type& v) {
  std::ostringstream stream;

  stream << v;
  return stream.str();
}

/*
int main(int argc, char* argv[]) {
  std::ifstream in("in.txt");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    int result = 0;

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}
*/

int main(int argc, char* argv[]) {
  std::ifstream in("A-small-attempt1.in");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    std::string result;

    int N = 0;
    in >> N;

    std::vector<std::string> strings(N);
    for (int i = 0; i < N; ++i) {
      in >> strings[i];
    }

    std::vector<std::vector<int>> counts(N);
    std::vector<std::string> chars(N);

    for (int i = 0; i < N; ++i) {
      char pc = 0;
      int c = 0;
      for (size_t j = 0; j < strings[i].size(); ++j) {
        if (pc != strings[i][j]) {
          if (pc) {
            counts[i].push_back(c);
            chars[i].push_back(pc);

            c = 0;
          }
        }

        pc = strings[i][j];
        c += 1;
      }

      counts[i].push_back(c);
      chars[i].push_back(pc);

      //print(counts[i]);
      //print(chars[i]);
    }

    bool allEq = true;
    for (int i = 0; i < N; ++i)
      if (chars[0] != chars[i]) {
        allEq = false;
        break;
      }

    if (!allEq) {
      result = "Fegla Won";
    } else {
      size_t C = 0;
      for (size_t i = 0; i < counts[0].size(); ++i) {
        int M = 0;
        for (int j = 0; j < N; ++j)
          M += counts[j][i];

        M = M / N;

        for (int j = 0; j < N; ++j) {
          if (counts[j][i] > M)
            C += counts[j][i] - M;
          else if (counts[j][i] < M)
            C += M - counts[j][i];
        }
      }

      result = Str(C);
    }

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}