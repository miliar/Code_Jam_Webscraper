#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <list>
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
  std::ifstream in("A-small-attempt0.in");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    std::string result;

    int a1 = 0;
    in >> a1;

    std::vector<std::vector<int>> F1;

    F1.resize(4);
    for (int i = 0; i < 4; ++i ) {
      F1[i].resize(4);
      for (int j = 0; j < 4; ++j) {
        in >> F1[i][j];
      }
    }

    int a2 = 0;
    in >> a2;

    std::vector<std::vector<int>> F2;

    F2.resize(4);
    for (int i = 0; i < 4; ++i ) {
      F2[i].resize(4);
      for (int j = 0; j < 4; ++j) {
        in >> F2[i][j];
      }
    }

    std::set<int> r1;
    for (int j = 0; j < 4; ++j)
      r1.insert(F1[a1 - 1][j]);

    int n = 0;
    int find_j = 0;
    for (int j = 0; j < 4; ++j) {
      if (r1.find(F2[a2 - 1][j]) != r1.end()) {
        n += 1;
        find_j = j;
      }
    }

    if (n == 1)
      result = Str(F2[a2 - 1][find_j]);
    else if (n == 0)
      result = "Volunteer cheated!";
    else
      result = "Bad magician!";

    out << "Case #" << case_index + 1 << ": " << result << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result << std::endl;
  }
}