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
  std::ifstream in("D-large.in");

  std::ofstream out("out.txt");

  int num_cases = 0;
  in >> num_cases;

  for (int case_index = 0; case_index < num_cases; ++case_index) {
    int result1 = 0;
    int result2 = 0;

    int N = 0;
    in >> N;

    std::vector<double> naomi(N);
    for (int i = 0; i < N; ++i)
      in >> naomi[i];

    std::vector<double> ken(N);
    for (int i = 0; i < N; ++i)
      in >> ken[i];

    std::sort(naomi.begin(), naomi.end());
    std::sort(ken.begin(), ken.end());

    auto n1 = naomi;
    auto k1 = ken;
    for (int i = 0; i < N; ++i) {
      double n = n1[i];

      int find_j = -1;
      for (int j = k1.size() - 1; j >= 0; --j) {
        if (k1[j] > n)
          find_j = j;
        else
          break;
      }

      int rem_j = 0;
      if (find_j != -1)
        rem_j = find_j;
      else
        result2 += 1;

      k1.erase(k1.begin() + rem_j);
    }

    auto n2 = naomi;
    auto k2 = ken;
    for (int i = 0; i < N; ++i) {
      double n = n2[i];

      int rem_j = 0;
      if (k2[0] < n) {
        result1 += 1;
        rem_j = 0;
      } else {
        rem_j = k2.size() - 1;
      }

      k2.erase(k2.begin() + rem_j);
    }

    out << "Case #" << case_index + 1 << ": " << result1 << " " << result2 << std::endl;
    std::cout << "Case #" << case_index + 1 << ": " << result1 << " " << result2 << std::endl;
  }
}